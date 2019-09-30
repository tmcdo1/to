<template>
  <section>
    <div v-for='alias in aliases' :key='alias.alias' class='item'>
      Alias: {{ alias.alias }}<br>
      Target: <a :href='alias.target'>{{ alias.target }}</a>
    </div>
  </section>
</template>

<script>
export default {
  name: 'DisplayAliasResults',
  props: ['aliases']
}
</script>

<style lang="scss" scoped>
.item {
  margin-top: 16px;
  padding: 12px;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}

.item:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>
