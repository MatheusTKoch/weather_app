<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

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
      <input 
        type="text" 
        placeholder="Buscar cidade..." 
        class="input" 
        v-model="cid" 
        @keypress.enter="pesquisaCidade"
      >
      <button 
        class="search-button"
        @click="pesquisaCidade"
        aria-label="Pesquisar"
      >
        <img 
          src="../components/icons/search.png" 
          alt="Ícone de pesquisa"
          class="search-icon"
        >
      </button>
    </div>
  </div>
</template>

<style scoped>
.pesquisa {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 1rem;
}

.search-container {
  position: relative;
  width: 100%;
  max-width: 450px; 
  margin: 0 auto;
  transform: translateX(50%);
}

.input {
  width: 100%;
  height: 45px;
  padding: 0.5rem 3rem 0.5rem 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  color: white;
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
}

.search-button {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.search-button:hover {
  transform: translateY(-50%) scale(1.1);
}

.search-icon {
  width: 22px;
  height: 22px;
  opacity: 0.9;
  transition: opacity 0.2s ease;
}

.search-button:hover .search-icon {
  opacity: 1;
}

@media (max-width: 768px) {
  .pesquisa {
    top: 70px;
    padding: 0.8rem;
  }

  .search-container {
    max-width: 400px;
  }
  
  .input {
    height: 40px;
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .pesquisa {
    top: 60px;
    padding: 0.6rem;
  }

  .search-container {
    max-width: 300px;
  }
  
  .input {
    height: 38px;
    font-size: 0.95rem;
    padding: 0.5rem 2.8rem 0.5rem 1.2rem;
  }

  .search-icon {
    width: 20px;
    height: 20px;
  }
}
</style>
