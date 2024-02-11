<script setup>

let props = defineProps({messages: Array})

function messagePayload(){
    if (props.messages.length > 0){
    let arr = []
    for (let i = 0; i < props.messages.length; i++) {
        let message = props.messages[i]
        arr.push(JSON.parse(message.replace(/'/g, '"')))
}
return arr
}
}

</script>

<template>
 <v-alert v-for="m in messagePayload()" closable 
                                        :text="m.message"
                                        :type="m.class"
                                        :title="m.title"
                                        variant="tonal" 
                                        />
</template>