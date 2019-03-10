import Vue from "vue";
import Vuex from "vuex";
import views from "./store/ViewState";
import food_data from './store/FoodData';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    views,
    food_data
  }
});
