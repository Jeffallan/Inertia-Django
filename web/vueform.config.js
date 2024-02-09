import en from '@vueform/vueform/locales/en'
import material from '@vueform/vueform/dist/material'
import { defineConfig } from '@vueform/vueform'

import '@vueform/vueform/dist/material.css';


export default defineConfig({
  theme: material,
  locales: { en },
  locale: 'en',
})