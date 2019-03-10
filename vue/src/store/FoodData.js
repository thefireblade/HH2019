import API from "../Util/API";
import { URLs } from "../Config";

export default {
  state: {
    food_items: [],
    currentFoodItem: {},
    locationURL: URLs.API_BASE_URL + URLs.ALL_ITEMS
  },
  getters: {
    getItemsPage: state => index => {
      const itemsPerPage = 30;
      const i = index * itemsPerPage;
      const j = i + itemsPerPage;
      console.log(state.food_items[0].name);
      return state.food_items.slice(i, j);
    }
  },
  mutations: {
    initializeFoodData(state, new_data) {
      state.food_items = new_data;
    },
    setCurrentFoodItem(state, data) {
      state.currentFoodItem = data;
    },
    setURL(state, url) {
      state.locationURL = URLs.API_BASE_URL + url;
    },
    resetData(state) {
      state.food_items = [];
    }
  },
  actions: {
    getData({ state, commit }) {
      // dispatch("toggleLoader");
      // commit("toggleLoader", null, { root: true });

      // API.getAllFood(response => {
      //   commit("initializeFoodData", response);
      //   console.log(response.length);
      //   commit("toggleLoader", null, { root: true });
      // });

      commit("toggleLoader", null, { root: true });
      API.getFood(state.locationURL, response => {
        commit("initializeFoodData", response);
        console.log(response.length);
        commit("toggleLoader", null, { root: true });
      });
    },
    sortBy({ state, commit }, { less_than, field, amount }) {
      commit("toggleLoader", null, { root: true });
      API.sortBy(less_than, field, amount, data => {
        commit("initializeFoodData", data);
        commit("toggleLoader", null, { root: true });
      });
    }
  }
};
