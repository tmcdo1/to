<template>
  <div class="page">
    <el-button @click='showDialog()'>Create Alias</el-button>
    <CreateAlias :visible.sync='createDialogVisible' />

    <div id='search'>
      <SearchAlias id='search-bar'/>
      <el-button id='search-button' type='primary' icon='el-icon-search'>Search</el-button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchAlias from '@/components/SearchAlias.vue'
import CreateAlias from '@/components/CreateAlias.vue'

function showDialog () {
  this.createDialogVisible = true
}

export default {
  name: 'home',
  components: {
    SearchAlias,
    CreateAlias
  },
  data () {
    return {
      createDialogVisible: false
    }
  },
  methods: {
    showDialog
  }
}
</script>

<style scoped lang='scss'>
  #search {
    display: flex;
    flex-wrap: wrap;
  }

  #search-bar {
    flex-grow: 3;
    min-width: 100px;
  }

  #search-button {
    flex-grow: 1;
    display: inline-block;
  }
</style>
