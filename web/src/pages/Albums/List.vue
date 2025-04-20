<script setup>
import { Link } from '@inertiajs/vue3'
import DefaultLayout from '../../layouts/DefaultLayout.vue';
import AlbumListView from '../../components/albums/AlbumListView.vue';


defineProps({
    albums: Array,
    message: String, 
    page: Object
})

</script>

<template>

    <DefaultLayout :messages="message"> 
        <AlbumListView :albums="albums" 
                       :page="page"/>
    </DefaultLayout>


</template>