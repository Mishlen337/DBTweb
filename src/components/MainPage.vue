<template>
    <div class="hello">
        <div class="container">
        <b-card-title>
            Команда специалистов диалектическая поведенческой терапии
        </b-card-title>

        <b-card> <img src="../assets/main_content-removebg-preview.png" class=" card-img-top img-fluid">
            <p>
                Deutsche Arbeitsgemeinschaft Dialektisch Behaviorale Therapie DAGDBT
            </p>
        </b-card>
    </div>

        <!--Ilnesses-->
        <b-card-title>
            Критерии пограничного расстройства личности (ПРЛ)
        </b-card-title>
        <div>
            <div class="mt-3">
                <b-card-group deck>
                    <b-card>
                        <img src="../assets/main_content/prl1.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text>
                            Отчаянные попытки предотвратить реальное или воображаемое одиночество
                        </b-card-text>


                    </b-card>

                    <b-card>
                        <img src="../assets/main_content/prl2.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text>
                            Повторяющиеся нестабильные и интенсивные межличностные отношения, характеризующийся чередованием
                            крайней
                            идеализации и обесценивания
                        </b-card-text>
                    </b-card>
                    <b-card>
                        <img src="../assets/main_content/prl3.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Временные параноидальные идеи, связанные со стрессом, или тяжелые диссоциативные
                            симптомы.
                        </b-card-text>
                    </b-card>
                </b-card-group>
            </div>

            <div class="mt-3">
                <b-card-group deck>
                    <b-card>
                        <img src="../assets/main_content/prl4.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Расстройство идентичности: выраженная и стойкая нестабильность самооценки или
                            болезненные
                            чувства к себе / ощущения себя.
                        </b-card-text>
                    </b-card>

                    <b-card>
                        <img src="../assets/main_content/prl5.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Импульсивность как минимум в двух областях, потенциально способных нанести вред /
                            ущерб.
                        </b-card-text>
                    </b-card>
                    <b-card>
                        <img src="../assets/main_content/prl6.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Повторяющиеся суицидальные мысли, угрозы суицида, суицидальные намерения, планы или
                            попытки, самоповреждающее поведение.
                        </b-card-text>
                    </b-card>
                </b-card-group>
            </div>
            <div class="mt-3">
                <b-card-group deck>
                    <b-card>
                        <img src="../assets/main_content/prl7.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Аффективная нестабильность, которая характеризуется ярко выраженной ориентацией
                            на текущее настроение
                        </b-card-text>
                    </b-card>
                    <b-card>
                        <img src="../assets/main_content/prl8.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Хроническое чувство пустоты.</b-card-text>
                    </b-card>
                    <b-card>
                        <img src="../assets/main_content/prl9.jpg" class="card-img card-img-top img-fluid" />
                        <b-card-text> Неуместный сильный гнев или трудности с контролем ярости или гнева
                        </b-card-text>
                    </b-card>
                </b-card-group>
            </div>
        </div>

        <!-- Employers -->
        <b-card-title>
                Наши специалисты
        </b-card-title>
        <div class="container">
            <b-carousel id="carousel-1" v-model="slide" :interval="4000" controls indicators background="#A45029"
                style="text-shadow: 1px 1px 2px #333;" @sliding-start="onSlideStart"
                @sliding-end="onSlideEnd">
                <b-carousel-slide>
                    <template #img>
                        <img slot="img" class="ImageParent img-fluid" src="../assets/employers/Golovaha.jpg"
                            alt="image slot">
                    </template>
                    <b-card-title>Головаха Николай </b-card-title>
                    <b-card-text>
                        психотерапевт, когнитивно-поведенческий и диалектико–поведенческий терапевт
                    </b-card-text>
                </b-carousel-slide>

                <b-carousel-slide>
                    <b-card-title>Mariia Aarseth</b-card-title>
                        
                    <template #img>
                        <img slot="img" class="ImageParent img-fluid" src="../assets/employers/Aarseth.jpg"
                            alt="image slot">
                    </template>
                    <b-card-text>
                        клинический психолог, преподаватель психологии.
                    </b-card-text>
                </b-carousel-slide>

                <b-carousel-slide>
                    <b-card-title>Макарова Яна</b-card-title>
                    <template #img>
                        <img slot="img" class="ImageParent img-fluid" src="../assets/employers/Makarova.jpg"
                            alt="image slot">
                    </template>
                    <b-card-text>
                        клинический психолог, нейробиолог, диалектико – поведенческий терапевт
                    </b-card-text>
                </b-carousel-slide>
            </b-carousel>
        </div>
    
    <!--Make appointment-->
    <section>
        <div class="container result__content">
    <b-card style="background: #4BA0B5">
        <b-button style="background: #A45029">Записаться сейчас</b-button>
    </b-card>
</div>
</section>
    </div>
</template>
  
<script>
export default {
    name: 'MainPage',
}
</script>
  
<style scoped>
/* Solution using `transform: translate`: */
.imageParent img {
    position: absolute;
    top: 80%;
    left: 80%;
    transform: translate(-80%,-80%);
}
</style>
  