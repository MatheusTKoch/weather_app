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
  isLoading.value = true;
  weatherData.value = null;
  try {
    const response = await axios.get('https://MatheusTK.pythonanywhere.com/resultado', {
      params: { city }
    });
    weatherData.value = response.data;
    
    if (response.data.description === "algumas nuvens") {
      condicao.value = "algumas nuvens";
    } else if (response.data.description === "tempestade com chuva"){
      condicao.value = "tempestade com chuva";
    } else if (response.data.description === "garoa"){
      condicao.value = "garoa";
    } else if (response.data.description === "neve"){
      condicao.value = "neve";
    } else if (response.data.description === "céu limpo"){
      condicao.value = "céu limpo";
    } else if (response.data.description === "nublado"){
      condicao.value = "nublado";
    }
  } catch (error) {
    console.log(error);
    if (error && error.response && error.response.status === 404) {
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
    <div class="content">
      <div class="message" v-if="weatherData == null && !isLoading && !cidadeNaoEncontrada">
        Digite uma cidade acima para trazer os dados da previsão atual!
      </div>
      
      <div class="loading" v-if="isLoading">Carregando...</div>
      
      <div class="error-message" v-if="cidadeNaoEncontrada">
        Cidade não encontrada, por favor pesquise novamente!
      </div>
      
      <div class="weather-data" v-else-if="weatherData">
        <div class="data-item">Cidade: {{ weatherData.name }}</div>
        <div class="data-item condition">
          Condição: {{ weatherData.description[0].toUpperCase() + weatherData.description.slice(1) }}
          <span class="weather-icon">
            <img v-if="condicao == 'algumas nuvens'" alt="☁️">
            <img v-else-if="condicao == 'tempestade com chuva'" alt="⛈️">
            <img v-else-if="condicao == 'garoa'" alt="🌧️">
            <img v-else-if="condicao == 'neve'" alt="🌨️">
            <img v-else-if="condicao == 'céu limpo'" alt="☀️">
            <img v-else-if="condicao == 'nublado'" alt="🌥️">
          </span>
        </div>
        <div class="data-item">Temperatura Mínima: {{ weatherData.min_temp }} °C</div>
        <div class="data-item">Sensação Térmica: {{ weatherData.feels_like }} °C</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.weather-card {
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
}


:deep(.p-card) {
  background: var(--surface-section);
  backdrop-filter: blur(8px);
  border: 1px solid var(--surface-border);
  border-radius: 15px;
  transition: all 0.3s ease;
}

.card {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
  padding: 1.5rem;
  box-shadow: 0 15px 25px rgba(129, 124, 124, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.15);
  transition: all 0.3s ease;
}

@media (min-width: 1440px) {
  .weather-card {
    max-width: 550px;
  }
  
  .card {
    max-width: 550px;
  }
  
  .content {
    min-height: 200px;
  }
}

@media (min-width: 1920px) {
  .weather-card {
    max-width: 650px;
  }
  
  .card {
    max-width: 650px;
  }
  
  .content {
    min-height: 220px;
  }
}

@media (max-width: 768px) {
  .weather-card {
    max-width: 400px;
  }
  
  .card {
    width: 100%;
    max-width: 400px;
  }

  .content {
    min-height: 160px;
  }
}

@media (max-width: 480px) {
  .weather-card {
    max-width: 100%;
  }
  
  .card {
    width: 100%;
    max-width: 100%;
    padding: 1rem;
  }

  .content {
    min-height: 140px;
    padding: 0.5rem;
  }

  .data-item {
    padding: 0.4rem;
  }
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 180px; 
  padding: 1rem;
}

.message,
.error-message,
.loading {
  font-size: clamp(1rem, 2.5vw, 1.3rem);
  text-align: center;
  color: white;
  padding: 1rem;
}

.error-message {
  color: #ff6b6b;
}

.weather-data {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.data-item {
  font-size: clamp(0.9rem, 2vw, 1.2rem);
  color: white;
  text-align: left;
  padding: 0.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.condition {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.weather-icon {
  margin-left: 0.5rem;
}

.weather-icon img {
  width: clamp(24px, 4vw, 32px);
  height: auto;
}
</style>
