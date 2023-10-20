
<template>
    <b-card>
    <img :src="imageSrc" class="card-img card-img-top img-fluid"/>
</b-card>
</template>
<script>



export default (
    {
        name: "ArticlePopular",
        props: ["title", "imageSrc", "articleLink"],
    })
</script>

<style scoped>
.card-actions {
    position: absolute;
    bottom: 0;

}

.card-outter {
    position: relative;
    padding-bottom: 50px;
}

.imageParent img {
    position: absolute;
    top: 80%;
    left: 80%;
    transform: translate(-80%, -80%);
}
</style>
