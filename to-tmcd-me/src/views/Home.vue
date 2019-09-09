<template>
  <div class="page">
    <el-button @click='showDialog()'>Create Alias</el-button>
    <CreateAlias :visible.sync='createDialogVisible' />

    <div id='search'>
      <SearchAlias id='search-bar' :value.sync='aliasQuery'/>
      <el-button id='search-button' type='primary' icon='el-icon-search' @click='searchAliases()'>Search</el-button>
    </div>

    <DisplayAliasResults :aliases='aliasResults'></DisplayAliasResults>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchAlias from '@/components/SearchAlias.vue'
import CreateAlias from '@/components/CreateAlias.vue'
import DisplayAliasResults from '@/components/DisplayAliasResults.vue'
import axios from 'axios'

function showDialog () {
  this.createDialogVisible = true
}

function searchAliases () {
  axios.get(`${process.env.VUE_APP_API_LOC}/search?query=${this.aliasQuery}`)
    .then(res => {
      this.aliasResults = res.data.aliases
    })
}

export default {
  name: 'home',
  components: {
    SearchAlias,
    CreateAlias,
    DisplayAliasResults
  },
  data () {
    return {
      createDialogVisible: false,
      aliasQuery: '',
      aliasResults: []
    }
  },
  methods: {
    showDialog,
    searchAliases
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
