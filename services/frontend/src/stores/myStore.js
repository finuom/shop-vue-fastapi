import { defineStore } from 'pinia';
import axios from 'axios'

export const useMyStore = defineStore('myStore', {
  state: () => ({
    basket: [],
    items: [],
    loading: false,
    error: null,
    search: '',
    selectedCategories: []
  }),

  getters: {
    basketTotal: (state) => {
      return state.basket.reduce((sum, item) => sum + item.price * item.qtd, 0)
    },
    basketCount: (state) => {
      let n_items = 0
      for (let i = 0; i < state.basket.length; i++) {
        n_items += state.basket[i].qtd
      }
      return n_items
    },
    filteredItems: (state) => {
      if (!Array.isArray(state.items)) {
        return []
      }
      return state.items.filter(item => {
        const matchesCategory = state.selectedCategories.length === 0 ||
                                state.selectedCategories.includes('todas') ||
                                state.selectedCategories.includes(item.category.toLowerCase())

        const matchesSearch = !state.search ||
                                      item.title.toLowerCase().includes(state.search.toLowerCase())
        return matchesCategory && matchesSearch
      })
    }
  },

  actions: {
    addToBasket(item, qtd) {
      // console.log('id:', id)
      // const item = this.items.find(item => item.id === id)
      // if (!item) return

      const alreadyInbasket = this.basket.some(basketItem => basketItem.title === item.title)
      if (!alreadyInbasket) this.basket.push(item)

      item.qtd += qtd
    },
    setSearch(query) {
      this.search = query
    },
    async fetchItems() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get('http://127.0.0.1:8500/items/') // use your actual endpoint
        // For postgres
        this.items = response.data
        // For mySql
        this.items = response.data.items
      } catch (err) {
        this.error = 'Failed to fetch items'
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  },
});
