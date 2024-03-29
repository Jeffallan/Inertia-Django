import './assets/main.css'

import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { aliases, fa } from 'vuetify/iconsets/fa'
import { mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import vueformConfig from '../vueform.config'
import Vueform from '@vueform/vueform'


const vuetify = createVuetify({
  components,
  directives,
  // icons: {
  //   defaultSet: 'mdi',
  //   aliases,
  //   sets: {
  //     fa,
  //     mdi,
  //   },
  // },
})

createInertiaApp({
  resolve: name => {
    const pages = import.meta.glob('./pages/**/*.vue', { eager: true })
    return pages[`./pages/${name}.vue`]
  },
  setup({ el, App, props, plugin}) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(vuetify)
      .use(Vueform, vueformConfig)
      .mount(el)
  },
})