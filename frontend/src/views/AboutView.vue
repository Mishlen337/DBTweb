<template>
  <div class="about">
    <div class="p-5 text-center bg-image">
      <b-card-title>Мы - команда дбт специалистов</b-card-title>
    </div>
    <div class="grid-2cols">
      <div class="iconcontainer first">
        <v-card>
          <img
            class="img-fluid"
            src="@/assets/about_content/team.jpg"
            alt="image slot"
          />
        </v-card>
      </div>
      <div class="iconcontainer second">
        <BasicInfoBlock></BasicInfoBlock>
        <ValuesBlock></ValuesBlock>
        <MotivationBlock></MotivationBlock>
      </div>
    </div>
  </div>
</template>

<script>
import BasicInfoBlock from "@/components/AboutView/BasicInfoBlock.vue";
import ValuesBlock from "@/components/AboutView/ValuesBlock.vue";
import MotivationBlock from "@/components/AboutView/MotivationBlock.vue";

export default {
  name: "AboutView",
  components: {
    BasicInfoBlock,
    ValuesBlock,
    MotivationBlock,
  },
};
</script>
<style scoped>
@media not (max-width: 1000px) {
  div.grid-2cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
  }
  .iconcontainer.first,
  .iconcontainer.second {
    display: block;
    width: 100%;
    height: 100%;
  }
  .iconcontainer.first {
    height: fit-content;
  }
}
</style>

