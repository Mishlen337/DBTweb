<template>
<CommonLayout>
  <TheHeader/>
  <!-- <HomeView></HomeView> -->
  <TheFooter/>
</CommonLayout>
</template>

<script>
// import HomeView from './views/HomeView.vue';
import TheHeader from './components/TheHeader.vue';
import TheFooter from './components/TheFooter.vue';

export default {
  components: {
    // HomeView,
    TheHeader,
    TheFooter
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
