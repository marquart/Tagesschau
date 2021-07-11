<template>
    <div id="slider">
        <vue-slider 
        v-model="value"
        :data="dates" 
        v-bind = "options"/>
        <p> <br> </p>
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
      dates: {'0': 'Jun 2014',
                '1': 'Jul 2014',
                '2': 'Aug 2014',
                '3': 'Sep 2014',
                '4': 'Okt 2014',
                '5': 'Nov 2014',
                '6': 'Dez 2014',
                '7': 'Jan 2015',
                '8': 'Feb 2015',
                '9': 'Mar 2015',
                '10': 'Apr 2015',
                '11': 'Mai 2015',
                '12': 'Jun 2015',
                '13': 'Jul 2015',
                '14': 'Aug 2015',
                '15': 'Sep 2015',
                '16': 'Okt 2015',
                '17': 'Nov 2015',
                '18': 'Dez 2015',
                '19': 'Jan 2016',
                '20': 'Feb 2016',
                '21': 'Mar 2016',
                '22': 'Apr 2016',
                '23': 'Mai 2016',
                '24': 'Jun 2016',
                '25': 'Jul 2016',
                '26': 'Aug 2016',
                '27': 'Sep 2016',
                '28': 'Okt 2016',
                '29': 'Nov 2016',
                '30': 'Dez 2016',
                '31': 'Jan 2017',
                '32': 'Feb 2017',
                '33': 'Mar 2017',
                '34': 'Apr 2017',
                '35': 'Mai 2017',
                '36': 'Jun 2017',
                '37': 'Jul 2017',
                '38': 'Aug 2017',
                '39': 'Sep 2017',
                '40': 'Okt 2017',
                '41': 'Nov 2017',
                '42': 'Dez 2017',
                '43': 'Jan 2018',
                '44': 'Feb 2018',
                '45': 'Mar 2018',
                '46': 'Apr 2018',
                '47': 'Mai 2018',
                '48': 'Jun 2018',
                '49': 'Jul 2018',
                '50': 'Aug 2018',
                '51': 'Sep 2018',
                '52': 'Okt 2018',
                '53': 'Nov 2018',
                '54': 'Dez 2018',
                '55': 'Jan 2019',
                '56': 'Feb 2019',
                '57': 'Mar 2019',
                '58': 'Apr 2019',
                '59': 'Mai 2019',
                '60': 'Jun 2019',
                '61': 'Jul 2019',
                '62': 'Aug 2019',
                '63': 'Sep 2019',
                '64': 'Okt 2019',
                '65': 'Nov 2019',
                '66': 'Dez 2019',
                '67': 'Jan 2020',
                '68': 'Feb 2020',
                '69': 'Mar 2020',
                '70': 'Apr 2020',
                '71': 'Mai 2020',
                '72': 'Jun 2020',
                '73': 'Jul 2020',
                '74': 'Aug 2020',
                '75': 'Sep 2020',
                '76': 'Okt 2020',
                '77': 'Nov 2020',
                '78': 'Dez 2020',
                '79': 'Jan 2021',
                '80': 'Feb 2021',
                '81': 'Mar 2021',
                '82': 'Apr 2021',
                '83': 'Mai 2021',
                '84': 'Gesamt'}
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