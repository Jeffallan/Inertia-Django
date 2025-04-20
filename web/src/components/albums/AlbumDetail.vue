<script setup>

    import { Link } from '@inertiajs/vue3'
    import { router } from '@inertiajs/vue3'
    import { useForm } from '@inertiajs/vue3'

  let props =  defineProps({
        album: Object,
    })

    let form = useForm({
  artist: props.album.artist,
  title: props.album.title,
})
    
    function deleteArtist(id){
        router.delete(`/${id}/delete`)
    }

    function handleEdit(){
  form.put(`${props.album.id}/edit`, {data: form, })
}

</script>

<template>
    <Link href="/">home</Link>
    <div>
        {{ album }}
    <v-btn><Link :href="'/'+props.album.id+'/edit'">edit</Link></v-btn>
    <v-btn @click="deleteArtist(props.album.id)" variant="tonal">delete</v-btn>
    </div>
</template>