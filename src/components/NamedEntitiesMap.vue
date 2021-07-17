<template>
  <div id="map">
    <h2>Karte zur außenpolitischen Berichterstattung</h2>
    <Slider @newMonth="updateMap" :monthIndex="monthIndex"/>
    <l-map 
    :center="center" :zoom="2" :minZoom="1" :maxZoom="5" :options="mapOptions"
    style="height: 600px; background-color: #011e58; color:#000000; border-color: black; border-width: 5px; border-style: solid; font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale">
      <l-control-zoom position="bottomright"</l-control-zoom>
      <p v-if="dates" style="margin-top: 560px; margin-right: 15px; text-align: right; font-size:18px; color:#fff"><b>{{dates[monthIndex]}}</b></p>
      <p v-else style="margin-top: 560px; margin-right: 15px; text-align: right; font-size:18px; color:#fff"><b>Gesamt</b></p>
      <l-choropleth-layer @activeState = "updateActiveState" :data="nerData" titleKey="state_name" idKey="state_id" :value="value" :extraValues="extraValues" :monthIndex="monthIndex"
        geojsonIdKey="NAME" :geojson="worldGeojson"
        :colorScale="colorScale" :strokeWidth="1" strokeColor="#ffffff" :currentStrokeWidth="currentStrokeWidth" currentStrokeColor = "#c97412">
        <template slot-scope="props">
          <l-info-control :item="props.currentItem" :unit="props.unit" title=" " placeholder="Staat auswählen" :monthIndex="monthIndex" :nerData="nerData" :activeState="activeState"/>
          <l-reference-chart title="Erwähnung pro Folge" :colorScale="colorScale" :min="props.min" :max="props.max" position="topright"/> 
        </template>
      </l-choropleth-layer>
    </l-map>
  <LinePlot @plotPosition="sendPlotPosition":activeState="activeState" :nerData="nerData"/>
  </div>
</template>

<script>
import InfoControl from './InfoControl'
import ReferenceChart from './ReferenceChart'
import ChoroplethLayer from './ChoroplethLayer'
import worldGeojson from '../../public/world.geo.json'
import { nerData } from '../../public/ner'
import {LMap, LControlZoom} from 'vue2-leaflet'
import Slider from './Slider.vue'
import LinePlot from './LinePlot.vue'

export default {
  name: "NamedEntitiesMap",
  components: { 
    LMap,
    LControlZoom,
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
      dates: {},
      monthIndex: "0",
      activeState: "",
      value: {
        key: "count",
        metric: "<br><u>Kookkurenzen:</u>"
      },
      extraValues: [{
        key: "coocc",
        metric: ""
      }],
      colorScale: ["#f2f8fc", "#00256e"],
      //center: [38, 13],
      center: [42, 20],
      currentStrokeWidth: 3, 
      mapOptions: {
        attributionControl: false,
        zoomControl: false,
        zoomSnap: 0.4,
      },
    }
  },

  methods: {

    updateMap(monthIndex) {
      if (monthIndex == 0) {
        this.value.key = 'count';
        this.extraValues[0].key = 'coocc';
      } else {
        this.value.key = 'count' + monthIndex;
        this.extraValues[0].key = 'coocc' + monthIndex;
      }
      this.monthIndex = monthIndex
    },
    sendPlotPosition(plotpos) {
      this.monthIndex = String(plotpos+1);
      this.updateMap(this.monthIndex);
    },

    updateActiveState(activeState){
      this.activeState = activeState
    },

  },

  computed: {
  },


  created(){
    this.gesamt = false;
    let year = 2014;
    let month = 4;
    let months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"];
    for (var i = 0; i < 85; i++){
      let out = "";
      month += 1;
      if (month > 12){
        month = 1;
        year += 1;
      }
      if (i == 0){
        out = "Gesamt";
      } else {
        out = months[month-1] + " " + new String(year);
      }
      let j = new String(i);
      this.dates[j] = out;
      }
  },

}

</script> 
<style> 
#map {
    height: 90%;
    width: 81%;
    margin-left: 55%;
    margin-right: 5%;
    margin:0px auto;
    font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: inherit;
    margin-top: 5em;
    
    }
</style>