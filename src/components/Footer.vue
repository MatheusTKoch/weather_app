<script setup>
</script>

<template>
  <Toolbar class="footer">
    <template #center>
      <div class="social-links">
        <Button
          icon="pi pi-github"
          rounded
          text
          severity="success"
          aria-label="Github"
          class="social-button"
          v-tooltip.top="'Github'"
          @click="() => window.open('https://github.com/MatheusTKoch', '_blank')"
        />
        <Button
          icon="pi pi-linkedin"
          rounded
          text
          severity="success"
          aria-label="LinkedIn"
          class="social-button"
          v-tooltip.top="'LinkedIn'"
          @click="() => window.open('https://www.linkedin.com/in/matheus-trilha-koch-712806162/', '_blank')"
        />
      </div>
    </template>
  </Toolbar>
</template>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: var(--surface-section);
  backdrop-filter: blur(8px);
  border: none;
  padding: 0.5rem 0;
  z-index: 100;
}

.footer::v-deep(.p-toolbar) {
  background: transparent;
  border: none;
  padding: 0.5rem;
}

.social-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}

.social-button {
  transition: all 0.2s ease;
  width: 2.5rem;
  height: 2.5rem;
}

.social-button:hover {
  transform: scale(1.1);
}

.social-button::v-deep(.p-button-icon) {
  font-size: 1.2rem;
  color: var(--green-100);
}

.social-button:hover::v-deep(.p-button-icon) {
  color: var(--green-500);
}

@media (max-width: 768px) {
  .footer {
    padding: 0.4rem 0;
  }

  .social-links {
    gap: 0.8rem;
  }

  .social-button::v-deep(.p-button-icon) {
    font-size: 1.1rem;
  }
}

@media (max-width: 480px) {
  .footer {
    padding: 0.3rem 0;
  }

  .social-links {
    gap: 0.6rem;
  }

  .social-button::v-deep(.p-button-icon) {
    font-size: 1rem;
  }
}
</style>