<template>
    <div>
        <h2>{{generateArc}}</h2>
        <div v-show="datapresent" id="canvas">

        </div>
    </div>
</template>

<script>
import * as d3 from "d3";

export default {
    name: 'Canvas',
    props: {
        words: Array,
        numberstoshow: Array
    },

    data() {
        return {
            margin: 50,
            datapresent: false,
            svg: null,
            width: 0,
            height: 0,

            xScale: null,
            yScale: null,

            yaxis: null,
            xaxis: null

        }
    },

    watch: {
        numberstoshow() {
            if (this.numberstoshow.length>0) {
                this.datapresent = true;
                this.draw();
            } else {
                this.datapresent = false;
            }
        }
    },

    methods: {
        draw() {
            //const color = d3.scaleOrdinal(d3.schemeDark2);
            
            this.xScale.domain([0, this.numberstoshow[0].length-1]);
            this.yScale.domain([0, d3.max(this.numberstoshow, l => d3.max(l, n => n))]);

            this.yaxis = d3.axisLeft().scale(this.yScale); 
            this.xaxis = d3.axisBottom().scale(this.xScale);
            this.svg.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(0," + this.height + ")")
                .call(this.xaxis);

            this.svg.append("g")
                .attr("class", "axis")
                .call(this.yaxis);

        }

    },
    computed: {
        generateArc() {
            if (this.numberstoshow.length>0) return "Keyword Density Plot";
            return "Zum anzeigen des Keyword Density Plots bitte ein Keyword suchen.";
        }
    },

    mounted() {
        this.width = window.innerWidth - 2*this.margin;
        this.height = window.innerHeight  - 2*this.margin;

        this.svg = d3
            .select("#canvas")
            .append("svg")
            .attr("width", this.width)
            .attr("height", this.height);
        this.yScale = d3.scaleLinear().range([this.height, 0]);
        this.xScale = d3.scaleLinear().range([0, this.width]);
    },

    destroyed() {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
