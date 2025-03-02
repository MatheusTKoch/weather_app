<script setup>
import { ref, onMounted} from 'vue';

const currentTime = ref("");

const updateTime = () => {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  currentTime.value = `${hours}:${minutes}`;
};

onMounted(() => {
  updateTime();
  setInterval(updateTime, 1000);
});
</script>

<template>
  <div class="header">
    <RouterLink to="/" class="title-link">
      <div class="titulo">Weather App</div>
    </RouterLink>
    <div class="clock">{{ currentTime }}</div>
    <div class="search">
      <img src="../components/icons/search.png" alt="Search icon" class="image">
    </div>
  </div>
</template>

<style scoped>
.header {
  position: fixed;
  width: 100%;
  left: 0;
  top: 0;
  box-shadow: 0 15px 25px rgba(129, 124, 124, 0.2);
  backdrop-filter: blur(2px);
  background-color: rgba(255, 255, 255, 0.2);
  padding: 0.75rem 1.5rem; 
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 3rem; 
}

.title-link {
  text-decoration: none;
}

.titulo {
  font-family: "Open Sans", sans-serif;
  font-weight: 200;
  font-size: clamp(1.5rem, 3vw, 2rem);
  color: whitesmoke;
}

.clock {
  font-weight: 200;
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  color: whitesmoke;
  font-family: "Open Sans", sans-serif;
  margin-right: 4rem; 
  margin-left: auto; 
}

.search {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: clamp(20px, 3vw, 30px);
}

.image {
  width: 100%;
  height: auto;
}

@media (max-width: 768px) {
  .header {
    padding: 0.6rem 1.2rem; 
  }

  .clock {
    margin-right: 0.5rem; 
  }
}

@media (max-width: 480px) {
  .header {
    flex-direction: column;
    padding: 0.75rem 0.5rem;
    gap: 0.3rem; 
  }

  .clock {
    margin: 0;
  }
}
</style>
