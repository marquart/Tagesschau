<template>
    <div>
        <p>Hier kannst du einen Begriff mit einem hohen <a href="https://de.wikipedia.org/wiki/Tf-idf-Ma%C3%9F" target="_blank">Tf-idf-Wert</a> aus einem Monat auswählen</p>

        <label for="yearselect">Wähle ein Jahr aus:</label>
        <select class="selectfield" id="yearselect"
            v-model="selectedYear">
            <option disabled selected value="Wähle ein Jahr aus">Wähle ein Jahr aus</option>
            <option class="selectoption"
                v-for="(year, i) in Object.keys(topwords)"
                :key="i"
                :value="year"
            >
                {{year}}
            </option>
        </select>

        <label v-show="validYear" for="monthselect">Wähle einen Monat aus:</label>
        <select class="selectfield" id="monthselect"
            v-if="validYear"
            v-model="selectedMonth">
            <option disabled selected value="Wähle einen Monat aus">Wähle einen Monat aus</option>
            <option class="selectoption"
                v-for="(month, i) in Object.keys(topwords[selectedYear])"
                :key="i"
                :value="month"
            >
                {{month}}
            </option>
        </select>
                


    </div>
</template>

<script>
import top_tfidf_words from '../../public/year_month_topwords.json'

export default {
    name: 'TopWordSelect',
    data() {
        return {
            topwords: top_tfidf_words,
            selectedYear: 0,
            selectedMonth: ''
        }
    },
    watch: {
        selectedMonth() {
            if (this.topwords.hasOwnProperty(this.selectedYear) && this.topwords[this.selectedYear].hasOwnProperty(this.selectedMonth)) {
                this.emitTopwords();
            }
        }
    },
    computed: {
        validYear() {
            return this.topwords.hasOwnProperty(this.selectedYear);
        }
    },
    methods: {
        emitTopwords() {
            this.$emit('showResults', this.topwords[this.selectedYear][this.selectedMonth]);
        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    .selectfield {
        font-size: 1.2em;
        font-family: inherit;
        margin: 0.3em;
    }

    .selectfield:hover {
        cursor: pointer;
    }
    .selectoption:hover {
        cursor: pointer;
    }

    p {
        margin-top: 0;
        margin-bottom: 0;
        text-align: center;
        color: black;
    }

    label {
        color: black;
    }
</style>
