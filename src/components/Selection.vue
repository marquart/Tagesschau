<template>
    <div class="Selection">
        <span class="card"
            v-for="(word, i) in words"
            :key="i"
            :style="setColor(i)"
            @click="deleteWord(i)"
        >
        {{word}} ⌫
        </span>
    </div>
</template>

<script>


export default {
    name: 'Selection',
    props: {
        words: Array,
        colors: Array
    },
    data() {
        return {

        }
    },
    methods: {
        deleteWord(index) {
            this.$emit('delete', index)
        },
        setColor(index) {
            return {"background-color": this.colors[index]}//{"color": this.colors[index], "border-color": this.colors[index]}
        }

    },
    computed: {
    },

    mounted() {

    },
    destroyed() {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .Selection {
        margin-top :  1.5em;
        margin-left:  5%;
        margin-right: 5%;
        text-align: center;
        width: 90%;
        box-sizing: border-box;
    }

    .card {
        display: inline;
        padding: 0.4em;
        margin: 0.3em;
        border: 3px solid white;
        background-color: #f1f1f1;
        color: black;
        
    }
    .card:hover {
        background-color: #de141b !important;
        color: white !important;
        /*border-color: white !important;*/
        cursor: pointer;
    }
</style>
