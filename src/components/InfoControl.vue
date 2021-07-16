<template>
  <div id="infoControl"/>
</template>

<script>
export default {
  props: {
    monthIndex: String,
    nerData: Array,
    activeState: "",
    unit: String,
    placeholder: {
      type: String,
      default: ""
    },
    title: String,
    position: {
      type: String,
      default: "bottomleft"
    }
  },

  mounted() {
    const { unit, title, placeholder, position } = this

    this.mapObject = L.control({
      position: position
    })

    this.mapObject.onAdd = function(map) {
      this._div = L.DomUtil.create("div", "info") // create a div with a class "info"
      this.update({ name: "", value: 0, unit, placeholder, title })
      return this._div
    }

    this.mapObject.update = function({
      name,
      value,
      extraValues = undefined,
      unit,
      title,
      placeholder
    }) {
      if (name.length > 0) {
        this._div.innerHTML = `<h4> ${title} </h4>
                    <b> ${name} </b><br /> ${value} ${unit}`
        if (extraValues) {
          for (let x of extraValues) {
            this._div.innerHTML =
              this._div.innerHTML + `<br /> ${x.value} ${x.metric}`
          }
        }
      } else {
        this._div.innerHTML = `<h4> ${title} </h4> <b> ${placeholder} </b>`
      }
    }

    if (this.$parent._isMounted) {
      this.deferredMountedTo(this.$parent.mapObject)
    }
  },

  methods: {
    deferredMountedTo(parent) {
      this.parent = parent
      this.mapObject.addTo(parent)
    },

    updateinfoControl(){
      if (!this.activeState) return;
      let state_data = this.nerData.find(key => key.state_name === this.activeState)
      let count = "count";
      let coocc = "coocc";
      if (this.monthIndex != 0){
        count = "count" + new String(this.monthIndex);
        coocc = "coocc" + new String(this.monthIndex);
      }
      this.mapObject.update({
        extraValues: [{
          value: state_data[coocc],
          metric: ""
        }],
        name: this.activeState,
        value: state_data[count],
        unit: this.unit,
        title: this.title,
        placeholder: this.placeholder
      })
    }
  },

  watch: {

    monthIndex() {
      this.updateinfoControl()
    },
    activeState(){
      this.updateinfoControl()
    }
  },

  beforeDestroy() {
    if (this.parent) {
      this.parent.removeControl(this.mapObject)
    }
  }
}
</script>

<style>
.info {

  font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding: 6px 8px;
  font: 18px/20px ;
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.info h4 {
  margin: 0 0 5px;
  color: #777;
}
</style>
