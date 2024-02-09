import './assets/main.css'

import { createApp, h } from 'vue'
import { createInertiaApp } from '@inertiajs/vue3'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { aliases, fa } from 'vuetify/iconsets/fa'
import { mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import Vueform from '@vueform/vueform'
import vueformConfig from '../vueform.config'

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'fa',
    aliases,
    sets: {
      fa,
      mdi,
    },
  },
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