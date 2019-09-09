<template>
  <div>Redirecting to {{ alias }}</div>
</template>

<script>
import axios from 'axios'
/* make request to server */

export default {
  name: 'redirect-alias',
  props: ['alias'],
  mounted () {
    console.log(`${process.env.VUE_APP_API_LOC}/alias/${this.alias}`, this.alias)
    axios.get(`${process.env.VUE_APP_API_LOC}/alias/${this.alias}`)
      .then(res => {
        console.log(res)
        window.location = res.data.target
      })
      .catch(err => {
        console.error(err)
        this.$router.push('/')
      })
  }
}
</script>
