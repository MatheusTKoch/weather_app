<script setup>
import { ref } from "vue";
import Header from './components/Header.vue';
import Pesquisa from './components/Pesquisa.vue';
import Resultados from './components/Resultados.vue';

const cidade = ref(null);

function handleCidade(param) {
  cidade.value = param;
}
</script>

<template>
  <Header></Header>
  <Pesquisa @cidade="handleCidade"></Pesquisa>
  <Resultados :cidade="cidade"></Resultados>
</template>

<style scoped>

</style>
