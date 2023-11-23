<template>
    <div id="search">
     <div class="p-5 text-center bg-image">
      <b-card-title>Интеллектуальный подбор специалиста </b-card-title>
    </div>
    <SearchBar></SearchBar>
    </div>
</template>

<script>
import SearchBar from "@/components/ChooseView/SearchBar.vue";

export default {
name: "ChooseView", 
  components: {
    SearchBar,
  },
};

</script>
