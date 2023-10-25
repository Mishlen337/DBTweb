
<template>
  <b-card class="card-outter">
    <b-text class="text-center"> 👨🏼‍🏫 Автор: {{ author }} </b-text>
    <img :src="imageSrc" class="card-img card-img-top img-fluid" />
    <b-card-title>{{ title }}</b-card-title>
    <b-text>
      {{ description }}
    </b-text>
    <div class="card-actions">
      <b-button :href="articleLink" style="background: #B96028">⚡️ Читать ⚡️</b-button>
    </div>
  </b-card>
</template>
<script>

export default {
  name: "EmployeeInfo",
  props: ["title", "author", "description", "imageSrc", "articleLink"],
  // data() {
  //     return {
  //         imageSrc: require('@/assets/employees/Makarova.jpg')
  //     };
  // }
};
</script>

<style scoped>
.card-actions {
  position: absolute;
  bottom: 0;
}
.card-outter {
  position: relative;
  padding-bottom: 50px;
}
</style>
