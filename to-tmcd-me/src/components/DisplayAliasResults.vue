<template>
  <div v-for='alias in aliases'>
    Alias: {{ alias.alias }}<br>
    Target: {{ alias.target }}
  </div>
</template>

<script>
export default {
  name: 'DisplayAliasResults',
  props: [aliases]
}
</script>