<script setup>

import DefaultLayout from '../../layouts/DefaultLayout.vue'
import AlbumDetail from '../../components/AlbumDetail.vue';


defineProps({message: Array,
             album: Object
             })
</script>

<template>

<DefaultLayout :messages="message" >
    <AlbumDetail :album="album"/>
</DefaultLayout>

</template>