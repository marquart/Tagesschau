<template>
  <div id="map">
    <h2>Karte zur außenpolitischen Berichterstattung</h2>
    <div style="margin-bottom:2em;"></div>
    <Slider @newMonth="updateMap"/>
    <l-map 
    :center="center" 
    :zoom="2"
    :minZoom="2"
    :maxZoom="5" 
    :options="mapOptions"
    style="height: 700px; 
            background-color: #011e58;
            color:#000000;
            border-color: black;
            border-width: 5px;
            border-style: solid">
      <l-choropleth-layer 
      @activeState = "updateActiveState"
      :data="nerData" 
      titleKey="state_name" 
      idKey="state_id" 
      :value="value" 
      :extraValues="extraValues" 
      geojsonIdKey="NAME" 
      :geojson="worldGeojson" 
      :colorScale="colorScale"
      :strokeWidth="1"
      strokeColor="ffffff"
      :currentStrokeWidth="currentStrokeWidth"
      currentStrokeColor = "f5d81b"
      :monthIndex="monthIndex">
        <template slot-scope="props">
          <l-info-control 
          :item="props.currentItem" 
          :unit="props.unit" 
          title=" " 
          placeholder="Staat auswählen"
          :monthIndex="monthIndex"/>
          <l-reference-chart 
          title="Erwähnung pro Folge" 
          :colorScale="colorScale" 
          :min="props.min" 
          :max="props.max" 
          position="topright"
          :monthIndex="monthIndex"/> 
        </template>
      </l-choropleth-layer>
    </l-map>
  <LinePlot :activeState="activeState" :nerData="nerData"/>
  </div>
</template>

<script>
// import { InfoControl, ReferenceChart, ChoroplethLayer } from '../../vue-choropleth'
// import { InfoControl, ReferenceChart, ChoroplethLayer } from 'vue-choropleth'
import InfoControl from './InfoControl'
import ReferenceChart from './ReferenceChart'
import ChoroplethLayer from './ChoroplethLayer'
import worldGeojson from '../../public/world.geo.json'
import { nerData } from '../../public/ner'
import {LMap} from 'vue2-leaflet'
import Slider from './Slider.vue'
import LinePlot from './LinePlot.vue'

export default {
  name: "NamedEntitiesMap",
  components: { 
    LMap,
    'l-info-control': InfoControl, 
    'l-reference-chart': ReferenceChart, 
    'l-choropleth-layer': ChoroplethLayer,
    Slider,
    LinePlot
  },
  data() {
    return {
      nerData,
      worldGeojson,
      colorScale: ["#f2f8fc", "#00256e"],
      center: [38, 13],
      monthIndex: "0",
      currentStrokeWidth: 3, 
      activeState: "",
      value: {
        key: "count",
        metric: "<br>(Erwähnung pro Folge gesamt)<br><u>Kookkurenzen:</u>"
      },
      extraValues: [{
        key: "coocc",
        metric: ""
      }],
      mapOptions: {
        attributionControl: false,
      },
    }
  },


  mounted() {
      //this.fetchData(); // Um die Daten asynchron von einem Backend zu holen -> rendert die Seite für den Benutzer schneller
      // this.loadData(); // Lädt die Daten aus JS-Skript -> -> rendert die Seite für den Benutzer langsamer, aber kein Backend nötig
    },

  methods: {

    updateMap(monthIndex) {
      if (monthIndex == 0) {
        this.value.key = 'count';
        this.value.metric = '<br>(Erwähnung pro Folge gesamt)<br><u>Kookkurenzen:</u>';
        this.extraValues[0].key = 'coocc';
        this.extraValues[0].metric = '';
      } else {
        this.value.key = 'count' + monthIndex;
        this.value.metric = '<br>(Erwähnung pro Folge)<br><u>Kookkurenzen:</u>';
        this.extraValues[0].key = 'coocc' + monthIndex;
        this.extraValues[0].metric = '';
      }
      this.monthIndex = monthIndex
    },

    updateActiveState(activeState){
      this.activeState = activeState
    }
 }
} 

</script> 
<style> 
#map {
    height: 90%;
    width: 90%; 
    margin:0px auto;
    }
</style>