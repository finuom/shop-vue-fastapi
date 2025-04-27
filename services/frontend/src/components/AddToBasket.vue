<template>
  <div class="d-flex align-center ga-2">
  <v-btn icon @click="decrease" :disabled="quantity <= 1" size="small" color="primary">
    <v-icon>mdi-minus</v-icon>
  </v-btn>
  <v-text-field
    v-model.number="quantity"
    type="number"
    min="1"
    density="compact"
    hide-details
    style="width: 60px"
  />
  <v-btn icon @click="increase" size="small" color="primary">
    <v-icon>mdi-plus</v-icon>
  </v-btn>
  <v-btn color="primary"
         prepend-icon="mdi-basket-plus"
         @click="addItem(item.id)"
         v-bind:disabled="quantity <= 0">
    Add
  </v-btn>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMyStore } from '@/stores/myStore'

const props = defineProps({
  item: Object
})

const store = useMyStore()
const quantity = ref(1)

const increase = () => {
  quantity.value++
}

const decrease = () => {
  if (quantity.value > 1) {
    quantity.value--
  }
}

const addItem = () => {
  store.addToBasket(props.item, quantity.value)
  quantity.value = 1
}
</script>

<style scoped lang="sass">

</style>
