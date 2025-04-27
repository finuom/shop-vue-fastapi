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
      return state.items.filter(item => {
        const matchesCategory = state.selectedCategories.length === 0 ||
                                state.selectedCategories.includes('todas') ||
                                state.selectedCategories.includes(item.category.toLowerCase())

        const matchesSearch = !state.search ||
                                      item.title.toLowerCase().includes(state.search.toLowerCase())
        return matchesCategory && matchesSearch
      });
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
        const response = await axios.get('http://127.0.0.1:8001/items/') // use your actual endpoint
        this.items = response.data
      } catch (err) {
        this.error = 'Failed to fetch items'
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  },
});
