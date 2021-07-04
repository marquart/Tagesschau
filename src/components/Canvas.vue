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
        numberstoshow: Array,
        colors: Array
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
            xaxis: null,

            linegenerator: null

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
            this.svg.selectAll("g.axis").remove()
            this.svg.selectAll("path.line").remove()
            
            this.xScale.domain([0, this.numberstoshow[0].length-1]);
            this.yScale.domain([0, d3.max(this.numberstoshow, l => d3.max(l, n => n))]);

            console.log(d3.max(this.numberstoshow, l => d3.max(l, n => n)));
            //this.xs = Array.from(Array(this.numberstoshow[0].length).keys())

            this.yaxis = d3.axisLeft().scale(this.yScale); 
            this.xaxis = d3.axisBottom().scale(this.xScale);

            this.svg.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(0," + this.height + ")")
                .call(this.xaxis);

            this.svg.append("g")
                .attr("class", "axis")
                .call(this.yaxis);

            this.numberstoshow.forEach((element, i) => {
                //console.log(element);
                this.svg.append("path")
                    .datum(element) // 10. Binds data to the line 
                    .attr("class", "line") // Assign a class for styling 
                    .attr("d", this.linegenerator) // 11. Calls the line generator
                    .style("stroke", this.colors[i]);
            });

        },
        getX(p, index) {
            return this.xScale(index);
        },
        getY(p) {
            return this.yScale(p);
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
            .attr("width", this.width+2*this.margin)
            .attr("height", this.height+2*this.margin)
            .append('g')
            .attr("transform", "translate(" + this.margin + "," + this.margin + ")");

        this.yScale = d3.scaleLinear().range([this.height, 0]);
        this.xScale = d3.scaleLinear().range([0, this.width]);

        this.linegenerator = d3.line()
            .x(this.getX) // set the x values for the line generator
            .y(this.getY) // set the y values for the line generator 
            .curve(d3.curveMonotoneX) // apply smoothing to the line
    },

    destroyed() {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
    .axis {
        font-family: inherit;
        font-size: inherit;
    }
    .line {
        stroke-width: 2;
        fill: none;
        stroke: black;
    }

</style>
