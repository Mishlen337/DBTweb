<template>
  <div class="home text-center">
    <GreetingBlock></GreetingBlock>

    <!-- Diseases -->
    <b-card-title>
      Критерии пограничного расстройства личности (ПРЛ)
    </b-card-title>
    <div class="row">
      <b-card-group class="col-md-4" v-for="des in diseases" :key="des.description">
        <DiseaseInfo
          :description="des.description"
          :imageSrc="des.imageSrc">
        </DiseaseInfo>
      </b-card-group>
    </div>
    <!-- ----------------- -->

    <ChooseBlock></ChooseBlock>
    
    <!-- Popular employees -->
    <b-card-title>
      Наши специалисты
    </b-card-title>
    <vueper-slides
      class="no-shadow text-center"
      arrows-outside
      bullets-outside
      prevent-y-scroll
      transition-speed="250"
      slide-content-outside="top"
      autoplay
      :slide-ratio="1 / 1"
      :dragging-distance="100"
    >
      <vueper-slide
        v-for="em in popularEmployees" :key="em.fio"
        :title="em.fio"
        :content="em.specialization.toString()"
        :image="'data:image/gif;base64,'+ em.imageSrc"
        :link="em.appointmentLink"
      >
      </vueper-slide>
    </vueper-slides>
    <!-- ----------------- -->

    <AppointmentBlock></AppointmentBlock>
  </div>
</template>

<script>
import { VueperSlide, VueperSlides } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import axios from 'axios';

import DiseaseInfo from "../components/MainView/DiseaseInfo.vue";
import AppointmentBlock from "../components/MainView/AppointmentBlock.vue";
import GreetingBlock from "../components/MainView/GreetingBlock.vue";
import ChooseBlock from "@/components/MainView/ChooseBlock.vue";

export default {
  name: "HomeView",
  components: {
    VueperSlide, VueperSlides,
    DiseaseInfo,
    // EmployeesBriefInfo,
    AppointmentBlock,
    GreetingBlock,
    ChooseBlock
  },
  data() {
        return {
            employees: null,
            diseases: null
        };
    },
  mounted() {
        axios
        .get('/employees')
        .then(response => (this.employees = response.data.employees))
        .catch(error => console.log(error));
        axios
        .get('/diseases')
        .then(response => (this.diseases = response.data.diseases))
        .catch(error => console.log(error));
  },
  computed: {
    popularEmployees() {
      return this.employees.filter(item => item.isPopular);
    },
  },
};
</script>


<style scoped>
/* Solution using `transform: translate`: */
.imageParent img {
  position: absolute;
  top: 80%;
  left: 80%;
  transform: translate(-80%, -80%);
}
.no-shadow {
  max-width: 50%;
  max-height: 50%;
  margin: auto;
}
</style>
