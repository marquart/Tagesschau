<template>
  <div id="app">

    <h1><img src="favicon.ico" alt="Tagesschau-Explorer Logo">  Tagesschau-Explorer</h1>

    <div class="explanation" @click="switchInfo">
      <h4 class="infotoggle">{{beschreibung}}</h4>
      <p v-show="showInfo">Für die Visualisierung haben wir die seit Juni 2014 auf <a href="https://www.tagesschau.de/multimedia/sendung/" target="_blank">tagesschau.de</a> verfügbaren Untertitel aufbereitet. Einerseits kann man mit einer Darstellung von Wortdichten als Kurvengrafik die Verwendung von Begriffen über die Zeit nachvollziehen und damit z.B. Schlüße auf die Themensetzungen ziehen, andererseits ist es durch eine Karte möglich, die außenpolitische Berichterstattung zu entdecken.</p>
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
        if (this.showInfo) this.showInfo = false;
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
    background: linear-gradient(to bottom, #ffffff,  #e2e1dc );
    color: black;
    padding: 0.3em 0;
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
