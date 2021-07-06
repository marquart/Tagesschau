<template>
  <div id="app">
    <h1>Tagesschau</h1>
    <SearchBar :words="words"  @add="addWord"/>
    <div v-if="showerror" class="errormsg" @click="hideError">{{errorstring}}</div>
    <Selection :words="selectedWords" :colors="colors" @delete="deleteWordFromIndex"/>
    <Canvas :selectedNumbers="selectedNumbers" :colors="colors" :dates="dates"/>
  </div>
</template>

<script>
// required from npm:
// npm install -D sass-loader@10.2.0 sass
// npm install d3

import SearchBar from './components/SearchBar.vue'
import Canvas from './components/Canvas.vue'
import Selection from './components/Selection.vue'

export default {
    name: 'App',
    components: {
      SearchBar,
      Selection,
      Canvas
    },

    data() {
      return {
        colors : ["#56ae6c","#9350a1","#697cd4","#ba496b","#53b3b6"],
        numbers: {},
        words: [],
        selectedWords: [],
        selectedNumbers: [],
        dates: [],
        showerror: false,
        errorstring: ""
      }
    },

    mounted() {
      this.fetchData();
    }, 

    methods: {


      async fetchData() {
        let result = await fetch("table.json")
          .then(response => response.json())
          .then(data => this.numbers = data);

        this.words = Object.keys(this.numbers);

        this.fillDates();
        return result;
      },

      fillDates() {
        let year = 2014,
            month = 5;
        for (let i = 0; i<this.numbers["merkel"].length; i++) {
          if (month > 12) {
            month = 1;
            year++;
          }
          this.dates.push(new Date(year, month));
          month++;
          
        }
      },

      addWord(newWord) {

        if (this.selectedWords.length < this.colors.length && !this.selectedWords.includes(newWord)) {
          this.hideError();
          this.selectedNumbers.length = 0;
          this.selectedWords.push(newWord)
          this.selectedWords.forEach(element => {
            this.selectedNumbers.push(this.numbers[element]);
          });
        } else {
          this.errorstring = "Bitte wähle höchstens fünf einzigartige Begriffe aus";
          this.showerror = true;
        }
      },

      hideError() {
        this.showerror = false;
      },

      deleteWordFromIndex(index) {
        if (index>=0 && index < this.selectedWords.length) {
          this.hideError();
          this.selectedWords.splice(index, 1);
          this.selectedNumbers.splice(index, 1);
        }
      }

    },

    computed: {
      
    },

    destroyed() {

    }

}
</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Barlow');

  body, html {
    background: linear-gradient(to bottom right, rgb(255, 255, 255),  rgb(220, 220, 220));
    background-attachment: fixed;
    background-size: cover;
    margin: 0;
    height: 100%;
  }

  #app {
    font-family: 'Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    margin: 0;
    height: 100%;
  }

  .errormsg {
    margin-top: 1em;
    margin-left: 35%;
    margin-right: 35%;
    text-align: center;
    width: 30%;

    padding: 0.4em;
    margin-top: 0.8em;

    background-color: #de141b;
    color: white;
    border: 2.5px solid white;
    }
</style>
