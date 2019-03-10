<template>
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>

      <!-- Toolbar Setup -->
      <v-toolbar card dark color="primary">
        <v-btn icon dark @click="$store.commit(toggle)">
          <v-icon>close</v-icon>
        </v-btn>
        <v-toolbar-title> Nutritional Information </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn dark flat @click="$store.commit(toggle)">Save</v-btn>
        </v-toolbar-items>
        <v-menu bottom right offset-y>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on">
              <v-icon>more_vert</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-tile v-for="(item, i) in items" :key="i" @click="">
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-toolbar>

      <!-- Main Content -->
      <v-card-text>
        
        <v-layout row wrap justify-left ma-5>
          <v-img :src="data.image_url" max-width="500"></v-img>

          <v-flex> 
            <h2 class="display-2 font-weight-light black--text mb-4 mt-2 mx-5"> {{ title() }} </h2>
            <v-divider class="mx-5"/>

            <v-flex mx-5 mt-3>
              <h2 
                v-for="(info, index) in nutritionInformation" :key="index"
                class="font-weight-light headline"
                mx-5
              > 
                {{ info.name }}: {{info.value}} {{info.type}} 
                
              </h2>
            </v-flex>


          </v-flex>


        </v-layout>
        <v-divider></v-divider>

      </v-card-text>

      <div style="flex: 1 1 auto;"></div>
    </v-card>
  </v-dialog>
</template>

<script>
import _ from 'lodash'
import setImmediate from 'setimmediate'

export default {
  props: ['show', 'toggle'],
  data(){
    return {
      items: ['Show', 'Delete'],
    }

  },
  computed: {
    data(){
      return this.$store.state.food_data.currentFoodItem
    },
    
    nutritionInformation(){
      
      const current = this.$store.state.food_data.currentFoodItem.rounded_nutrition_info;
      if(!current) return []
      return [
        {name: "Calories", type: 'calories', value: current.calories},
        {name: 'Carbohydrates', type: 'g', value: current.g_carbs},
        {name: "Fat", type: 'g', value: current.g_fat},
        {name: "Fiber", type: 'g', value: current.g_fiber},
        {name: "Protein", type: 'g', value: current.g_protein},
        {name: "Saturated Fat", type: 'g', value: current.g_saturated_fat},
        {name: "Sugar", type: 'g', value: current.g_sugar},
        {name: "Trans Fat", type: 'g', value: current.g_trans_fat},
        {name: "Vitamin A", type: '', value: current.iu_vitamin_a},
        {name: "Calcium", type:'mg', value: current.mg_calcium},
        {name: "Cholesterol", type:'mg', value: current.mg_cholesterol},
        {name: "Iron", type:'mg', value: current.mg_iron},
        {name: "Potassium", type:'mg', value: current.mg_potassium},
        {name: "Sodium", type:'mg', value: current.mg_sodium},
        {name: "Vitamin C", type:'mg', value: current.mg_vitamin_c},
        {name: "Vitamin D", type:'mg', value: current.mg_vitamin_d},
        {name: "Vitamin A", type: '', value: current.re_vitamin_a}

      ]
    }
  },
  methods:{
    title() {
      return _.startCase(_.toLower(this.data.name));
    }
  }
}
</script>
