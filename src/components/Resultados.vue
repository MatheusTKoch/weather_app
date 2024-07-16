<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  cidade: String,
});
</script>

<template>
  <div class="card">
    <div class="resultados" v-if="cidade == null">Digite uma cidade acima para trazer os dados da previsao!</div>
    <div class="resultados" v-else>
      <div>Cidade: {{ cidade }}</div>
      <div>Temperatura Atual: </div>
      <div>Temperatura Mínima: </div>
      <div>Sensação Térmica: </div>
    </div>
  </div>
</template>

<style scoped>
  .resultados {
    position: absolute;
    bottom: 30%;
    left: 15%;
    padding: 12%;
  }

  .card {
    position: absolute;
    bottom: 20%;
    left: 42%;
    width: 250px; 
    box-shadow: 0 15px 25px rgba(129, 124, 124, 0.2); 
    height: 300px; 
    border-radius: 1px; 
    backdrop-filter: blur(2px); 
    background-color: rgba(255, 255, 255, 0.2); 
    padding: 10px; 
    text-align: center; 
  }
</style>
