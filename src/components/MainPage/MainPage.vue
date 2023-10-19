<template>
    <div class="hello">
        <GreetingBlock></GreetingBlock>
        <DiseasesInfo></DiseasesInfo>
        <EmployeesBriefInfo></EmployeesBriefInfo>
        <AppointmentBlock></AppointmentBlock>
    </div>
</template>
  
<script>
import DiseasesInfo from './DiseasesInfo.vue';
import EmployeesBriefInfo from './EmployeesBriefInfo.vue';
import AppointmentBlock from './AppointmentBlock.vue';
import GreetingBlock from './GreetingBlock.vue';

export default {
    name: 'MainPage',
    components: {
    DiseasesInfo,
    EmployeesBriefInfo,
    AppointmentBlock,
    GreetingBlock
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
  