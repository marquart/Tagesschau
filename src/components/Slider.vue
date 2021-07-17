<template>
    <div id="slider">
        <vue-slider ref="slider" v-model="value" :data="dates" v-bind = "options"/>
    </div>
    
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

export default {
  components: {
    VueSlider
  },
  props: {
    monthIndex : String,
  },
  data () {
    return {
      value: 0,
      dates: {},
      options: {
        dotSize: 20,
        width: 'auto',
        height: 5,
        direction: 'ltr',
        dataLabel: 'label',
        dataValue: 'value',
        interval: 1,
        clickable: true,
        duration: 0.5,
        tooltip: 'always',
        tooltipFormatter: void 0,
        useKeyboard: true,
        dragOnClick: true,
        enableCross: true,
        fixed: true,
        order: true,
        marks: false,
        hideLabel: true,
      }
    }
  },
  
  created() {
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

  watch: {
    value() {
        this.$emit('newMonth', this.value);
    },
    monthIndex(){
      this.$refs.slider.setValue(this.monthIndex);
    }
  }
}
</script>

<style scoped>
#slider {
    margin-left: 1%;
    width: 98%; 
    }
</style>