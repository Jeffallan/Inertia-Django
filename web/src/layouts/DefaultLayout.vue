<script setup>

import Messages from "../components/Messages.vue"
import { Link } from "@inertiajs/vue3";

defineProps({messages: Array})

</script>

<template>
    <v-layout class="d-flex flex-column align-center justify-space-between" >
    <v-app-bar
        color="primary"
        prominent
      >
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>My files</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn variant="text" icon="mdi-magnify"></v-btn>

        <v-btn variant="text" icon="mdi-filter"></v-btn>

        <v-btn variant="text" icon="mdi-dots-vertical"></v-btn>
      </v-app-bar>
    <v-navigation-drawer>
        <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
  <v-divider></v-divider>
  <v-list-item link title=""><Link href="/">home</Link></v-list-item>
  <v-list-item link title="List Item 2"></v-list-item>
  <v-list-item link title="List Item 3"></v-list-item>
    </v-navigation-drawer>
    <v-main class="d-flex flex-column align-center justify-space-between"  style="min-height: 100vh;">
   
    <div class="align-self-end mr-4 ml-4">
        <Messages :messages="messages" />
    </div>
    <div class="ma-4">
    <slot />
    </div>
    
    <div>
    <v-footer color="primary"
              class="justify-end"
              prominent
              style="min-width: 100vw;">footer</v-footer>
    </div>
</v-main>
</v-layout>
</template>

<style scoped>


</style>