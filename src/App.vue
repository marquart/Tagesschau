<template>
  <div id="app">

    <h1><img src="favicon.ico" alt="Tagesschau-Explorer Logo">  Tagesschau-Explorer</h1>

    <div class="explanation">
      <h4 class="infotoggle" @click="switchInfo">{{beschreibung}}</h4>
      <div v-show="showInfo">
        <p>Für die Visualisierung haben wir die seit Juni 2014 auf <a href="https://www.tagesschau.de/multimedia/sendung/" target="_blank">tagesschau.de</a> verfügbaren Untertitel aufbereitet. Aus den Untertitlen inkludierten wir in unsere Auswertung Inhaltswörter (d.h. Nomen, Adjektive, Adverbien und Vollverben), die</p>
        <ul style="margin-left:5%;text-align:left;">
          <li>länger als drei Zeichen sind (außer auf bekannte Abkürzungen wie UN, EU, IS etc.).</li>
          <li>keine Zahlen beinhalten.</li>
          <li>insgesamt mehr als drei mal genannt wurden.</li>
        </ul>
        <p>Einerseits kann man mit einer <a href="#keyworddensity">Darstellung von Wortdichten als Kurvengrafik</a> die Verwendung von Begriffen über die Zeit nachvollziehen und damit z.B. Schlüße auf die Themensetzungen ziehen, andererseits ist es durch <a href="#map">eine Karte</a> möglich, die außenpolitische Berichterstattung zu entdecken.</p>
        <p>Die Wortdichte zeigt den Anteil eines Wortes in einer Sammlung von Wörtern an, indem es die Anzahl des Wortes durch die Gesamtzahl von Wörtern in der Sammlung teilt. Für die Darstellung der Wortdichten in der Tagesschau über die Zeit haben wir die Wörter jeweils nach den Monaten gruppiert, in denen die Tagesschau ausgestrahl wurde.</p>
        <p>Um die Wortdichte eines Begriffes zu sehen, kannst du im <a href="#SearchBar">unteren Suchfeld</a> bis zu fünf Begriffe suchen, deren Wortdichten über die Zeit in einem Kurvendiagramm angezeigt werden oder du lässt dir jeweils 15 Begriffe anzeigen, die in einem Monat im Gegensatz zu allen anderen Monaten besonders hervorstechen.</p>
        <p>Für die <a href="#map">Karte</a> zur Analyse der außenpolitischen Berichterstattung der Tagesschau wurden die Untertitel mithilfe von Named Entity Recognition auf die Erwähnung von Staatennamen (außer Deutschland) untersucht. Die Karte zeigt, wie oft die jeweiligen Staaten pro Episode pro Monat oder im gesamten Zeitraum erwähnt wurden. In der Infobox unten rechts sind die Top 10 Kookkurenzen für den ausgewählten Staat im gewählten Zeitraum zu sehen.</p>
        <p>Unter der Karte findest du eine Kurvendiagramm, das die Entwicklung der Berichterstattung über die jeweiligen Staaten darstellt. Über einen Mausklick in den Plot können die Kookkurrenzen für den jeweiligen Monat in der Karte angezeigt werden. </p>
      </div>
    </div>
    <KeywordDensityPlot />
    <NamedEntitiesMap />
  </div>
</template>

<script>
// required from npm:
// npm install -D sass-loader@10.2.0 sass
// npm install d3

import KeywordDensityPlot from './components/KeywordDensityPlot.vue'
import NamedEntitiesMap from './components/NamedEntitiesMap.vue'

export default {
    name: 'App',
    components: {
      KeywordDensityPlot,
      NamedEntitiesMap,
    },

    data() {
      return {
        showInfo: false
        
      }
    },

    computed: {
      beschreibung() {
        if (this.showInfo) return "Info ▼";
        else return "Info ▶";
      }
    },

    methods: {
      switchInfo() {
        if (this.showInfo)this.showInfo = false;
        else this.showInfo = true;
      }
    }

}
</script>

<style lang="scss">
  //@import url('https://fonts.googleapis.com/css?family=Barlow');
  @import url('https://fonts.googleapis.com/css2?family=PT+Sans&display=swap');

  body, html {
    // background: linear-gradient(to bottom right, rgb(255, 255, 255),  rgb(220, 220, 220));
    background: linear-gradient(to bottom, rgb(1, 69, 150),  rgb(1, 30, 88) );
    // background: #011e58;
    color: #e9ebf0;
    background-attachment: fixed;
    background-size: cover;
    margin: 0;
    height: 100%;
  }

  #app {
    font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    margin: 0;
    height: 100%;
  }

  .explanation {
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    margin-bottom: 1em;
    padding: 0.3em 0;
    color: 'white';
    background: 'rgba(0,0,0,0)'; //linear-gradient(to bottom, #ffffff,  #e2e1dc );
  }

  p {
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    text-align: justify;
  }

  a {
    color: inherit;
    text-decoration: underline;
  }
  a:hover {
    text-decoration: none;
    font-weight: bold;
  }
  
  img {
    display: inline;
    transform: translate(0, 25%);
  }

  .infotoggle {
      margin-top: 0;
      margin-bottom: 0;
  }

  .infotoggle:hover {
    cursor: pointer;
  }

</style>
