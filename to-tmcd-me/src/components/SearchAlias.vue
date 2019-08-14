<template>
  <span class='search-alias'>
    <el-input placeholder='to/' v-model='searchInput'></el-input>
  </span>
</template>

<script>
export default {
  name: 'SearchAlias',
  data () {
    return {
      searchInput: ''
    }
  },
  props: {
    msg: String
  }
}
</script>
