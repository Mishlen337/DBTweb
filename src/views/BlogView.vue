<template>
  <div class="blog">
    <div class="p-5 text-center bg-image">
      <b-card-title>Блог</b-card-title>
    </div>
    <div class="text-center">
      <b-card-title>Популярные статьи</b-card-title>
    </div>

    <b-card>
    <!-- Slider -->
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
        v-for="ar in articles"
        :key="ar.title"
        :image="ar.imageSrc"
        :title="ar.title"
        :link="ar.articleLink"
      >
      </vueper-slide>
    </vueper-slides>
  </b-card>
    <div class="text-center">
      <b-card-title>Новые статьи</b-card-title>
    </div>

    <!-- Articles -->
    <div class="row">
      <b-card-group class="col-md-4" v-for="ar in articles" :key="ar.title">
        <ArticleInfo
          :title="ar.title"
          :author="ar.author"
          :description="ar.description"
          :imageSrc="ar.imageSrc"
          :articleLink="ar.articleLink"
        >
        </ArticleInfo>
      </b-card-group>
    </div>
  </div>
</template>
  


<script>
import { VueperSlide, VueperSlides } from "vueperslides";
import "vueperslides/dist/vueperslides.css";

import ArticleInfo from "@/components/BlogView/ArticleInfo.vue";
// import ArticlePopular from '@/components/BlogView/ArticlePopular.vue'

export default {
  name: "BlogView",
  components: {
    ArticleInfo,
    VueperSlides,
    VueperSlide,
    // ArticlePopular
  },
  data() {
    return {
      imageSrc: require("@/assets/articles/article2.jpg"),
      articles: [
        {
          title: "История DBT терапии",
          author: "Головаха Николай",
          description:
            "Диалектическа поведенческая терапия (DBT) – создана Маршей Линехан во второй половине 20 века, для людей ...",
          imageSrc: require("@/assets/articles/article1.jpg"),
          articleLink: "https://telegra.ph/Here-it-is-basic-history-10-20",
        },
        {
          title: "Биосоциальная модель ПРЛ",
          author: "Головаха Николай",
          description:
            "Людям с ПРЛ сложно контролировать свои эмоции. Почему так происходит? Есть биологическая основа ...",
          imageSrc: require("@/assets/articles/article2.jpg"),
          articleLink: "https://telegra.ph/Here-it-is-basic-history-10-20",
        },
        {
          title: "Эмоциональная дисрегуляция при ПРЛ",
          author: "Головаха Николай",
          description:
            "В ДБТ считается, что не умение регулировать сильные эмоции, приводит к проблемному поведению. Это такое поведение ...",
          imageSrc: require("@/assets/articles/article3.jpg"),
          articleLink: "https://telegra.ph/Here-it-is-basic-history-10-20",
        },
        {
          title: "Возможности ДБТ при лечении ПРЛ",
          author: "Головаха Николай",
          description:
            "Мы не можем изменить повышенную врожденную эмоциональность. При этом, можно учиться регулировать свои эмоции с помощью  ...",
          imageSrc: require("@/assets/articles/article4.jpg"),
          articleLink: "https://telegra.ph/Here-it-is-basic-history-10-20",
        },
      ],
    };
  },
};
</script>

<style scoped>
.no-shadow {
  max-width: 50%;
  max-height: 50%;
  margin: auto;
}
</style>
