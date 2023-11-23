<template>
  <div>
    <b-card class="card-outter">
      <img
        :src="'data:image/gif;base64,' + imageSrc"
        class="card-img card-img-top img-fluid"
      />
      <b-card-text>
        {{ description }}
      </b-card-text>
    </b-card>
  </div>
</template>


<script>
export default {
  name: "DiseaseInfo",
  props: ["description", "imageSrc"],
};
</script>
