<script setup>
import { ref } from "vue";

const cid = ref(null);
</script>

<template>
  <div class="pesquisa">
    <img class="search" alt="">
    <input type="text" placeholder="Busca..." class="input" v-model="cid" @keypress.enter="console.log(cid)">
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
    background-repeat: no-repeat;
    background-size: cover;
  }

  .input {
    width: 150%;
    border-style: outset;
    border-width: 1px;
    border-color: transparent;
    border-radius: 10px;
    height: 30px;
    text-indent: 30px;
  }

  .input:focus {
    outline: none;
  }
</style>
