<script setup>
import { ref, onMounted } from 'vue';

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
  <Toolbar class="header">
    <template #start>
      <RouterLink to="/" class="title-link">
        <span class="titulo">
          <i class="pi pi-cloud mr-2"></i>
          Weather App
        </span>
      </RouterLink>
    </template>
    <template #end>
      <div class="clock-container">
        <i class="pi pi-clock mr-2"></i>
        <span class="clock">{{ currentTime }}</span>
      </div>
    </template>
  </Toolbar>
</template>

<style scoped>
.header {
  position: fixed;
  width: 100%;
  left: 0;
  top: 0;
  background-color: var(--surface-section);
  backdrop-filter: blur(8px);
  border: none;
  z-index: 1000;
}

.header::v-deep(.p-toolbar) {
  background: transparent;
  border: none;
  padding: 0.75rem 1.5rem;
}

.title-link {
  text-decoration: none;
}

.titulo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-family);
  font-weight: 500;
  font-size: clamp(1.5rem, 3vw, 2rem);
  color: var(--green-100);
}

.titulo i {
  color: var(--green-500);
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
}

.clock-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--green-100);
}

.clock {
  font-weight: 400;
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  font-family: var(--font-family);
}

.pi-clock {
  color: var(--green-500);
  font-size: clamp(1rem, 2vw, 1.4rem);
}

@media (max-width: 768px) {
  .header::v-deep(.p-toolbar) {
    padding: 0.6rem 1.2rem;
  }

  .titulo {
    font-size: 1.4rem;
  }

  .clock {
    font-size: 1.2rem;
  }
}

@media (max-width: 480px) {
  .header::v-deep(.p-toolbar) {
    padding: 0.5rem;
    flex-direction: column;
    gap: 0.5rem;
  }

  .titulo {
    font-size: 1.3rem;
  }

  .clock {
    font-size: 1.1rem;
  }
}
</style>
