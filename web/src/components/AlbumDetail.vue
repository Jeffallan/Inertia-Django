<script setup>

    import { Link } from '@inertiajs/vue3'
    import { router } from '@inertiajs/vue3'

    defineProps({
        album: Object,
    })

    function deleteArtist(id){
        router.delete(`/${id}/delete`)
    }

</script>

<template>
    <Link href="/">home</Link>
    <div>
        {{ album }}
    <v-btn><Link :href="'/'+album.id+'/edit'">edit</Link></v-btn>
    <v-btn @click="deleteArtist(album.id)" variant="tonal">delete</v-btn>
    </div>

</template>