<template>
    <div class="SearchBar">
        <div class="navmode">
            <div class="selectmode" :style="searchStyle" @click="showTopwords=false">Begriffs-Suche</div>
            <div class="selectmode" :style="selectStyle" @click="showTopwords=true">Auswählen von pro Monat herausstechenden Begriffen</div>
        </div>
        <div class="autocomplete">
            <p>{{words.length}} Wörter geladen</p>

            <div v-show="!showTopwords">
                <input class="searchfield"
                    placeholder="Bitte gib einen Suchbegriff ein und suche mit Enter"
                    v-model="searchString"
                    type="text"
                    @keydown.enter="setResults(false)"
                />
                <input type="submit" value="Suche" id="button" @click="setResults(false)"
                />
            </div>
            <TopWordSelect v-show="showTopwords" @showResults="setResults"/>

            <ul class="autocomplete-results" v-show="isOpen" >
                <li class="autocomplete-result"
                    v-for="(result, i) in results"
                    :key="i"
                    @click="addWord(result)"
                >
                    {{result}}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import TopWordSelect from './TopWordSelect.vue'

export default {
    name: 'SearchBar',
    components: {
      TopWordSelect
    },
    props: {
        words: Array
    },
    data() {
        return {
            searchString: '',
            results: [],
            isOpen: false,

            showTopwords: false,
            searchStyle: {background: '#ffffff'},
            selectStyle: {background: '#f1f0ed'},
        }
    },
    watch: {
        showTopwords() {
            if (this.showTopwords){
                this.selectStyle.background = '#ffffff';
                this.searchStyle.background = '#f1f0ed';
            } else {
                this.selectStyle.background = '#f1f0ed';
                this.searchStyle.background = '#ffffff';
            }
        }
    },
    methods: {
        addWord(result) {
            //this.showTopwords = false;
            this.isOpen = false;
            this.$emit('add', result)
        },

        setResults(selectedTopwords) {
            this.isOpen = true;
            //this.showTopwords = false;
            if (selectedTopwords) this.results = selectedTopwords;
            else if (this.searchString.length >=2) {
                //this.results = Array.from(this.filterWords());
                //this.isOpen = true;
                this.results = Array.from(this.filterWords());
            }
            this.searchString = '';
        },

        * filterWords() {
            let maxSize = 80;
            if (maxSize > this.words.length) {
                maxSize = this.words.length;
            }
            let count = 0;
            let i = 0;
            let string = this.searchString.toLowerCase();
            while (count < maxSize && i < this.words.length) {
                if (this.words[i].indexOf(string) != -1) {
                    yield this.words[i];
                    count++;
                }
                i++;
            }
        },
        handleClickOutside(event) {
            if (!this.$el.contains(event.target)) {
                this.isOpen = false;
            }
        }
    },
    mounted() {
        document.addEventListener('click', this.handleClickOutside); // Close results if clicked outside of component
    },
    destroyed() {
        document.removeEventListener('click', this.handleClickOutside); // Close results if clicked outside of component
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .SearchBar {
        margin-left: 5%;
        margin-right: 5%;
        text-align: center;
        width: 90%;
    }

    .autocomplete {
        padding: 0.7em;
        /*box-shadow: 0.5em 0.4em #5a5a5a;*/
        /*background-color: #f1f1f1; /*#dcdcdc;*/
        background: linear-gradient(to bottom, #ffffff,  #e2e1dc );
        box-sizing: border-box;

    }
    .navmode {
        width: 100%;
        height: auto;
    }

    .selectmode {
        width: 50%;
        font-size: 1.2em;
        font-family: inherit;
        display: inline-block;
        text-align: center;
        background: #ffffff;
        color: black;
        padding-top: 0.5em;
        padding-bottom: 0.5em;
    }

    .selectmode:hover {
        cursor: pointer;
        background: #e2e1dc;
    }

    .searchfield {
        box-sizing: border-box;
        width: 60%;
        font-size: 1.2em;
        font-family: inherit;
    }

    ::placeholder {
        font-style: italic;
    }

    #button {
        box-sizing: border-box;
        display: inline;
        font-size: 1.2em;
        margin: 1.2em;
        font-family: inherit;
        cursor: pointer;
    }

    .autocomplete-results {
        padding: 0;
        margin: 0;
        /*border: 1px solid #eeeeee;*/
        height: 8em;
        min-height: 1em;
        max-height: 18em;
        overflow: auto;
        color: black;
    }

    .autocomplete-result {
        list-style: none;
        text-align: left;
        padding: 4px 2px;
        cursor: pointer;
    }

    .autocomplete-result:hover {
        background-color:  rgb(1, 69, 150); /*#4AAE9B;*/
        color: white;
    }

    p {
        margin-top: 0;
        margin-bottom: 0;
        text-align: center;
        color: black;
    }
</style>
