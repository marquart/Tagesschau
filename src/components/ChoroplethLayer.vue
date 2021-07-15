<template>
  <div id="choropleth">
    <p v-if="gesamt"><b>Gesamt</b></p>
    <p v-else><b>{{dates[monthIndex]}}</b></p>
    <l-geo-json :key="start"
                :geojson="geojsonData.geojson" 
                :options="geojsonOptions" 
                ref="geolayer"
                :visible="start === true"></l-geo-json>
    <l-geo-json :key="monthIndex"
                :geojson="geojsonData.geojson" 
                :options="geojsonOptions" 
                ref="geolayer"
                :visible="monthIndex === monthIndex"></l-geo-json>
    <slot :currentItem="currentItem" 
          :unit="value.metric" 
          :min="min" 
          :max="max"
          ></slot>
  </div>
</template>
<script>

import {LGeoJson} from "vue2-leaflet"
import { getMin, getMax, normalizeValue, getColor, validNumber } from "../util"

function mouseover({ target }) {
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
  if (!item) {
    this.currentItem = { name: "", value: 0 }
    return
  }

  let tempItem = { name: item[this.titleKey], value: item[this.value.key] }
  if (this.extraValues) {
    let tempValues = []
    for (let x of this.extraValues) {
      tempValues.push({
        value: item[x.key],
        metric: x.metric
      })
    }
    tempItem = { ...tempItem, extraValues: tempValues }
  }
  this.currentItem = tempItem
}


function click({ target }) {
  
  let geojsonItem = target.feature.properties
  let item2 = this.geojsonData.data.find(
    x => x[this.idKey] == geojsonItem[this.geojsonIdKey]
  ) 
  if (item2) {
    this.activeState = item2[this.titleKey]
  } 

}

function mouseout({ target }) {
  target.setStyle({
    weight: this.strokeWidth,
    color: this.colorScale[0],
  })
  this.currentItem = { name: "", value: 0 }
}


export default {
  props: {
    monthIndex: String,
    start: true,
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
      currentItem: { name: "", value: 0 },
      activeState: "",
      fillOpacity: 0.75,
      dates: {},
      gesamt : true,
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
            mouseover: mouseover.bind(this),
            mouseout: mouseout.bind(this),
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
      
      /*
      monthIndex() {
          this.month = this.monthIndex
          console.log("Click");
      } */
  },

  computed: {
    min() {
      return (0)
    },
    max() {
      if (this.monthIndex == 0) {
        return (150)
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
    },


    fillDates() {
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
  },

    mounted() {
    console.log(this.gesamt);
    if (this.$parent._isMounted) {
      this.deferredMountedTo(this.$parent.mapObject)
    }
    this.fillDates();
    this.gesamt = false;

  },
}
</script>

<style>
#choropleth {
    height: 90%;
    width: 90%; 
    margin:0px auto;
    font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: white;
    margin-top: 1%;
    margin-left: 3%;
    font-size:18px;
    }
</style>