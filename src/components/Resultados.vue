<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const weatherData = ref(null);
const isLoading = ref(false);

const pesquisaData = async (city) => {
  isLoading.value = true;
  weatherData.value = null;
  try {
    const response = await axios.get('http://localhost:5000/resultado', {
      params: { city }
    });
    weatherData.value = response.data;
    console.log(weatherData);
  } catch (error) {
    console.error('Error fetching weather data:', error);
  } finally {
    isLoading.value = false;
  }
};

watch(() => route.params.cidade, (novaCidade) => {
  if (novaCidade) {
    pesquisaData(novaCidade);
  }
});

</script>

<template>
  <div class="card">
    <div class="resultados_1" v-if="weatherData == null && !isLoading">Digite uma cidade acima para trazer os dados da previsão atual!</div>
    <div class="loading" v-if="isLoading">Carregando...</div>
    <div class="resultados_2" v-else-if="weatherData">
      <div>Cidade: {{ weatherData.name }}</div>
      <div>Condição: {{ weatherData.description[0].toUpperCase() + weatherData.description.slice(1) }}</div>
      <div>Temperatura Mínima: {{ weatherData.min_temp }} °C</div>
      <div>Sensação Térmica: {{ weatherData.feels_like }} °C</div>
    </div>
  </div>
</template>

<style scoped>
  .resultados_1 {
    position: absolute;
    bottom: 22%;
    left: 6%;
    padding: 12%;
    font-size: 22px;
    text-align: start;
  }

  .resultados_2 {
    position: absolute;
    bottom: 10%;
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

  .loading {
    position: absolute;
    bottom: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    text-align: center;
  }
</style>
