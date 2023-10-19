<template>
  <CommonLayout class="text-center">
    <TheHeader/>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" overflow="auto"/> -->
    <MainPage></MainPage>
    <TheFooter/>

  </CommonLayout>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TheHeader from './components/TheHeader.vue';
import TheFooter from './components/TheFooter.vue';
import MainPage from './components/MainPage.vue';


export default {
  name: 'App',
  components: {
    //HelloWorld,
    MainPage,
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
  margin-top: 60px;
}
</style>
