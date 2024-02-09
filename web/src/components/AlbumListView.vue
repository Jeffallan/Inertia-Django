<script setup>

    import { Link } from '@inertiajs/vue3'
    import { router } from '@inertiajs/vue3'
    import { reactive, ref } from 'vue';

    let props = defineProps({
        albums: Array,
        page: Object
    })

    function deleteArtist(id){
        router.delete(`/${id}/delete`)
    }
    //table logic
    let itemsPerPage = ref(props.page.per_page)
    let search = reactive("")
    let headers = [{title: 'Artist',
                    align: 'start',
                    sortable: false,
                    key: 'artist',
                    },
                    {title: 'Album',
                    align: 'start',
                    sortable: false,
                    key: 'title',},
                    {title: '',
                    align: 'start',
                    sortable: false,
                    key: 'actions',},
                    
                    ]
    
    function getData(){
        return props.albums
    }
    let link = "'/'+a.id" 
</script>

<template>
    <!-- {{ page }}
    <div v-for="a in props.albums">
       <p>{{ a.artist }} <Link :href="link" >{{ a.title }} </Link>       
    </p>
        </div> -->

  <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :search="search"
    :headers="headers"
    :items-length="page.count"
    :items="getData()"
    :loading="loading"
    item-value="name"
    @update:options="loadItems"
    style="min-width: 50vw"
  >
    
  <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Albums</v-toolbar-title> <!--props-->
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              variant="elevated"
              color="secondary"
              dark
              class="mb-2"
              v-bind="props"
            >
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Dessert name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.calories"
                      label="Calories"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.fat"
                      label="Fat (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.carbs"
                      label="Carbs (g)"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.protein"
                      label="Protein (g)"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue-darken-1"
                variant="text"
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.title="{ item }">
        <Link :href="'/'+item.id" >{{ item.title }}</Link> 
    </template>
    <template v-slot:item.actions="{ item }">
        <v-btn class="ml-1" size="small" variant="text"><Link :href="'/'+item.id+'/edit'">edit</Link></v-btn> 
        <v-btn class="ml-1" size="small" variant="text" color="red" @click="deleteArtist(item.id)">delete</v-btn>
    </template>
  </v-data-table-server>
</template>


<!-- <v-btn variant="outlined"><Link href="/add">add</Link></v-btn>  -->