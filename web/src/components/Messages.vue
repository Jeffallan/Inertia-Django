<script setup>
import { ref } from 'vue';


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
                                        close-label="Close"
                                        :text="m.message"
                                        :type="m.class"
                                        :title="m.title"
                                        icon="$success"
                                        variant="tonal" 
                                        >
<!-- <template v-slot:close>
    <v-icon>mdi-close</v-icon>
</template> -->
</v-alert>
</template>

<!-- close -->