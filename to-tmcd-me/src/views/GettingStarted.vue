<template>
  <div class='page'>
    <h1 class='title'>Getting Started</h1>
    <section>
      <p>This service is an alias or url shortener service.</p>
      <p>
        It is highly recommended to get the To Alias browser extension.
        With the extension, you can use <code>to/&lt;alias&gt;</code> in your browser search bar.
      </p>
      <p>
        If you decide to not use the extension, you can still use the service by typing <code>{{ window.location.host }}/to/&lt;alias&gt;</code>
        in the browser search bar.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: 'GettingStarted',
  data () {
    return {
      window
    }
  }
}
</script>
