<template>
  <span class='search-alias'>
    <el-input placeholder='to/'
      v-model='newVal'
      v-on:change='$emit("update:value", newVal)'></el-input>
  </span>
</template>

<script>
export default {
  name: 'SearchAlias',
  props: {
    value: String
  },
  data () {
    return {
      newVal: this.value
    }
  }
}
</script>
