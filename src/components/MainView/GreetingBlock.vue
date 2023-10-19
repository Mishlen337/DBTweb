<template>
    <div>
        <b-card-title>
            <div class="p-5 text-center bg-image">
                Команда специалистов диалектическая поведенческой терапии
            </div>
        </b-card-title>
        <b-card>
            <p>
                Прошедших обучение в Deutsche Arbeitsgemeinschaft Dialektisch Behaviorale Therapie DAGDBT
            </p>
            <p>
                под руководством Prof. Dr. Martin Bohus
            </p>
            <div>
                <v-card>
                    <img class="ImageParent img-fluid" src="@/assets/main_content.gif" alt="image slot">
                </v-card>
            </div>
        </b-card>
        <div class="container">
            <b-card-title>
                <b-icon icon="circle-fill" animation="throb"></b-icon>
                Работаем онлайн в Европе и по всему миру
                <b-icon icon="circle-fill" animation="throb"></b-icon>
            </b-card-title>

            <b-text>Проект ориентирован на помощь русскоговорящим людям страдающим ПРЛ</b-text>
            <div>
                <v-card>
                    <img class="ImageParent img-fluid" src="@/assets/planet.gif" alt="image slot">
                </v-card>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'GreetingBlock',
}
</script>
<style scoped>
/* .container {
  min-height: calc(100vh - 0px);
  justify-content: center;

} */
.imageParent img {
    position: absolute;
    top: 80%;
    left: 80%;
    transform: translate(-80%, -80%);
}
</style>