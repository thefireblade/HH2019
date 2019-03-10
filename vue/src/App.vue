<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" fixed right app style="z-index:3">
      <v-list dense>
          <v-list-tile v-for="(route, index) in routes" :key="index" :to="{path: route.link}">
            <v-list-tile-action>
              <v-icon>{{ route.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title> {{ route.title }} </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="primary" dark fixed app style="z-index:2">
      <v-spacer></v-spacer>
      <v-icon>fastfood</v-icon>
      <v-toolbar-title>{{ appTitle }}</v-toolbar-title>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    </v-toolbar>
    <v-content>
      <v-container fluid>
        <v-fade-transition mode="out-in">
          <router-view id="router-view"/>
        </v-fade-transition>
      </v-container>
    </v-content>
    <v-footer color="primary" app>
      <v-spacer></v-spacer>
      <span class="white--text">&copy; Hack Health 2019</span>
      <v-spacer></v-spacer>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",
  components: {
    HelloWorld
  },
  data() {
    return {
      appTitle: 'Chef Wolfie',
      drawer: false,
      routes: [
        {title: 'Home', icon: 'home', link: '/'},
        {title: 'Browse', icon: 'dashboard', link: '/browse'},
        {title: 'Settings', icon: 'settings', link:'/settings'},
        // {title: 'About', icon: 'question_answer', link: '/about'}
      ]
    };
  },
  props: {
    source: String
  }
};
</script>
