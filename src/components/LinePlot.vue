<template>
    <div id="linePlot">
        <p v-if="activeState"><b>{{activeState}}</b></p>
        <p v-else><b>Staat auswählen</b></p>
        <div id="showPlot"/>
        <div id="hovertext" :style="hoverTextStyle">
            <p class="date">{{dates_array[mouseindex]}}:</p>
            <p class="lineinfo">{{values[mouseindex]}}</p>
        </div>
    </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: 'LinePlot',
  props: {
      activeState: String,
      nerData: Array
  },
  
  data() {
    return {
      dates: {},
      dates_array: [],
      values: [],
      svg: null,
      margin: window.innerWidth*0.1,

      figureWidth: 0,
      figureHeight: 0,

      xScale: null,
      yScale: null,

      yaxis: null,
      xaxis: null,
      xticks: [],
      xticklabels: [],

      linegenerator: null,

      listeningRect: null,
      hoverline: null,

      mouseindex: 0,
      hoverTextStyle: {
          display: 'none',
          left: 0,
          top: 0
      }
    }
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
      this.values = values;
      this.draw()
    }

  },

  methods: {
    
    draw() {
      this.svg.selectAll("g.axis").remove()
      this.svg.selectAll("path.line").remove()
      
      this.xScale.domain([0, this.dates_array.length]);
      this.yScale.domain([0, 8.5]);
      //this.yScale.domain([0, d3.max(this.selectedNumbers, l => d3.max(l, n => n))]);

      this.yaxis = d3.axisLeft().scale(this.yScale); 
      this.xaxis = d3.axisBottom().scale(this.xScale)
                      .tickValues(this.getTickValues())
                      .tickFormat(i => this.dates_array[i]);

      this.svg.append("g")
          .attr("class", "axis")
          .attr("transform", "translate(0," + this.figureHeight + ")")
          .call(this.xaxis);

      this.svg.append("g")
          .attr("class", "axis")
          .call(this.yaxis);

      this.svg.append("path")
          .datum(this.values) // 10. Binds data to the line 
          .attr("class", "line") // Assign a class for styling 
          .attr("d", this.linegenerator) // 11. Calls the line generator

      this.listeningRect.raise();
    },

    getX(p, index) {
        return this.xScale(index);
    },
    getY(p) {
        return this.yScale(p);
    },
    formatDate(d) {
        return  d3.timeFormat("%b %Y")(d);
    },

    onMouseMove(event) {
        let mousePosition = d3.pointer(event),
            x = this.xScale.invert(mousePosition[0]),
            i = Math.round(x);
        this.hoverline
            .attr("transform", "translate(" + this.xScale(i) + ",0)")
            .style("opacity", 1);

        this.mouseindex = i;
        if (i>77) this.hoverTextStyle['left'] = (event.pageX-100) + 'px';
        else this.hoverTextStyle['left'] = (event.pageX+20) + 'px';
        this.hoverTextStyle['top'] = event.pageY + "px";
        this.hoverTextStyle['display'] = 'block';
    },

    onMouseLeave() {
        this.hoverline.style("opacity", 0);
        this.hoverTextStyle['display'] = 'none';
    },

    around(n) {
        return d3.format(".2f")(n);
    },

    getTickValues() {
      
      let month = 6;
      let result = [];
      for (let i = 0; i < this.dates_array.length; i++){
          if (!(month % 6)) result.push(i);
          month++;
      }
      this.xticks = result;
      return result;

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
          this.dates_array.push(out);
        }
        let j = new String(i);
        this.dates[j] = out;
      }
    }
  },

  mounted() {
    
    this.fillDates();

    this.figureWidth = window.innerWidth - this.margin - 8;
    this.figureHeight = window.innerHeight  - 4*this.margin;
    if (this.figureHeight<0) this.figureHeight = 0;

    this.svg = d3
      .select("#showPlot")
      .append("svg")
      .attr("width", this.figureWidth)
      .attr("height", this.figureHeight+this.margin/3)
      .append('g')
      .attr("transform", "translate(" + this.margin/6 + ",0)");

    this.yScale = d3.scaleLinear().range([this.figureHeight, 0]);
    this.xScale = d3.scaleLinear().range([0, this.figureWidth]);

    this.linegenerator = d3.line()
        .x(this.getX) // set the x values for the line generator
        .y(this.getY) // set the y values for the line generator 
        .curve(d3.curveMonotoneX)//.curve(d3.curveCatmullRom.alpha(0.5)) // apply smoothing to the line
        
    this.listeningRect = this.svg
        .append("rect")
        .attr("class", "listening-rect")
        .attr("width", this.figureWidth)
        .attr("height", this.figureHeight)
        .on("mousemove", this.onMouseMove)
        .on("mouseleave", this.onMouseLeave);

    let hoverlinegroup = this.svg.append("g").attr("class", "hoverline");

    this.hoverline =  hoverlinegroup
                      .append("line")
                      .attr("x1", 0).attr("x2", 0)
                      .attr("y1", 0).attr("y2", this.figureHeight)
                      .style("opacity", 0);
    this.getTickValues();
  },
}

</script>

<style>

#linePlot{

  font-family: 'PT Sans','Barlow', Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#showPlot{
  padding-top: 0
}

.axis {
        font-family: inherit;
        font-size: inherit;
    }
.line {
      stroke-width: 3;
      fill: none;
      stroke: white;
    }
.lineinfo {
      padding: 0.05em;
      margin-top:1px;
      margin-bottom:0;
      color: black;
  }

</style> 