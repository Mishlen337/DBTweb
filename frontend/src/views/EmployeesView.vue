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
import axios from 'axios';

export default {
    name: 'EmployeesView',
    components: {
        EmployeeInfo
    },
    data() {
        return {
            employees: null
        };
    },
    mounted() {
        axios
        .get('/employees')
        .then(response => (this.employees = response.data.employees))
        .catch(error => console.log(error));
    },
}
</script>


<style scoped>
.card-group {
        margin: 0 auto; /* Added */
        float: none; /* Added */
        margin-bottom: 10px; /* Added */
}
</style>