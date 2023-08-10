// vite.config.js
import { defineConfig } from 'vite';
import postcss from 'rollup-plugin-postcss'; // Add the missing import
import tailwindcss from 'tailwindcss';
import path from 'path';
import vue from '@vitejs/plugin-vue';
import sassPlugin from 'vite-plugin-sass';

export default defineConfig({
  plugins: [
    postcss({
      plugins: [tailwindcss('./tailwind.config.js')],
      extract: path.resolve('static/css/style.css'),
    }),
    vue(),
    sassPlugin()
  ],
  build: {
    outDir: 'static',
  },
  resolve:{
    alias:{
      '/@':path.resolve(__dirname,'assets/scss')
    }
  },
  server: {
    proxy: {
      '/': 'http://127.0.0.1:8000', // Adjust the port if your Django server runs on a different port
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import './assets/scss/styles.scss';`, // Use the alias to fix the path
      },
    },
  },
});
