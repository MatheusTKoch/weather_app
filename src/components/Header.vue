<script setup>
import { ref, onMounted} from 'vue';

const currentTime = ref("");

const updateTime = () => {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  currentTime.value = `${hours}:${minutes}:${seconds}`;
};

onMounted(() => {
  updateTime();
  setInterval(updateTime, 1000);
});
</script>

<template>
  <div class="header"></div>
  <RouterLink to="/">
    <div class="titulo">Weather App</div>
  </RouterLink>
  <div class="clock">{{ currentTime }}</div>
  <div class="search">
    <img src="../components/icons/search.png" alt="" class="image">
  </div>
</template>

<style scoped>
  .search {
    position: absolute;
    top: 27.75%;
    left: 42.5%;
    z-index: 1;
    width: 1%;
  }

  .image {
    width: 125%;
  }

  .header {
    position: absolute;
    width: 100vw;
    left: 0%;
    top: 0%;
    box-shadow: 0 15px 25px rgba(129, 124, 124, 0.2);
    backdrop-filter: blur(2px); 
    background-color: rgba(255, 255, 255, 0.2); 
    padding-bottom: 5%;
  }

  .titulo {
    font-family: "Open Sans", sans-serif;
    font-optical-sizing: auto;
    font-weight: 200;
    font-style: normal;
    font-variation-settings: "wdth" 86.5;
    font-size:xx-large;
    position: absolute;
    left: 2%;
    top: 2%;
    color: whitesmoke;
  }
</style>
