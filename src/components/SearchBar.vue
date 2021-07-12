<template>
    <div class="SearchBar">
    <p>{{words.length}} Wörter geladen</p>

        <div class="autocomplete">
            <input class="searchfield"
                placeholder="Bitte gib einen Suchbegriff ein und suche mit Enter"
                v-model="searchString"
                type="text"
                @keydown.enter="setResults"
            />
            <input type="submit" value="Suche" id="button" @click="setResults"
            />
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
export default {
    name: 'SearchBar',
    props: {
        words: Array
    },
    data() {
        return {
            searchString: '',
            results: [],
            isOpen: false
        }
    },
    computed: {

    },
    methods: {
        addWord(result) {
            this.isOpen = false;
            this.$emit('add', result)
        },
        setResults() {
            this.isOpen = true;
            if (this.searchString.length >=2) {
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
    background-color: #f1f1f1; /*#dcdcdc;*/
    box-sizing: border-box;

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
</style>
