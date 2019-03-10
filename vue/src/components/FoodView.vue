<template>
  <v-card>
    <!-- Image -->
    <v-img :src="imageURL" :aspect-ratio="aspectRatio">
      <v-layout align-end fill-height pa-3 white--text>
        <!-- <h1 class="font-weight-light display-1"> Butter Chicken </h1> -->
      </v-layout>
    </v-img>

    <!-- Card Text -->
    <v-card-text class="pt-4" style="position: relative;">

      <!-- Icon to Show -->
      <v-btn
        style="z-index:1"
        absolute
        color="primary"
        class="white--text"
        fab
        medium
        right
        @click="showFoodModal()"
        top>
        <v-icon>restaurant_menu</v-icon>
      </v-btn>

      <!-- Title of The Item -->
      <h3 class="display-1 font-weight-light primary--text mb-2 mt-3"> {{ title() }} </h3>

      <!-- Price and Sub Information -->
      <div class="font-weight-light grey--text title mb-2"> {{ price() }} </div>

      <!-- Food Description -->
      <div class="font-weight-light title mb-2">
        {{data.description}}
      </div>
      
    </v-card-text>
  </v-card>
</template>

<script>
import google_image from 'image-search-google'
import _ from 'lodash'
import { IMAGE_KEY } from "../Config.js";

const IMAGE = new google_image(
  "011896105525757733572:edr33g0rt94",
  "AIzaSyA8SVxkOKnYb0mb7PFWFXeLCkSfDITMapo"
);

// AIzaSyCQ0oHcY-xlAaqfTnTrY34BnpGne2x5bEQ
// AIzaSyCQ2U5YiGWZkn6YyQQfJ9YyLGvvHrgK7Rg
// AIzaSyA8SVxkOKnYb0mb7PFWFXeLCkSfDITMapo 

const options = {page:1}

export default {
  props: ['aspectRatio', 'data'],
  data(){
    return {
      imageURL: ''
    }
  },
  methods: {
    showFoodModal(){
      this.$store.commit('toggleFoodModal');
      this.$store.commit('setCurrentFoodItem', this.data);
    },
    title() {
      return _.startCase(_.toLower(this.data.name));
    },
    price() {
      if(this.data.price == 0){
        return "Buffet Item"
      }else{
        return this.data.price
      }
    }
  },
  mounted(){
    IMAGE.search(this.data.name, options)
      .then((res) => {
        this.imageURL = res[0].url
        this.data.image_url = res[0].url
        console.log(res.length)
    })
  }
}
</script>

