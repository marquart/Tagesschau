<template>
    <div id="lineplot">
        <h3 v-if="activeState">{{activeState}}</h3>
        <h3 v-else>Staat auswählen</h3>
        <p> <br> </p>
    </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: 'LinePlot',
    props: {
        activeState: String,
        nerData: Array,
    },

watch: {
      activeState() {
          let state_data = this.nerData.find(key => key.state_name === this.activeState)
          let values = []
          for (const [key, value] of Object.entries(state_data)) {
            if (key.startsWith("count")) {
              values.push(value)
            }
          }
          values.shift()
          console.log(values)
      }
  }
}



</script>

<style scoped>
#map {
    margin:1px auto;
    }
</style> 