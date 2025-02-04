<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const route = useRoute();
const weatherData = ref(null);
const isLoading = ref(false);
const cidadeNaoEncontrada = ref(false);
const condicao = ref('');

const pesquisaData = async (city) => {
  console.log(URL_API)
  isLoading.value = true;
  weatherData.value = null;
  try {
    const response = await axios.get('MatheusTK.pythonanywhere.com/resultado', {
      params: { city }
    });
    weatherData.value = response.data;
    if (response.data.description == "algumas nuvens") {
      condicao.value = "algumas nuvens";
    } else if (response.value.description == "tempestade com chuva"){
      condicao.value = "tempestade com chuva";
    } else if (response.value.description == "garoa"){
      condicao.value = "garoa";
    } else if (response.value.description == "neve"){
      condicao.value = "neve";
    } else if (response.value.description == "céu limpo"){
      condicao.value = "céu limpo";
    } else if (response.value.description == "nublado"){
      condicao.value = "nublado";
    }
  } catch (error) {
    console.log(error)
    if (error && error.response.status == "404") {
      cidadeNaoEncontrada.value = true;
    }
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
    <div class="resultados_1" v-if="weatherData == null && !isLoading && cidadeNaoEncontrada == false">Digite uma cidade acima para trazer os dados da previsão atual!</div>
    <div class="loading" v-if="isLoading">Carregando...</div>
    <div class="cid_nao_encontrada" v-if="cidadeNaoEncontrada">Cidade não encontrada, por favor pesquise novamente!</div>
    <div class="resultados_2" v-else-if="weatherData">
      <div>Cidade: {{ weatherData.name }}</div>
      <div>Condição: {{ weatherData.description[0].toUpperCase() + weatherData.description.slice(1) }}
        <img v-if="condicao == 'algumas nuvens'" alt="☁️">
        <img v-else-if="condicao == 'tempestade com chuva'" alt="⛈️">
        <img v-else-if="condicao == 'garoa'" alt="🌧️">
        <img v-else-if="condicao == 'neve'" alt="🌨️">
        <img v-else-if="condicao == 'céu limpo'" alt="☀️">
        <img v-else-if="condicao == 'nublado'" alt="🌥️">
      </div>
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

  .cid_nao_encontrada {
    position: absolute;
    bottom: 15%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 22px;
    text-align: center;
  }
</style>
