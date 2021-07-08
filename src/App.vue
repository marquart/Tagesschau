<template>
  <div id="app">
    <h1>Tagesschau</h1>
    <KeywordDensityPlot />
  </div>
</template>

<script>
// required from npm:
// npm install -D sass-loader@10.2.0 sass
// npm install d3

import KeywordDensityPlot from './components/KeywordDensityPlot.vue'

export default {
    name: 'App',
    components: {
      KeywordDensityPlot,
    },

    data() {
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

</style>
