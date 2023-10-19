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
            <img src="@/assets/main_content.gif"  class="card-img-top img-fluid">
        </b-card>
    <div class="container">
        <b-card-title>
            <b-icon icon="circle-fill" animation="throb"></b-icon> 
            Работаем онлайн в Европе и по всему миру
            <b-icon icon="circle-fill" animation="throb"></b-icon>
    </b-card-title> 
   
    <b-text>Проект ориентирован на помощь русскоговорящим людям страдающим ПРЛ</b-text>
    <img src="@/assets/planet.gif"  class="card-img-top img-fluid">
    </div>    
    </div>
</template>

<script>

export default {
    name: 'GreetingBlock',
}
</script>
<style scoped>
.container {
  min-height: calc(100vh - 0px);
  justify-content: center;

}
</style>