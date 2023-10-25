<template>
  <card>
    <b-card-title>
      <b-icon icon="circle-fill" animation="throb"></b-icon>
        Искуственнный интеллект порекомендует специалиста
      <b-icon icon="circle-fill" animation="throb"></b-icon>
    </b-card-title>
    <div>
      <v-card>
        <img
          class="ImageParent img-fluid"
          src="@/assets/ai_choose.gif"
          alt="image slot"
        />
      </v-card>
    </div>
        <div>
            <b-card style="background: #A7C5C5">
                <b-button to="/choose" style="background: #B96028">Попробовать</b-button>
            </b-card>
        </div>
  </card>
</template>

<script>

export default {
    name: 'ChooseBlock',
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