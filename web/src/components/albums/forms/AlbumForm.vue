<script setup>
import { ref, onMounted } from 'vue';
import { Link } from '@inertiajs/vue3'
import { router } from '@inertiajs/vue3'
import { usePage } from '@inertiajs/vue3';
import {useForm} from '@inertiajs/vue3';
import BackButton  from "../../buttons/BackButton.vue"

let props = defineProps({
    album: Object,
    url: String,
    method: String,
})

let data = ref({title: props.album.title, artist:props.album.artist})

let form = useForm({
  title: String,
  artist: String
})

onMounted(() => {
  if(props.album != null){
    //data.title = props.album.title,
    //data.artist = props.album.artist
    //data = {title: props.album.title, artist:props.album.artist}
  }
})
function handleEdit(){
  console.log(data.value)
  router.put(usePage().url, data.value, )
}
function handleBack(){
  history.back()
}
</script>

<template>

<Vueform  v-model="data" 
          sync
          :endpoint="false"
          @submit="handleEdit()"
           
          >
    <TextElement
      name="artist"
      label="Artist"
      field-name="artist"
      :rules="[
        'required',
        'min:1',
        'max:50',
      ]"
    />
    <TextElement
      name="title"
      label="Title"
      field-name="title"
      :rules="[
        'required',
        'min:2',
        'max:50',
      ]"
    />
    <GroupElement
      name="container2"
    >
      <GroupElement
        name="column1"
        :columns="{
          container: 6,
        }"
      >
        <BackButton />
      </GroupElement>
      <GroupElement
        name="column2"
        :columns="{
          container: 6,
        }"
      >
        <ButtonElement
          name="submit"
          button-label="Submit"
          align="right"
          :submits="true"
          
        />
      </GroupElement>
    </GroupElement>
  </Vueform>
  <!-- <v-form validate-on="input">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="data.artist"
            label="Artist"
            required

          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="data.title"
            label="Title"
            hide-details
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
        </v-col>
      </v-row>
      <v-row>
      <BackButton />
      <v-btn class="primary" variant="tonal" @click="handleEdit()">Submit</v-btn>
      </v-row>
    </v-container>
  </v-form> -->
</template>