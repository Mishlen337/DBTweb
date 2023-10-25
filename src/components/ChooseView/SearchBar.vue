<template>
  <div>
    <b-card-text class="text-center">
      Опишите свою проблему, а ИИ порекомендует специалиста
    </b-card-text>
    <b-input-group size="lg" class="mb-3">
      <b-form-input></b-form-input>
      <b-input-group-append>
        <b-button
          style="background: #B96028"
          size="lg"
          text="Поиск"
          @click="addNewElement"
          >Поиск</b-button
        >
      </b-input-group-append>
    </b-input-group>

    <div v-if="isButtonPushed">
      
    <b-text>Вам нужен когнитивно-поведенческий терапевт</b-text>
    <b-card>
    
    <b-card-title>Рекомендованный специалист</b-card-title>
        <EmployeeInfo
          :fio="em.fio" :specialization="em.specialization"
          :education="em.education"
          :imageSrc="em.imageSrc"
          :workExperience="em.workExperience"
          :appointmentLink="em.appointmentLink">
        </EmployeeInfo>
      
      </b-card>
    </div>
  </div>
</template>


<script>
import EmployeeInfo from "@/components/EmployeesView/EmployeeInfo.vue";

export default {
  name: "SearchBar",
  components: {
    EmployeeInfo,
  },
  data() {
    return {
      isButtonPushed: false,
      em: {
        fio: "Головаха Николай",
        specialization: [
          "К.М.Н.",
          "психотерапевт",
          "когнитивно-поведенческий терапевт",
          "диалектико–поведенческий терапевт",
        ],
        education: [
          "1998 г. - Алтайский государственный медицинский университет по специальности лечебное дело",
          "Ординатура по специальности психиатрия-наркология.",
          "Кандидат медицинских наук.",
          "Сертификат врача психотерапевта",
          "Когнитивно-поведенческая терапия",
          "Диалектическая поведенческая терапия в Behavioral Tech под руководством André Ivanoff, PhD",
          "Участвовал в международных стажировках и конференциях по лечению ожирения, лечению расстройств пищевого поведения, помощи людям с суицидальным поведением и самоповреждениями",
        ],
        workExperience: [
          "Кандидат медицинских наук",
          "Сертификат врача психотерапевта",
        ],
        imageSrc: require("@/assets/employees/Golovaha.jpg"),
        appointmentLink:
          "https://n269840.yclients.com/company/262333/select-services?o=m772221",
      },
    };
  },
  methods: {
    addNewElement() {
      // Add element logic...
      this.isButtonPushed = true;
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