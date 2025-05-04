<template>
  <v-row class="pa-10" justify="center">
    <v-col
      v-for="(item, id) in paginatedProducts"
      :key="id"
      class="d-flex justify-center"
    >
      <v-card width="400px">
        <v-img
          class="bg-grey-lighten-2"
          height="500px"
          :src="item.source"
        ></v-img>
        <v-card-title class="mt-3">
          {{ item.title }} <br/>
          <v-chip>
            {{ item.category }}
          </v-chip>
        </v-card-title>
        <v-card-subtitle>
          {{ item.subtitle }}
        </v-card-subtitle>
        <v-card-text>
        <h2>R$ {{ item.price }}</h2>
        </v-card-text>
        <AddToBasket :item="item" />
      </v-card>
    </v-col>
  </v-row>
  <v-row justify="center">
    <v-pagination
      v-model="currentPage"
      :length="pageCount"
      class="mt-4"
      color="primary"
    />
  </v-row>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useMyStore } from "@/stores/myStore.js"
import AddToBasket from "@/components/AddToBasket.vue";

const store = useMyStore()

// onMounted(() => {
//   console.log(store.products)
// })

const productsPerPage = 8
const currentPage = ref(1)

const pageCount = computed(() =>
  Math.ceil(store.filteredProducts.length / productsPerPage)
)

const paginatedProducts = computed (() => {
    const start = (currentPage.value - 1) * productsPerPage
    const end = start + productsPerPage

    return store.filteredProducts.slice(start, end)
  }
)

</script>
