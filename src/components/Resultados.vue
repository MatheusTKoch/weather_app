<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const weatherData = ref(null);

const pesquisaData = async () => {
  const city = route.params.cidade;
  try {
    const response = await axios.get('http://localhost:5000/resultado', {
      params: { city }
    });
    weatherData.value = response.data;
    console.log(weatherData)
  } catch (error) {
    console.error('Error fetching weather data:', error);
  }
};

watch(() => route.params.cidade, (novaCidade) => {
  pesquisaData(novaCidade);
})

</script>

<template>
  <div class="card">
    <div class="resultados" v-if="weatherData == null">Digite uma cidade acima para trazer os dados da previsão atual!</div>
    <div class="resultados" v-else>
      <div>Cidade: {{ weatherData.name }}</div>
      <div>Temperatura Atual: {{ weatherData.description }} </div>
      <div>Temperatura Mínima: {{ weatherData.min_temp }} </div>
      <div>Sensação Térmica: {{ weatherData.feels_like }}</div>
    </div>
  </div>
</template>

<style scoped>
  .resultados {
    position: absolute;
    bottom: 22%;
    left: 6%;
    padding: 12%;
    font-size: 22px;
    text-align: start;
  }

  .card {
    position: absolute;
    bottom: 20%;
    left: 44%;
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
