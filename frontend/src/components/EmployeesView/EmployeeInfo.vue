
<template>
    <b-card class="card-outter">
        <b-card-title class="text-center">{{ fio }}</b-card-title>
        <img :src="'data:image/gif;base64,'+ imageSrc" class="card-img card-img-top img-fluid"/>
        <b-text>
            <div class="text-center"> <b>👨🏻‍🎓 Специализация:</b></div>
            <li v-for="item in specialization" :key="item">
                {{ item }}
            </li>
            <div class="text-center"> <b>📚 Образование:</b></div>
            <li v-for="item in education" :key="item">
                {{ item }}
            </li>
            <div class="text-center"> <b>🔎 Опыт работы: </b></div>
            <li v-for="item in workExperience" :key="item">
                {{ item }}
            </li>
        </b-text>
        <div class="card-actions mw-100">
            <b-button :href="appointmentLink" style="background: #B96028">Запись на прием</b-button>
        </div>
    </b-card>
</template>
<script>

export default ({
    name: "EmployeeInfo",
    props: ["fio", "education", "imageSrc", "workExperience", "specialization", "appointmentLink"],
    // data() {
    //     return {
    //         imageSrc: require('@/assets/employees/Makarova.jpg')
    //     };
    // }

})
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
