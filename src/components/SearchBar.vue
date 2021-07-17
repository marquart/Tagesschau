<template>
    <div class="SearchBar">
        
        <div class="autocomplete">
            <p>{{words.length}} Wörter geladen</p>
            <input class="searchfield"
                placeholder="Bitte gib einen Suchbegriff ein und suche mit Enter"
                v-model="searchString"
                type="text"
                @keydown.enter="setResults(false)"
            />
            <input type="submit" value="Suche" id="button" @click="setResults(false)"
            />
            <div>
                <p class="infotoggle" @click="toggleTopwords">Oder wähle einen Begriff mit einem hohen <a href="https://de.wikipedia.org/wiki/Tf-idf-Ma%C3%9F" target="_blank">Tf-idf-Wert</a> aus einem Monat {{openedTopwords}}</p>
                <div v-show="showTopwords">
                    <select class="selectfield"
                        v-model="selectedYear">
                        <option disabled selected value="Wähle ein Jahr aus">Wähle ein Jahr aus</option>
                        <option class="selectoption"
                            v-for="(year, i) in Object.keys(topwords)"
                            :key="i"
                            :value="year"
                        >
                            {{year}}
                        </option>
                    </select>
                    <select class="selectfield"
                        v-if="selectedYear"
                        v-model="selectedMonth">
                        <option disabled selected value="Wähle einen Monat aus">Wähle einen Monat aus</option>
                        <option class="selectoption"
                            v-for="(month, i) in Object.keys(topwords[selectedYear])"
                            :key="i"
                            :value="month"
                        >
                            {{month}}
                        </option>
                    </select>
                
                </div>
            </div>
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
import top_tfidf_words from '../../public/year_month_topwords.json'

export default {
    name: 'SearchBar',
    props: {
        words: Array
    },
    data() {
        return {
            searchString: '',
            results: [],
            isOpen: false,

            topwords: top_tfidf_words,
            showTopwords: false,
            selectedYear: 0,
            selectedMonth: ''
        }
    },
    computed: {
        openedTopwords() {
            if (this.showTopwords) return "▼";
            else return "▶";
        }

    },
    watch: {
        selectedMonth() {
            if (this.topwords.hasOwnProperty(this.selectedYear) && this.topwords[this.selectedYear].hasOwnProperty(this.selectedMonth)) {
                this.setResults(true)
            }
        }
    },
    methods: {
        addWord(result) {
            this.showTopwords = false;
            this.isOpen = false;
            this.$emit('add', result)
        },

        setResults(from_topwords) {
            this.isOpen = true;
            this.showTopwords = false;
            if (from_topwords) this.results = this.topwords[this.selectedYear][this.selectedMonth];
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
        },

        toggleTopwords() {
            if (this.showTopwords) this.showTopwords = false;
            else this.showTopwords = true;
            this.selectedMonth = '';
            this.selectedYear = 0;
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

    .selectfield {
        font-size: 1.2em;
        font-family: inherit;
        margin: 0.3em;
    }

    .selectfield:hover, .selectoption:hover {
        cursor: pointer;
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
