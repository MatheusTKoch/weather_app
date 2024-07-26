<script setup>
import { ref } from "vue";
import Header from './components/Header.vue';
import Pesquisa from './components/Pesquisa.vue';
import Resultados from './components/Resultados.vue';
import Footer from './components/Footer.vue';

const cidade = ref(null);

function handleCidade(param) {
  cidade.value = param;
}
</script>

<template>
  <Header></Header>
  <Pesquisa @cidade="handleCidade"></Pesquisa>
  <Resultados :cidade="cidade"></Resultados>
  <Footer></Footer>
</template>

<style scoped>

</style>
