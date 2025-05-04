<template>
  <v-app>
    <v-app-bar app color="primary" dark>

      <div class="d-flex align-center">
        <v-toolbar-title class="ml-4 mr-4 text-truncate" style="max-width: 300px">Loja de Chapéus 🤠</v-toolbar-title>
      </div>

      <div class="d-flex align-center justify-center" style="flex: 1; min-width: 0;">
        <v-text-field
            v-model="store.search"
            label="Search products"
            prepend-inner-icon="mdi-magnify"
            clearable
            hide-details
            density="comfortable"
            style="min-width: 300px; max-width: 900px;"
        ></v-text-field>
        <v-combobox
          v-model="store.selectedCategories"
          v-model:search="searchCategories"
          :hide-no-data="false"
          :items="categories"
          label="Add some tags"
          chips
          hide-selected
          hide-details
          density="comfortable"
          multiple
          persistent-hint
          style="min-width: 300px; max-width: 900px;"
          class="ml-4"
        >
          <template v-slot:no-data>
            <v-list-item>
              <v-list-item-title>
                No results matching "<strong>{{ search }}</strong>". Press <kbd>enter</kbd> to create a new one
              </v-list-item-title>
            </v-list-item>
          </template>
        </v-combobox>
      </div>

      <div class="d-flex align-center ml-4 mr-4">
        <v-badge
            :content="store.basketCount"
            color="red"
            overlap
            :model-value="store.basketCount > 0"
        >
          <v-btn icon @click="goToBasket">
            <v-icon>mdi-basket</v-icon>
          </v-btn>
        </v-badge>

        <v-btn icon @click="goToCatalog">
          <v-icon>mdi-store</v-icon>
        </v-btn>

        <v-btn icon @click="goToAccount">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </div>

    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { useMyStore } from "@/stores/myStore.js"
  import {useRouter} from 'vue-router'

  import { nextTick, ref, watch } from 'vue'

  const categories = ['todas', 'masculino', 'feminino', 'unissex', 'infantil']

  const searchCategories = ref(null)

  // watch(store.selectedCategories, val => {
  //   if (val.length > 5) {
  //     nextTick(() => store.selectedCategories.pop())
  //   }
  // })

  const store = useMyStore()
  const router = useRouter()

  function goToCatalog() {
    router.push('/')
  }

  function goToBasket() {
    router.push('/cesta')
  }

  function goToAccount() {
    router.push('/account')
  }

  onMounted(() => {
    store.fetchProducts()
  })
</script>
