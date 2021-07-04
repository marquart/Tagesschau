<template>
    <div class="Selection">
        <span class="card"
            v-for="(word, i) in words"
            :key="i"
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
        words: Array
    },
    data() {
        return {

        }
    },
    methods: {
        deleteWord(index) {
            this.$emit('delete', index)
        }

    },
    computed: {
        showWords() {
            //return this.words;
            return Array.from(this.words).join(', ');
        }
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
        padding: 0.5em;
        margin: 0.3em;
        border: 1px solid #000000;
    }
    .card:hover {
        background-color: #de141b;
        color: white;
        border-color: white;        
        cursor: pointer;
    }
</style>
