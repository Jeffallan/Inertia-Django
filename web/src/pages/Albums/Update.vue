<script setup>

import { Link } from '@inertiajs/vue3'
import { router } from '@inertiajs/vue3'
import { usePage } from '@inertiajs/vue3'
import { useForm } from '@inertiajs/vue3'

import DefaultLayout from '../../layouts/DefaultLayout.vue'
import AlbumForm from "../../components/albums/forms/AlbumForm.vue"

let props = defineProps({
    message: Array,
    album: Object
})

let form = useForm({
  artist: props.album.artist,
  title: props.album.title,
})

function handleEdit(){
  //router.put(usePage().url, { forceFormData: true, data: form });
  form.put(usePage().url, {data: form})
}

</script>

<template>
    <DefaultLayout :messages="message">
    <AlbumForm :album="props.album"
               :url="usePage().url"
               method="put"
               />
  <!-- <form >
    <input type="text" v-model="form.artist">
    <div v-if="form.errors.email">{{ form.errors.email }}</div>
    <input type="text" v-model="form.title">
    <div v-if="form.errors.title">{{ form.errors.title }}</div>
    <Link :href="usePage().url" @click="handleEdit"><v-btn>Update</v-btn></Link>
  </form > -->
  </DefaultLayout>
</template>