<template>
  <div>
    <b-card-text class="text-center">
      Опишите свою проблему, а ИИ порекомендует специалиста
    </b-card-text>
    <b-input-group size="lg" class="mb-3">
      <b-form-input id="ProblemText"></b-form-input>
      <b-input-group-append>
        <b-button
          style="background: #b96028"
          size="lg"
          text="Поиск"
          @click="getRecommendation"
          >Поиск</b-button
        >
      </b-input-group-append>
    </b-input-group>
    
    <div v-if="notFoundMessage">
      <b-text>{{ notFoundMessage }}</b-text>
    </div>
    <div v-if="employee">
      <b-text>Предположительно у вас: {{ recommendedSpecialization }}</b-text>
      <b-card>
        <b-card-title>Рекомендованный специалист</b-card-title>
        <EmployeeInfo
          :fio="employee.fio"
          :specialization="employee.specialization"
          :education="employee.education"
          :imageSrc="employee.imageSrc"
          :workExperience="employee.workExperience"
          :appointmentLink="employee.appointmentLink"
        >
        </EmployeeInfo>
      </b-card>
    </div>
  </div>
</template>


<script>
import EmployeeInfo from "@/components/EmployeesView/EmployeeInfo.vue";
import axios from "axios";

export default {
  name: "SearchBar",
  components: {
    EmployeeInfo,
  },
  data() {
    return {
      employee: null,
      recommendedSpecialization: null,
      notFoundMessage: null
    };
  },
  methods: {
    getRecommendation() {
      axios
        .get("/recommendation", {
          params: {
            problem: document.getElementById("ProblemText").value,
          },
        })
        .then((response) => {
          this.employee = response.data.employee;
          this.recommendedSpecialization = response.data.recommendedSpecialization;
          this.notFoundMessage = null
        }
          )
          .catch((error) => {
            // Check if the error response status is 404
            if (error.response && error.response.status === 404) {
              // Update the UI or state to show a custom message
              this.notFoundMessage = 'Не можем найти подходящего специалиста, подберите его самостоятельно';
              this.employee = null
              this.recommendedSpecialization = null

            } else {
              // Handle other types of errors or log them
              console.log(error);
            }
          });
    },
  },
};
</script>

<style scoped>
.card {
  margin: 0 auto; /* Added */
  float: none; /* Added */
  margin-bottom: 10px; /* Added */
}
</style>