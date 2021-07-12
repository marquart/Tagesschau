<template>
    <div id="slider">
        <vue-slider 
        v-model="value"
        :data="dates" 
        v-bind = "options"/>
    </div>
</template>

<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

export default {
  components: {
    VueSlider
  },
  data () {
    return {
      value: 0,
      options: {
        dotSize: 20,
        width: 'auto',
        height: 5,
        contained: true,
        direction: 'ltr',
        dataLabel: 'label',
        dataValue: 'value',
        min: 0,
        max: 84,
        interval: 1,
        disabled: false,
        clickable: true,
        duration: 0.5,
        adsorb: false,
        lazy: false,
        tooltip: 'always',
        tooltipPlacement: 'top',
        tooltipFormatter: void 0,
        useKeyboard: true,
        keydownHook: null,
        dragOnClick: true,
        enableCross: true,
        fixed: true,
        minRange: void 0,
        maxRange: void 0,
        order: true,
        marks: false,
        included: true,
        hideLabel: true,
        dotOptions: void 0,
        dotAttrs: void 0,
        process: true,
        dotStyle: void 0,
        railStyle: void 0,
        processStyle: void 0,
        tooltipStyle: void 0,
        stepStyle: void 0,
        stepActiveStyle: void 0,
        labelStyle: void 0,
        labelActiveStyle: void 0,
      },
      dates: {'0': 'Gesamt',
              '1': 'Jun 2014',
              '2': 'Jul 2014',
              '3': 'Aug 2014',
              '4': 'Sep 2014',
              '5': 'Okt 2014',
              '6': 'Nov 2014',
              '7': 'Dez 2014',
              '8': 'Jan 2015',
              '9': 'Feb 2015',
              '10': 'Mar 2015',
              '11': 'Apr 2015',
              '12': 'Mai 2015',
              '13': 'Jun 2015',
              '14': 'Jul 2015',
              '15': 'Aug 2015',
              '16': 'Sep 2015',
              '17': 'Okt 2015',
              '18': 'Nov 2015',
              '19': 'Dez 2015',
              '20': 'Jan 2016',
              '21': 'Feb 2016',
              '22': 'Mar 2016',
              '23': 'Apr 2016',
              '24': 'Mai 2016',
              '25': 'Jun 2016',
              '26': 'Jul 2016',
              '27': 'Aug 2016',
              '28': 'Sep 2016',
              '29': 'Okt 2016',
              '30': 'Nov 2016',
              '31': 'Dez 2016',
              '32': 'Jan 2017',
              '33': 'Feb 2017',
              '34': 'Mar 2017',
              '35': 'Apr 2017',
              '36': 'Mai 2017',
              '37': 'Jun 2017',
              '38': 'Jul 2017',
              '39': 'Aug 2017',
              '40': 'Sep 2017',
              '41': 'Okt 2017',
              '42': 'Nov 2017',
              '43': 'Dez 2017',
              '44': 'Jan 2018',
              '45': 'Feb 2018',
              '46': 'Mar 2018',
              '47': 'Apr 2018',
              '48': 'Mai 2018',
              '49': 'Jun 2018',
              '50': 'Jul 2018',
              '51': 'Aug 2018',
              '52': 'Sep 2018',
              '53': 'Okt 2018',
              '54': 'Nov 2018',
              '55': 'Dez 2018',
              '56': 'Jan 2019',
              '57': 'Feb 2019',
              '58': 'Mar 2019',
              '59': 'Apr 2019',
              '60': 'Mai 2019',
              '61': 'Jun 2019',
              '62': 'Jul 2019',
              '63': 'Aug 2019',
              '64': 'Sep 2019',
              '65': 'Okt 2019',
              '66': 'Nov 2019',
              '67': 'Dez 2019',
              '68': 'Jan 2020',
              '69': 'Feb 2020',
              '70': 'Mar 2020',
              '71': 'Apr 2020',
              '72': 'Mai 2020',
              '73': 'Jun 2020',
              '74': 'Jul 2020',
              '75': 'Aug 2020',
              '76': 'Sep 2020',
              '77': 'Okt 2020',
              '78': 'Nov 2020',
              '79': 'Dez 2020',
              '80': 'Jan 2021',
              '81': 'Feb 2021',
              '82': 'Mar 2021',
              '83': 'Apr 2021',
              '84': 'Mai 2021'
              }
      }
  },

  watch: {
      value() {
          this.$emit('newMonth', this.value);
      }
  }
}
</script>

<style scoped>
#map {
    margin:1px auto;
    }
</style>