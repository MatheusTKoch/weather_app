<script setup>

</script>

<template>
  <footer class="footer">
    <div class="social-links">
      <a target="_blank" href="https://github.com/MatheusTKoch" class="social-link">
        <img class="icon github" alt="Github" src="data:image/png;base64,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">
      </a>
      <a target="_blank" href="https://www.linkedin.com/in/matheus-trilha-koch-712806162/" class="social-link">
        <img class="icon linkedin" alt="Linkedin" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZElEQVR4nO2ZvUoDQRSFP1Hs/AFtBQt9A99BwV20FIV0lr6CjQTyID6DnSbqg9gp/iDopkpzZWEaw+zOzFrsHbkHThNuZs+Xu3dmk4DJZOqqI2ACTAHp2VNgDJSpECMF4aXBw5ROiHIXMSATBUEl4LsYkEpBUAn4OwZEMnFQfQcUA5lT2yfyApwAG85nwFuOHdlXtF0H1fbmVU/9Wo4gpae+yBHkHRgAm871jLzmCCKKHFTfAcVA5tSlnSk1j+4s2gKWgRVgD7gEPnIAqQ/Og8C114Eb7SA7MRcHloAHzSAp2gZmOYAsRtRcawa5AJ5d3RNw3lJ7qhXkOPH7965WkPuGNevfCOjwMNobyGfDmvXrPi1oBfnrumIgWEe8slsLmxFs1xL/eNiMiJ0jtG+TmhzUvwGpFISUgL9iQMYKgkrAtzEgpYKgEvAhkRoqCCsNviJRhfv3VMPMVO52iu6EyWTil34AFdRDhxtrT8cAAAAASUVORK5CYII=">
      </a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
  z-index: 100;
}

.social-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
  padding: 0.5rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease;
}

.social-link:hover {
  transform: scale(1.1);
}

.icon {
  width: clamp(24px, 4vw, 32px);
  height: auto;
  opacity: 0.9;
  transition: all 0.3s ease;
}

.icon:hover {
  opacity: 1;
  filter: brightness(1.2);
}

.github:hover {
  outline: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  outline-offset: 4px;
}

.linkedin:hover {
  outline: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 20%;
  outline-offset: 4px;
}

@media (max-width: 768px) {
  .footer {
    padding: 0.8rem 0;
  }

  .social-links {
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .footer {
    padding: 0.6rem 0;
  }

  .social-links {
    gap: 0.8rem;
  }

  .icon {
    width: clamp(20px, 3vw, 28px);
  }
}
</style>