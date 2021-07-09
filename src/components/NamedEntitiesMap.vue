<template>
  <div id="map">
    <h2>Karte</h2>
    <l-map 
    :center="[38, 13]" 
    :zoom="2"
    :minZoom="2"
    :maxZoom="5" 
    :options="mapOptions"
    style="height: 800px;">
      <l-choropleth-layer 
      :data="nerData" 
      titleKey="state_name" 
      idKey="state_id" 
      :value="value" 
      :extraValues="extraValues" 
      geojsonIdKey="NAME" 
      :geojson="worldGeojson" 
      :colorScale="colorScale">
        <template slot-scope="props">
          <l-info-control 
          :item="props.currentItem" 
          :unit="props.unit" 
          title=" " 
          placeholder="Staat auswählen"/>
          <l-reference-chart 
          title="Erwähnung pro Episode" 
          :colorScale="colorScale" 
          :min="props.min" 
          :max="props.max" 
          position="topright"/>
        </template>
      </l-choropleth-layer>
    </l-map>
    <br><br>
  <Slider/>
  </div>
</template>

<script>
import { InfoControl, ReferenceChart, ChoroplethLayer } from 'vue-choropleth'
import worldGeojson from '../../public/world.geo.json'
import { nerData } from '../../public/ner'
import {LMap} from 'vue2-leaflet';
import Slider from './Slider.vue'

export default {
  name: "NamedEntitiesMap",
  components: { 
    LMap,
    'l-info-control': InfoControl, 
    'l-reference-chart': ReferenceChart, 
    'l-choropleth-layer': ChoroplethLayer,
    Slider
  },
  data() {
    return {
      nerData,
      worldGeojson,
      colorScale: ["dbf0ff", "#002b80"],
      value: {
        key: "count",
        metric: " == Summe aller Erwähnung pro Folge"
      },
      extraValues: [{
        key: "coocc",
        metric: ""
      }],
      mapOptions: {
        attributionControl: false,
        styles: {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [{color: '#17263c'}]
        },
      },
      currentStrokeColor: '3d3213'
    }
  },
}
</script>
<style scoped>
#map {
    height: 90%;
    width: 90%; 
    margin:0px auto;
    }
</style>