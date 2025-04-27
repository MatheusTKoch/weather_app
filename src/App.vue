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
  <main class="main-content">
    <div class="content-wrapper">
      <Pesquisa @cidade="handleCidade"></Pesquisa>
      <Resultados :cidade="cidade"></Resultados>
    </div>
  </main>
  <Footer></Footer>
</template>

<style scoped>
.main-content {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 160px);
  width: 100%;
  padding: 2rem;
  margin-top: 80px;
  transform: translateX(15vw);
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 1440px) {
  .content-wrapper {
    max-width: 700px;
  }
}

@media (min-width: 1920px) {
  .content-wrapper {
    max-width: 800px;
  }
}

@media (max-width: 768px) {
  .main-content {
    min-height: calc(100vh - 140px);
    padding: 1.5rem;
    margin-top: 50px;
  }

  .content-wrapper {
    gap: 1.5rem;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: 1rem;
    margin-top: 40px;
  }

  .content-wrapper {
    gap: 1rem;
  }
}
</style>
