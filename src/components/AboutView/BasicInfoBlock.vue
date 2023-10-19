<template>
    <div>
        <div class="p-5 text-center bg-image">
            <b-card-title>Мы - команда дбт специалистов</b-card-title>
        </div>
        <div>
            <v-card>
                <img class="ImageParent img-fluid" src="@/assets/about_content/team.jpg" alt="image slot">
            </v-card>
        </div>
        <b-card-title class="text-center">О нас:</b-card-title>
        <b-card>
            Прошли обучение в Deutsche Arbeitsgemeinschaft Dialektisch Behaviorale
            Therapie DAGDBT, под руководством Prof. Dr. Martin Bohus
        </b-card>
        <b-card>
            Мы живём в разных странах, но объединились, в один проект, чтобы изучать и практиковать диалетичекую
            поведенческую терапию (DBT) и оказывать помощь людям с пограничным расстройством личности (ПРЛ).
        </b-card>
    </div>
</template>

<script>

export default {
    name: 'BasicInfoBlock',
}
</script>
<style>

.imageParent img {
    position: absolute;
    top: 80%;
    left: 80%;
    transform: translate(-80%, -80%);
}

</style>