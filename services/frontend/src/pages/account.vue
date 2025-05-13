<template>
  <v-row class="pa-10">
    <h1>Hello <b>{{store.users[0].user}}</b></h1>
  </v-row>

  <v-row class="pt-5 pl-10 pr-10">
    <p>You're admin, you can manage users and products in store</p>
  </v-row>

  <v-row class="pt-5 pl-10 pr-10">
    <p>The following options are available:</p>
  </v-row>

  <v-row class="pa-10">
    <v-btn>
      <template v-slot:prepend>
        <v-icon>mdi-account-cog</v-icon>
      </template>
      Manage users
    </v-btn>
    <v-btn class="ml-5">
      <template v-slot:prepend>
        <v-icon>mdi-store-edit</v-icon>
      </template>
      Manage products
    </v-btn>
  </v-row>

  <v-container class="pa-10">
    <v-btn color="primary" @click="openDialog()">Add Product</v-btn>
    <v-data-table :headers="headers"
                  :items="products"
                  item-value="id"
                  class="limited-columns"
    >
      <template #item.actions="{ item }">
        <v-btn icon="mdi-pencil" @click="openDialog(item)" />
        <v-btn icon="mdi-delete" @click="deleteProduct(item.id)" />
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="text-h6">{{ editedProduct.id ? 'Edit' : 'Add' }} Product</span>
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="editedProduct.title" label="Name" />
          <v-text-field v-model="editedProduct.subtitle" label="Description" />
          <v-text-field v-model="editedProduct.source" label="Image" />
          <v-text-field v-model="editedProduct.price" label="Price" type="number" />
          <v-text-field v-model="editedProduct.category" label="Category" />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="closeDialog">Cancel</v-btn>
          <v-btn color="primary" @click="saveProduct">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useMyStore } from "@/stores/myStore.js"
import { storeToRefs } from 'pinia'
import axios from 'axios'

const store = useMyStore()

const headers = [
  {title: 'Id', key: 'id'},
  {title: 'Title', key: 'title' },
  {title: 'Subtitle', key: 'subtitle'},
  {title: 'Source', key: 'source'},
  {title: 'Price', key: 'price'},
  {title: 'Category', key: 'category'},
  {title: 'Actions', key: 'actions', sortable: false},
]

const { products } = storeToRefs(store)

const dialog = ref(false)
const editedProduct = ref()

function openDialog(product = null){
  if (product) {
    editedProduct.value = { ...product }
  }
  else {
    editedProduct.value = { title: null, qtd: 0}
  }
  dialog.value = true
}

function closeDialog() {
  dialog.value = false
}

function saveProduct() {
  if (editedProduct.value.id) {
    axios.put(`http://localhost:8500/products/${editedProduct.value.id}`, editedProduct.value)
  } else {
    axios.post("http://localhost:8500/products", editedProduct.value)
        .then(response => {
          console.log("Updated:", response.data)
        })
        .catch(error => {
          console.error("Error updating product:", error)
        })
  }
  closeDialog()
  store.fetchProducts()
}

function deleteProduct(id) {
  // products.value = products.value.filter(p => p.id !== id)
  axios.delete(`http://localhost:8500/products/${id}`)
      .then(response => {
        console.log("Deleted:", response.data)
      })
      .catch(error => {
        console.error("Error deleting product:", error)
      })
  store.fetchProducts()
}
</script>

<style>
.limited-columns td,
.limited-columns th {
  max-width: 150px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>