<script setup>

defineProps({messages: Array})

</script>

<template>

 <h2 v-for="m in messages">{{ m }}</h2>

</template>