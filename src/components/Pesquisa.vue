<script setup>

</script>

<template>
  <div class="pesquisa">
    <img class="search" alt="">
    <input type="text" placeholder="Busca..." class="input">
  </div>
</template>

<style scoped>
  .pesquisa {
    position: absolute;
    left: 40%;
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
