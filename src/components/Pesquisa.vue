<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

const cid = ref("");
const router = useRouter();
const emit = defineEmits(["cidade"]);

function pesquisaCidade() {
  if (cid.value?.trim()) {
    emit("cidade", cid.value.trim());
    router.push({ name: "Resultado", params: { cidade: cid.value.trim() }});
  }
}
</script>

<template>
  <div class="pesquisa">
    <div class="search-container">
      <span class="p-input-icon-right">
        <Button
          icon="pi pi-search"
          severity="success"
          text
          rounded
          aria-label="Search"
          class="search-button"
          @click="pesquisaCidade"
          v-tooltip.bottom="'Pesquisar'"
        />
        <InputText
          v-model="cid"
          type="text"
          placeholder="Buscar cidade..."
          class="p-inputtext-lg"
          @keydown.enter="pesquisaCidade"
        />
      </span>
    </div>
  </div>
</template>

<style scoped>
.pesquisa {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.search-container {
  position: relative;
  width: 100%;
  max-width: 450px;
  margin: 0 auto;
}

.p-input-icon-right {
  width: 100%;
  position: relative;
}

:deep(.p-inputtext) {
  width: 100%;
  background: var(--surface-section);
  border: 1px solid var(--surface-border);
  border-radius: 25px;
  color: var(--green-100);
  font-size: 1.1rem;
  padding: 1rem 3rem 1rem 1.5rem;
  backdrop-filter: blur(8px);
  transition: all 0.3s ease;
}

:deep(.p-inputtext:enabled:focus) {
  outline: none;
  background: var(--surface-card);
  border-color: var(--green-500);
  box-shadow: 0 0 15px rgba(0, 189, 126, 0.2);
}

:deep(.p-inputtext:enabled:hover) {
  border-color: var(--green-400);
}

:deep(.p-inputtext::placeholder) {
  color: var(--surface-400);
}

.search-button {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
  transition: all 0.3s ease;
}

:deep(.search-button .p-button-icon) {
  font-size: 1.2rem;
  color: var(--green-500);
  transition: color 0.3s ease;
}

:deep(.search-button:hover .p-button-icon) {
  color: var(--green-400);
  transform: scale(1.1);
}

:deep(.p-inputtext:focus::placeholder) {
  transform: translateX(10px);
  opacity: 0.5;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .pesquisa {
    padding: 0.8rem;
  }

  .search-container {
    max-width: 400px;
  }
  
  :deep(.p-inputtext) {
    font-size: 1rem;
    padding: 0.8rem 3rem 0.8rem 1.2rem;
  }
}

@media (max-width: 480px) {
  .pesquisa {
    padding: 0.6rem;
  }

  .search-container {
    max-width: 100%;
    padding: 0 0.5rem;
  }
  
  :deep(.p-inputtext) {
    font-size: 0.95rem;
    padding: 0.7rem 2.8rem 0.7rem 1.2rem;
  }

  :deep(.search-button .p-button-icon) {
    font-size: 1.1rem;
  }
}

@media (min-width: 1440px) {
  .search-container {
    max-width: 550px;
  }

  :deep(.p-inputtext) {
    font-size: 1.2rem;
  }
}

@media (min-width: 1920px) {
  .search-container {
    max-width: 650px;
  }
}
</style>
