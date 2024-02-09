import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import  { resolve } from "path"


//https://vitejs.dev/config/
//export default defineConfig({
//  plugins: [
//    vue(),
//  ],
//  resolve: name => {
//      const pages = import.meta.glob('./pages/**/*.vue', { eager: true })
//      return pages[`./pages/${name}.vue`]
//    },
//    alias: {
//      '@': fileURLToPath(new URL('./src', import.meta.url))
//    },  
//  
//})


export default defineConfig({
  base: "/static/",
  plugins: [
      vue({
        compilerOptions: {
          hydratable: false
        }
      })
  ],
  
  build: {
    outDir: resolve('./dist'),
    manifest: true,
    rollupOptions: {
      input: './src/main.js',
    },
  },
  server: {
    origin: "http://localhost:5173",
    cors: {
      allowedHeaders: "*"
    }
  }
}) 
