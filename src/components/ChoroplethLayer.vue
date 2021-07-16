<template>
  <div id="choroplethLayer">
    <l-geo-json :key="monthIndex" :geojson="geojsonData.geojson" :options="geojsonOptions" ref="geolayer" :visible="monthIndex === monthIndex"></l-geo-json>
    <slot :unit="value.metric" :min="min" :max="max" ></slot>
  </div>
</template>
<script>

import {LGeoJson} from "vue2-leaflet"
import { getMin, getMax, normalizeValue, getColor, validNumber } from "../util"


function click({target}) {

  if (this.oldtarget) {
    this.oldtarget.setStyle({
      weight: this.strokeWidth,
      color: this.colorScale[0],
    })
  }
  this.oldtarget = target;

  target.setStyle({
    weight: this.currentStrokeWidth,
    color: `#${this.currentStrokeColor}`,
    dashArray: "" 
  })
  
  if (!L.Browser.ie && !L.Browser.opera) {
    target.bringToFront()
  } 

  let geojsonItem = target.feature.properties
  let item = this.geojsonData.data.find(
    x => x[this.idKey] == geojsonItem[this.geojsonIdKey]
  )
  if (item){
    this.activeState = item[this.titleKey]
  }
}

export default {
  props: {
    monthIndex: String,
    plotposition: Number,
    geojson: Object,
    data: Array,
    center: Array,
    colorScale: Array,
    titleKey: String,
    idKey: String,
    value: Object,
    extraValues: Array,
    geojsonIdKey: String,
    mapStyle: Object,
    zoom: Number,
    mapOptions: Object,
    strokeColor: {type: String, default: 'fff'},
    currentStrokeColor: {type: String, default:'666'},
    strokeWidth: {type: Number, default: 2},
    currentStrokeWidth: {type: Number, default: 5}
  },
  data() {
    return {
      activeState: "",
      fillOpacity: 0.75,
      oldtarget: false,
      geojsonOptions: {
        style: feature => {
          let itemGeoJSONID = feature.properties[this.geojsonIdKey]
          let color = "NONE"
          const {data} = this.geojsonData

          let item = data.find(x => x[this.idKey] == itemGeoJSONID)
          if (!item) {
            return {
              color: this.colorScale[0],
              weight: this.strokeWidth,
              fillOpacity: this.fillOpacity
            }
          }
          let valueParam = Number(item[this.value.key]) + 0.00001
          if (!validNumber(valueParam)) {
            return {
              color: this.colorScale[0],
              weight: this.strokeWidth,
              fillOpacity: this.fillOpacity
            }
          }
          
          if (item[this.idKey] === "Germany"){
            return {
            color: "#ffffff",
            weight: this.strokeWidth,
            fillOpacity: this.fillOpacity
            }
          }

          const { min, max } = this
 
          return {
            weight: this.strokeWidth,
            opacity: 1,
            color: `#${this.strokeColor}`,
            dashArray: "1",
            fillColor: getColor(valueParam, this.colorScale, min, max),
            fillOpacity: this.fillOpacity
          }
        },

        onEachFeature: (feature, layer) => {
          layer.on({
            //mouseover: mouseover.bind(this),
            //mouseout: mouseout.bind(this),
            click: click.bind(this)
          })
        }
      }
    }
  },

  watch: {
    activeState() {
        this.$emit('activeState', this.activeState);
    },
    plotposition() {
      console.log(this.plotposition);
      //this.monthIndex = this.poltposition;
    }
  },

  computed: {
    min() {
      return (0)
    },
    max() {
      if (this.monthIndex == 0) {
        return (200)
      } else {
        return (3)
        //return getMax(this.geojsonData.data, this.value.key)
      }
    },
    geojsonData() {
      return {geojson: {...this.geojson}, data: this.data};
    }
  },

  components: {
    LGeoJson
  },

  methods: {
    deferredMountedTo(parent) {
      this.parent = parent
      for (var i = 0; i < this.$children.length; i++) {
        if (typeof this.$children[i].deferredMountedTo === "function") {
          this.$children[i].deferredMountedTo(parent)
        }
      }
      this.monthIndex = '0'
    }
  },

  mounted() {
  if (this.$parent._isMounted) {
    this.deferredMountedTo(this.$parent.mapObject)
    }
  }
}
</script>


<style>
#choroplethLayer {
    font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: right;
    color: white;
    margin-top: 34%;
    margin-right: 3%;
    font-size:18px;
    }
</style>