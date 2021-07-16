<template>
  <div id="keyworddensity">
    <h2>Kurvengrafik zur Wortdichte</h2>
    <div class="explanation" @click="switchInfo">
      <h4 class="infotoggle">{{beschreibung}}</h4>
      <div v-show="showInfo">
        <p>Die Wortdichte zeigt den Anteil eines Wortes in einer Sammlung von Wörtern an, indem es die Anzahl des Wortes durch die Gesamtzahl von Wörtern in der Sammlung teilt. Für die Darstellung der Wortdichten in der Tagesschau über die Zeit haben wir zwei Vereinfachungen vorgenommen: zum einen haben wir versucht, nur Inhaltswörter einzubeziehen, d.h. Nomen, Adjektive, Adverbien und Vollverben. Zum anderen haben wir die Tagesschauen nach den Monaten gruppiert, in denen sie jeweils gesendet wurden.</p>
        <p>Um die Wortdichte eines Begriffes zu sehen, kannst du im unteren Suchfeld bis zu fünf Begriffe suchen, deren Wortdichten über die Zeit in einem Kurvendiagramm angezeigt werden.</p>
      </div>
    </div>
    <SearchBar :words="words"  @add="addWord"/>
    <div v-if="showerror" class="errormsg" @click="hideError">{{errorstring}}</div>
    <Selection :words="selectedWords" :colors="colors" @delete="deleteWordFromIndex"/>
    <Canvas :selectedNumbers="selectedNumbers" :colors="colors" :dates="dates"/>
  </div>
</template>

<script>

import SearchBar from './SearchBar.vue'
import Canvas from './Canvas.vue'
import Selection from './Selection.vue'
import densities from '../../public/table.json'

export default {
    name: 'KeywordDensityPlot',
    components: {
      SearchBar,
      Selection,
      Canvas
    },

    data() {
      return {
        showInfo: false,
        colors : ['#00ced1','#ffa500','#0ac40a', '#911eb4', '#ff1493'], //['rgb(146,255,183)','rgb(249,136,255)','rgb(178,210,255)','rgb(255,124,181)','rgb(141,255,255)'], //["#9affc2","#9350a1","#697cd4","#ba496b","#53b3b6"],
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
      //this.fetchData(); // Um die Daten asynchron von einem Backend zu holen -> rendert die Seite für den Benutzer schneller
      this.loadData(); // Lädt die Daten aus JS-Skript -> -> rendert die Seite für den Benutzer langsamer, aber kein Backend nötig
    }, 

    methods: {


      /*async fetchData() {
        // Holt die Daten per HTTP von einem Backend
        let result = await fetch("table.json")
          .then(response => response.json())
          .then(data => this.numbers = data);

        this.words = Object.keys(this.numbers);

        this.fillDates();
        return result;
      },*/

      loadData() {
        // Lädt die Daten direkt
        this.numbers = densities;
        this.words = Object.keys(this.numbers);
        this.fillDates();
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

      switchInfo() {
        if (this.showInfo) this.showInfo = false;
        else this.showInfo = true;
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
      beschreibung() {
        if (this.showInfo) return "Info ▼";
        else return "Info ▶";
      }
      
    },

    destroyed() {

    }

}
</script>

<style>


  #keyworddensity {
    background: inherit;
    background-attachment: inherit;
    background-size: inherit;
    margin: inherit;


    font-family: inherit;
    -webkit-font-smoothing: inherit;
    -moz-osx-font-smoothing: inherit;
    text-align: inherit;
    margin: inherit;

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


  .explanation>p {

  }
</style>
