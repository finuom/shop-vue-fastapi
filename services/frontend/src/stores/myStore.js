import { defineStore } from 'pinia';
import axios from 'axios'

export const useMyStore = defineStore('myStore', {
  state: () => ({
    basket: [],
    products: [],
    loading: false,
    error: null,
    search: '',
    selectedCategories: [],
    users: [
      { id: 1, user: 'admin', password: 123 }
    ],
  }),

  getters: {
    basketTotal: (state) => {
      return state.basket.reduce((sum, item) => sum + item.price * item.qtd, 0)
    },
    basketCount: (state) => {
      let n_products = 0
      for (let i = 0; i < state.basket.length; i++) {
        n_products += state.basket[i].qtd
      }
      return n_products
    },
    filteredProducts: (state) => {
      if (!Array.isArray(state.products)) {
        return []
      }
      return state.products.filter(item => {
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
      // const item = this.products.find(item => item.id === id)
      // if (!item) return

      const alreadyInbasket = this.basket.some(basketItem => basketItem.title === item.title)
      if (!alreadyInbasket) this.basket.push(item)

      item.qtd += qtd
    },
    setSearch(query) {
      this.search = query
    },
    async fetchProducts() {
      this.loading = true
      this.error = null
      try {
        const response = await axios.get('http://127.0.0.1:8500/products/') // use your actual endpoint
        // For postgres
        this.products = response.data
      } catch (err) {
        this.error = 'Failed to fetch products'
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  },
});
