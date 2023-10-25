<template>
    <div>
        <!-- Employees -->
        <!--TODO use list-->
        <b-card-title>
                Наши специалисты
        </b-card-title>
        <div class="container">
            <b-carousel id="carousel-1" v-model="slide" :interval="4000" controls indicators background="#B96028"
                style="text-shadow: 1px 1px 2px #333;" @sliding-start="onSlideStart"
                @sliding-end="onSlideEnd">
                <b-carousel-slide>
                    <template #img>
                        <img slot="img" class="ImageParent img-fluid" src="@/assets/employees/Golovaha.jpg"
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
                        <img slot="img" class="ImageParent img-fluid" src="@/assets/employees/Aarseth.jpg"
                            alt="image slot">
                    </template>
                    <b-card-text>
                        клинический психолог, преподаватель психологии.
                    </b-card-text>
                </b-carousel-slide>

                <b-carousel-slide>
                    <b-card-title>Макарова Яна</b-card-title>
                    <template #img>
                        <img slot="img" class="ImageParent img-fluid" src="@/assets/employees/Makarova.jpg"
                            alt="image slot">
                    </template>
                    <b-card-text>
                        клинический психолог, нейробиолог, диалектико – поведенческий терапевт
                    </b-card-text>
                </b-carousel-slide>
            </b-carousel>
        </div>
    </div>
</template>

<script>
export default {
    name: 'EmployeesBriefInfo',
}
</script>

<style scoped>
/* Solution using `transform: translate`: */
.imageParent img {
    position: absolute;
    top: 80%;
    left: 80%;
    transform: translate(-80%, -80%);
}
</style>