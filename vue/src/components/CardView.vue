<template>
  <v-card>
    <v-img :src="image.src" :aspect-ratio="aspectRatio">
      <v-layout align-end fill-height pa-3 white--text>
        <h1 class="font-weight-light display-2"> {{image.title }} </h1>
      </v-layout>
    </v-img>
  </v-card>
</template>

<script>
export default {
  props: ['image', 'aspect-ratio']
}
</script>

<style scoped>

  .bottom-gradient {
    background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 72px);
  }

</style>


