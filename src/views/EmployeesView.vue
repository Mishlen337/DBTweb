<template>
    <div class="employess">
        <div class="p-5 text-center bg-image">
            <b-card-title>Cпециалисты</b-card-title>
        </div>
        <div class="row">
            <b-card-group class="col-md-5" v-for="em in employees" :key="em.fio">
                <EmployeeInfo :fio="em.fio" :specialization="em.specialization" :education="em.education" :imageSrc="em.imageSrc"
                    :workExperience="em.workExperience" :appointmentLink="em.appointmentLink"> </EmployeeInfo>
            </b-card-group>
        </div>
    </div>
</template>
  
<script>
import EmployeeInfo from '@/components/EmployeesView/EmployeeInfo.vue'

export default {
    name: 'EmployeesView',
    components: {
        EmployeeInfo
    },
    data() {
        return {
            employees: [{
                fio: "Макарова Яна",
                specialization: [
                    "клинический психолог",
                    "нейробиолог",
                    "когнитивно-поведенческий",
                    "диалектико – поведенческий терапевт"
                ],
                education: ["2008 - 2013 гг. - РГГУ, Институт психологии им.Л.С.Выготского",
                    "2010 г. - Боткинская больница, кафедра нейрохирургии, г. Москва",
                    "2012-2013 гг. - Психиатрическая клиническая больница №1 им Н.А. Алексеева, г. Москва",
                    "2015 - 2017 гг. - СПбГУ, факультет биологии, специализация 'Нейробиология, психофизиология', г. Санкт - Петербург",
                    "2017-2020 гг. - СЗГМУ им. И.И. Мечникова, повышение квалификации по направлениям «Когнитивно-поведенческая терапия», «Когнитивно-поведенческая терапия пар», г. Санкт – Петербург",
                    "2021 г. – Центр Когнитивной Терапии, повышение квалификации по направлению «Терапия, сфокусированная на сострадании», г. Москва",
                    "2021 г. - Доктор Дуглас Туркингтон (Dr.Douglas Turkington, Royal College of Psychiatrists): 'Когнитивно-поведенческая терапия психозов",
                    "с 2021г. - член коллегии Ассоциации клинического психоанализа и психотерапии, участник регулярной интервизионной группы"],
                workExperience: ["2013-2015 гг. – Психиатрическая клиническая больница №1 им.Н.А.Алексеева, г. Москва",
                    "2015 – 2020 гг. – Психоневрологический диспансер №5 г. Санкт-Петербург",
                    "2020 г. – по настоящее время - Частная практика"],
                imageSrc: require('@/assets/employees/Makarova.jpg'),
                appointmentLink: "https://n269840.yclients.com/company/262333/select-services?o=m772221"
            },
            {
                fio: "Головаха Николай",
                specialization: ["К.М.Н.", "психотерапевт", "когнитивно-поведенческий терапевт", "диалектико–поведенческий терапевт"],
                education: ["1998 г. - Алтайский государственный медицинский университет по специальности лечебное дело",
                    "Ординатура по специальности психиатрия-наркология.", "Кандидат медицинских наук.", "Сертификат врача психотерапевта", "Когнитивно-поведенческая терапия",
                    "Диалектическая поведенческая терапия в Behavioral Tech под руководством André Ivanoff, PhD", "Участвовал в международных стажировках и конференциях по лечению ожирения, лечению расстройств пищевого поведения, помощи людям с суицидальным поведением и самоповреждениями"],
                workExperience: ["Кандидат медицинских наук", "Сертификат врача психотерапевта"],
                imageSrc: require('@/assets/employees/Golovaha.jpg'),
                appointmentLink: "https://n269840.yclients.com/company/262333/select-services?o=m772221"
            },
            {
                fio: "Mariia Aarseth",
                specialization: ["Клинический психолог", "преподаватель", "психологии"],
                education: ["2009 г - Санкт-Петербургский институт гуманитарного образования, специальность - психолог",
                    "2020 г - Санкт-Петербургский Межотраслевой Институт Повышения Квалификации, специальность - Клиническая психология"],
                workExperience: ["EMDR терапевт с Европейской аккредитацией ( как взрослый, так и детский ), супервизор.", "Член ассоциаций Норвегия, Россия, Казахстан.", "TFP ( терапия сфокусированная на переносе Columbia University Weill Cornell Medical CollegeOtto Friedmann Kernberg", "Обучение в Heidelberg University Germany. Martin Bohus, а так же Universitetet i Oslo Lars Mehlum. DBT, DBT PTSD, CFT"],
                imageSrc: require('@/assets/employees/Aarseth.jpg'),
                appointmentLink: "https://n269840.yclients.com/company/262333/select-services?o=m772221"
            }
            ]
        };
    }
}
</script>
<style scoped>
/* .card-deck .card {
    max-width: calc(25% - 30px);
} */
</style>