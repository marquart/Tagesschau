<template>
  <div id="app">
    <h1>Tagesschau</h1>
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
        
      }
    },

    mounted() {
    }, 

    methods: {

    },

    computed: {
      
    },

    destroyed() {

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

</style>
