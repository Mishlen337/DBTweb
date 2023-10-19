<template>
  <div class="home text-center">
      <GreetingBlock></GreetingBlock>
      <DiseasesInfo></DiseasesInfo>
      <EmployeesBriefInfo></EmployeesBriefInfo>
      <AppointmentBlock></AppointmentBlock>
  </div>
</template>

<script>
import DiseasesInfo from '../components/MainView/DiseasesInfo.vue';
import EmployeesBriefInfo from '../components/MainView/EmployeesBriefInfo.vue';
import AppointmentBlock from '../components/MainView/AppointmentBlock.vue';
import GreetingBlock from '../components/MainView/GreetingBlock.vue';


export default {
  name: 'HomeView',
  components: {
  DiseasesInfo,
  EmployeesBriefInfo,
  AppointmentBlock,
  GreetingBlock,
  }
}

</script>

<style scoped>
/* Solution using `transform: translate`: */
.imageParent img {
  position: absolute;
  top: 80%;
  left: 80%;
  transform: translate(-80%, -80%);
}
</style>
