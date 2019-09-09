<template>
  <section>
    <div v-for='alias in aliases' :key='alias.alias'>
      Alias: {{ alias.alias }}<br>
      Target: {{ alias.target }}
    </div>
  </section>
</template>

<script>
export default {
  name: 'DisplayAliasResults',
  props: ['aliases']
}
</script>
