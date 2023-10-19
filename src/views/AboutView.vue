<template>
  <div class="about">
    <BasicInfoBlock></BasicInfoBlock>
    <ValuesBlock></ValuesBlock>
    <MotivationBlock></MotivationBlock>
  </div>
</template>

<script>
import BasicInfoBlock from '@/components/AboutView/BasicInfoBlock.vue'
import ValuesBlock from '@/components/AboutView/ValuesBlock.vue'
import MotivationBlock from '@/components/AboutView/MotivationBlock.vue'

export default {
  name: 'AboutView',
  components: {
    BasicInfoBlock,
    ValuesBlock,
    MotivationBlock,
  }
}
</script>

