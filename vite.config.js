// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/': 'http://127.0.0.1:8000', // Adjust the port if your Django server runs on a different port
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import 'assets/scss/styles.scss;`,
      },
    },
  },
});
