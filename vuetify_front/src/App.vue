<template>
  <v-app>
    <v-main>
      <SearchBar/>
    </v-main>
  </v-app>
</template>

<script>
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',

  components: {
    SearchBar,
  },  

  data: () => ({
    //
  }),
}
</script>
