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

    <form >
    <input type="text" v-model="form.artist">
    <div v-if="form.errors.email">{{ form.errors.email }}</div>
    <input type="text" v-model="form.title">
    <div v-if="form.errors.password">{{ form.errors.title }}</div>
    <Link  @click="handleEdit"><v-btn>Update</v-btn></Link>
  </form >

</template>