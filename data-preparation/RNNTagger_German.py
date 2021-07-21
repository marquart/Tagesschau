import sys, os, pickle, torch, re
from io import StringIO, BytesIO

class RNNTagger_German:

    class Args:
        def __init__(self, path, lib):
            self.path_param = os.path.join(path, "lib", lib, "german")
            self.batch_size = 32
            self.crf_beam_size = 10
            self.beam_size = 0
            self.gpu = 0
            self.quiet = False
            self.print_probs = False
            self.print_source = True
            self.data_buffer = None
    
    def __init__(self, path):
        '''
        Load the models of RNNTagger by Helmut Schmid.
        Parameter path is the directory where the RNNTagger is located.
        To get the german lemmatized words of a text, run process_tokens(doc, filter_tags=filtertags, stop_words=stop_words)
        where doc is a list of sentences with tokenized words, filter_tags is a tuple with the tags you want
        and stopwords is is an optional tuple or list with the stopwords you don't want in your result
        '''

        sys.path.insert(0, os.path.join(path, "PyRNN"))
        
        try:
            from RNN_Data import Data as RNNData
            from CRFTagger import CRFTagger
            from RNNTagger import RNNTagger
            from rnn_annotate import run_tagging
        except ModuleNotFoundError as error:
            print(error, f"\nPlease make sure that the files RNN_Data, CRFTagger, RNNTagger, rnn_annotate are located in {os.path.join(path, 'PyRNN')}.\n They should be included in the distribution of this implementation.\n")
            exit()
        sys.path.insert(0, os.path.join(path, "PyNMT"))
        
        try:
            from Data import Data as NMTData
            from NMT import NMTDecoder
            from nmt_translate import translate
        except ModuleNotFoundError as error:
            print(error, f"\nPlease make sure that the files Data, NMT, nmt_translate are located in {os.path.join(path, 'PyNMT')}.\n They should be included in the distribution of this implementation.\n")
            exit()
            
        self.run_tagging = run_tagging
        self.translate = translate
            
        self.Tagger_Args     = self.Args(path, "PyRNN")
        self.Lemmatizer_Args = self.Args(path, "PyNMT")
        
        # tagger
        self.tag_data  = RNNData(self.Tagger_Args.path_param+".io") 
        with open(self.Tagger_Args.path_param+".hyper", "rb") as file:
            self.tag_hyper_params = pickle.load(file)
        self.tag_model = CRFTagger(*self.tag_hyper_params) if len(self.tag_hyper_params)==10 else RNNTagger(*self.tag_hyper_params)
        self.tag_model.load_state_dict(torch.load(self.Tagger_Args.path_param+".rnn"))
        
        # Lemmatizer
        self.lemma_data = NMTData(self.Lemmatizer_Args.path_param+".io", self.Lemmatizer_Args.batch_size)
        with open(self.Lemmatizer_Args.path_param+".hyper", "rb") as file:
            self.lemma_hyper_params = pickle.load(file)
        self.lemma_model = NMTDecoder(*self.lemma_hyper_params)
        self.lemma_model.load_state_dict( torch.load(self.Lemmatizer_Args.path_param+".nmt") )   # read the model
        
        self.stopwords = ()


    def process_tokens(self, doc, filter_tags=(), stopwords=()):
        '''
        To get the german lemmatized words of a text, run process_tokens(doc, filter_tags=filtertags, stop_words=stop_words)
        where doc is a list of sentences with tokenized words, filter_tags is an optional tuple or list with the tags you want
        and stopwords is is an optional tuple or list with the stopwords you don't want in your result
        '''
        def invalid_word(word):
            return word == '<unk>' or word in self.stopwords or word.lower() in self.stopwords or bool(re.search(".*\d.*", word))
        
        def get_tokens_after_lemma(lemmatized_token_string):
            result = []
            for line_string in lemmatized_token_string.split("\n\n"):
                lines = line_string.split("\n")
                if len(lines)<2: continue
                word = lines[1].replace(' ', '')
                if invalid_word(word): continue
                result.append(word.lower())
            return result



        def reformat_for_lemma(tagged_token_string, filter_tags=()):
            result = []
            for line in tagged_token_string.split('\n'):
                if line:
                    word_tag = line.split("\t")
                    if len(word_tag[0])<2: continue #Punctuation
                    if word_tag[1].startswith('A'): word_tag[0] = word_tag[0].lower()
                    if filter_tags:
                        try:
                            tag = word_tag[1].split('.')[0]
                        except IndexError: continue
                        if tag in filter_tags: result.append(f"{' '.join(word_tag[0])} ## {' '.join(word_tag[1])}")
                    else: result.append(f"{' '.join(word_tag[0])} ## {' '.join(word_tag[1])}")
            return "\n".join(result)


        def tag(doc):
            result = ""
            with StringIO() as feeder:
                for snt in doc:
                    for token in snt:
                        feeder.write(f"{token.text}\n") #{token.tag_} # after sentences must come a newline
                    feeder.write("\n") #{token.tag_} # after sentences must come a newline
                feeder.seek(0)
                self.Tagger_Args.data_buffer = feeder
                with StringIO() as catcher:
                    notebook_io_out = sys.stdout
                    notebook_io_err = sys.stderr
                    sys.stdout = catcher
                    sys.stderr = catcher
                    self.run_tagging(self.Tagger_Args, self.tag_data, self.tag_hyper_params, self.tag_model)
                    sys.stdout = notebook_io_out
                    sys.stderr = notebook_io_err
                    result = "%s" % catcher.getvalue()
            cleaned =  re.sub("\d?\d\r", '', result).replace("\n\n", "\n")
            return re.sub("^\d(?=[A-Z])", '', cleaned, flags=re.MULTILINE) # re.sub("\$\.\n\d(?=[A-Z])", '$.\n', s)
            #return re.sub("\d?\d\r", '', result.encode('cp1252').decode('utf-8')).replace("\n\n", "\n")

        def lemma(tokens):
            result = ""
            with StringIO(tokens) as feeder:
                feeder.seek(0)
                with StringIO() as catcher:
                    notebook_io_out = sys.stdout
                    notebook_io_err = sys.stderr
                    sys.stdout = catcher
                    sys.stderr = catcher
                    self.translate(self.Lemmatizer_Args, self.lemma_data, self.lemma_model, feeder)
                    sys.stdout = notebook_io_out
                    sys.stderr = notebook_io_err
                    result = "%s" % catcher.getvalue()
            return result #result.encode('cp1252').decode('utf-8')
        
        self.stopwords = stopwords
        tagged = tag(doc)
        if not tagged: return []
        lemma_format = reformat_for_lemma(tagged, filter_tags=filter_tags)
        if not lemma_format: return []
        lemmatized = lemma(lemma_format)
        if not lemmatized: return []
        return get_tokens_after_lemma(lemmatized)
    
