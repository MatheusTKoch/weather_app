<template>
  <div class="card">
    <div class="resultados">
      <div>Cidade: </div>
      <div>Temperatura Atual: </div>
      <div>Temperatura Mínima </div>
      <div>Sensação Térmica: </div>
    </div>
  </div>
</template>

<style scoped>
  .resultados {
    position: absolute;
    bottom: 25%;
    left: 43%;
  }

  .card {
    position: absolute;
    bottom: 20%;
    left: 42%;
    width: 250px; 
    box-shadow: 0 15px 25px rgba(129, 124, 124, 0.2); 
    height: 300px; 
    border-radius: 1px; 
    backdrop-filter: blur(2px); 
    background-color: rgba(255, 255, 255, 0.2); 
    padding: 10px; 
    text-align: center; 
  }
</style>
