<script setup>


import { useForm } from '@inertiajs/vue3'

import DefaultLayout from '../../layouts/DefaultLayout.vue'

let props = defineProps({
    message: Array,
    album: Object
})

let form = useForm({
  artist: props.album.artist,
  title: props.album.title,
})

function handleEdit(){
  router.put(usePage().url, { forceFormData: true, data: form });
}

</script>

<template>
    <DefaultLayout :messages="message">
        {{ album }}
        {{ form }}

  <form v-on:prevent.submit="handleEdit">
    <input type="text" v-model="form.artist">
    <div v-if="form.errors.arttist">{{ form.errors.artist }}</div>
    <input type="text" v-model="form.title">
    <div v-if="form.errors.title">{{ form.errors.title }}</div>
    <button type="submit" :disabled="form.processing">Update</button>
  </form >
  </DefaultLayout>
</template>