<template>
  <div class="home text-center">
    <GreetingBlock></GreetingBlock>
    <DiseasesInfo></DiseasesInfo>
    <ChooseBlock></ChooseBlock>
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
        v-for="em in employees" :key="em.fio"
        :title="em.fio"
        :image="em.imageSrc"
      >
      </vueper-slide>
    </vueper-slides>

    <AppointmentBlock></AppointmentBlock>
  </div>
</template>

<script>
import { VueperSlide, VueperSlides } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

import DiseasesInfo from "../components/MainView/DiseasesInfo.vue";
// import EmployeesBriefInfo from '../components/MainView/EmployeesBriefInfo.vue';
import AppointmentBlock from "../components/MainView/AppointmentBlock.vue";
import GreetingBlock from "../components/MainView/GreetingBlock.vue";
import ChooseBlock from "@/components/MainView/ChooseBlock.vue";

export default {
  
  name: "HomeView",
  components: {
    VueperSlide, VueperSlides,
    DiseasesInfo,
    // EmployeesBriefInfo,
    AppointmentBlock,
    GreetingBlock,
    ChooseBlock
  },
  data() {
    return {
      employees: [
        {
          fio: "Макарова Яна",
          specialization: [
            "клинический психолог",
            "нейробиолог",
            "когнитивно-поведенческий",
            "диалектико – поведенческий терапевт",
          ],
          education: [
            "2008 - 2013 гг. - РГГУ, Институт психологии им.Л.С.Выготского",
            "2010 г. - Боткинская больница, кафедра нейрохирургии, г. Москва",
            "2012-2013 гг. - Психиатрическая клиническая больница №1 им Н.А. Алексеева, г. Москва",
            "2015 - 2017 гг. - СПбГУ, факультет биологии, специализация 'Нейробиология, психофизиология', г. Санкт - Петербург",
            "2017-2020 гг. - СЗГМУ им. И.И. Мечникова, повышение квалификации по направлениям «Когнитивно-поведенческая терапия», «Когнитивно-поведенческая терапия пар», г. Санкт – Петербург",
            "2021 г. – Центр Когнитивной Терапии, повышение квалификации по направлению «Терапия, сфокусированная на сострадании», г. Москва",
            "2021 г. - Доктор Дуглас Туркингтон (Dr.Douglas Turkington, Royal College of Psychiatrists): 'Когнитивно-поведенческая терапия психозов",
            "с 2021г. - член коллегии Ассоциации клинического психоанализа и психотерапии, участник регулярной интервизионной группы",
          ],
          workExperience: [
            "2013-2015 гг. – Психиатрическая клиническая больница №1 им.Н.А.Алексеева, г. Москва",
            "2015 – 2020 гг. – Психоневрологический диспансер №5 г. Санкт-Петербург",
            "2020 г. – по настоящее время - Частная практика",
          ],
          imageSrc: require("@/assets/employees/Makarova.jpg"),
          appointmentLink:
            "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        },
        {
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
        {
          fio: "Mariia Aarseth",
          specialization: [
            "Клинический психолог",
            "преподаватель",
            "психологии",
          ],
          education: [
            "2009 г - Санкт-Петербургский институт гуманитарного образования, специальность - психолог",
            "2020 г - Санкт-Петербургский Межотраслевой Институт Повышения Квалификации, специальность - Клиническая психология",
          ],
          workExperience: [
            "EMDR терапевт с Европейской аккредитацией ( как взрослый, так и детский ), супервизор.",
            "Член ассоциаций Норвегия, Россия, Казахстан.",
            "TFP ( терапия сфокусированная на переносе Columbia University Weill Cornell Medical CollegeOtto Friedmann Kernberg",
            "Обучение в Heidelberg University Germany. Martin Bohus, а так же Universitetet i Oslo Lars Mehlum. DBT, DBT PTSD, CFT",
          ],
          imageSrc: require("@/assets/employees/Aarseth.jpg"),
          appointmentLink:
            "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        },
      ],
    };
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
