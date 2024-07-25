<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const cid = ref(null);
const router = useRouter();
const emit = defineEmits(["cidade"]);

function pesquisaCidade() {
  emit("cidade", cid.value);
  if (cid.value) {
    router.push({ name: "Resultado" , params: { cidade: cid.value }});
  }
}
</script>

<template>
  <div class="pesquisa">
    <img class="search" alt="">
    <input type="text" placeholder="Busca..." class="input" v-model="cid" @keypress.enter="pesquisaCidade">
  </div>
</template>

<style scoped>
  .pesquisa {
    position: absolute;
    left: 42%;
    top: 25%;
  }

  .search {
    background-image: url('../components/icons/search.png');
    background-size: cover;
  }

  .input {
    width: 150%;
    border-style: outset;
    border-width: 1px;
    border-color: transparent;
    border-radius: 10px;
    height: 32px;
    text-indent: 34px;
    font-size: 18px;
  }

  .input:focus {
    outline: none;
  }
</style>
