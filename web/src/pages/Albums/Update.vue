<script setup>

import DefaultLayout from '../../layouts/DefaultLayout.vue'
    defineProps({
        message: Array,
        album: Object
    })

</script>

<template>
    <DefaultLayout :messages="message">
        {{ album }}
        <Vueform>
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
      name="Album"
      label="Album"
      field-name="album"
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
        <ButtonElement
          name="secondaryButton"
          button-label="Cancel"
          :secondary="true"
        />
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
          :submits="true"
        />
      </GroupElement>
    </GroupElement>
  </Vueform>
    </DefaultLayout>
</template>