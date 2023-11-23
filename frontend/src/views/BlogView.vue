<template>
  <div class="blog">
    <div class="p-5 text-center bg-image">
      <b-card-title>Блог</b-card-title>
    </div>

    <!-- Popular articles -->
    <div class="text-center">
      <b-card-title>Популярные статьи</b-card-title>
    </div>
    <b-card>
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
          v-for="ar in popularArticles"
          :key="ar.title"
          :image="'data:image/gif;base64,' + ar.imageSrc"
          :title="ar.title"
          :link="ar.articleLink"
        >
        </vueper-slide>
      </vueper-slides>
    </b-card>
    <!-- ----------------------- -->

    <!-- All articles -->
    <div class="text-center">
      <b-card-title>Новые статьи</b-card-title>
    </div>
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
    <!-- ----------------------- -->
  </div>
</template>


<script>
import { VueperSlide, VueperSlides } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
import axios from "axios";

import ArticleInfo from "@/components/BlogView/ArticleInfo.vue";

export default {
  name: "BlogView",
  components: {
    ArticleInfo,
    VueperSlides,
    VueperSlide,
  },
  data() {
    return {
      articles: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:7777/articles")
      .then((response) => (this.articles = response.data.articles))
      .catch((error) => console.log(error));
  },
  computed: {
    popularArticles() {
      return this.articles.filter(item => item.isPopular);
    },
  },
}
</script>

<style scoped>
.no-shadow {
  max-width: 50%;
  max-height: 50%;
  margin: auto;
}
</style>
