<template>
  <v-container fluid px-1 grid-list-sm>

    <food-detail :show="showFoodModal" :toggle=" 'toggleFoodModal' "></food-detail>
    <loading :show="showLoading" :toggle=" 'toggleLoader' "/>

      <!-- Select A Location -->
      <div v-if="!selectedLocation">
        <v-layout row wrap justify-space-around>
          <v-flex xs6 v-for="(image, index) in images" :key="index" @click="choseLocation(image)">
          <card-view class="location" :image="image" aspect-ratio="2.55"></card-view>
          </v-flex>
        </v-layout>
      </div>

      <div v-if="selectedLocation">

        <!-- Sort -->
        <v-flex d-flex>
          <v-btn color="error" @click="changeLocation()">Back</v-btn>
          <v-spacer></v-spacer>
          <v-select
            :items="sort"
            label="Sort By"
          ></v-select>
          <v-spacer></v-spacer>
          <v-select
            :items="size"
            label="Sort Type"
          ></v-select>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="amount"
            label="Amount"
          ></v-text-field>

          <v-btn color="success" @click="performSort()">Sort</v-btn>

          <v-btn color="success" @click="$store.dispatch('getData')">Get All Food</v-btn>
          <v-btn color="success" @click="getFoodPage()">Get Food Page</v-btn>
        </v-flex>
        

        <!-- Food View -->
        <v-layout row wrap justify-center ma-5>
          <v-flex xs3 v-for="(item, index) in foods" :key="index" pa-2>
          <food-view :data="item" aspect-ratio="2.1"></food-view>
          </v-flex>
        </v-layout>
      </div>



  </v-container>
</template>

<style scoped>
  .location {
    cursor: pointer;
  }
</style>

<script>
import CardView from '../components/CardView'
import {locations} from '../Locations.js'
import FoodView from '../components/FoodView'
import FoodDetail from '../components/FoodViewDetailModal'
import Loading from '../components/Loading'
import { match } from 'minimatch';

export default {
  components: {
    FoodDetail,
    CardView,
    FoodView,
    Loading

  },
  data(){
    return {
      images: locations,
      foods: [],
      sort: ['Calories', 'Price', 'Carbs', 'Protein'],
      size: ['Greater Than', 'Less Than or Equal To'],
      sortURLs: [''],
      amount: 10
    }
  },
  methods: {
    getFoodPage(){
      this.foods = this.$store.getters.getItemsPage(0);
    },
    choseLocation(location){
      this.$store.commit('setURL', location.url)
      this.$store.commit('toggleSelectedLocation')
      this.$store.dispatch('getData')
    },
    changeLocation(){
      this.$store.commit('toggleSelectedLocation')
      this.$store.commit('resetData')
    },
    performSort(){
      this.$store.dispatch('sortBy', {less_than: false, field: 'price', amount: this.amount })
    }
  },
  computed: {
    showFoodModal(){
      return this.$store.state.views.showFoodModal
    },
    showLoading(){
      return this.$store.state.views.showLoader
    },
    foodData(){
      return this.$store.state.food_data.food_items
    },
    selectedLocation(){
      return this.$store.state.views.selectedLocation
    }
  },
  mounted() {
  }

}
</script>
