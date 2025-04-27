<template>
  <v-row class="pa-10" justify="center">
    <v-col cols="6">
      <v-expand-transition class='mt-2 mb-2 pa-10'>
        <v-card>
          <v-card-title>Minha cesta <v-icon>mdi-basket</v-icon></v-card-title>
          <v-divider inset></v-divider>
          <v-alert v-if="store.basket.length === 0" type="info">
            Sua cesta está vazia
          </v-alert>
          <div v-else>
            <v-list>
              <v-list-item v-for="(item, id) in store.basket">
                <div> {{ item.title }} - R$ {{ item.price}} - Qtd: {{ item.qtd }}</div>
              </v-list-item>
              <v-list-item>Total: R$ {{ store.basketTotal.toFixed(2) }}</v-list-item>
            </v-list>
          </div>
        </v-card>
      </v-expand-transition>
    </v-col>
  </v-row>
</template>

<script setup>

import { ref, computed } from 'vue'
import { useMyStore} from "@/stores/myStore.js";
const store = useMyStore()


// const totalPrice = computed(() =>
//   basket.value.reduce((sum, item) => sum + item.price * item.qtd, 0)
// )

</script>

<style scoped>

</style>
