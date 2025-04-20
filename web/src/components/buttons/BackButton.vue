<script setup>
    function handleBack(){
        history.back()
    }
</script>

<template>
    <v-btn @click="handleBack()">Cancel</v-btn>    
</template>