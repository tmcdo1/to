<template>
  <div id="app">
    <nav id="nav">
      <router-link to="/"><img alt='to logo' src='./assets/logo.png' class='nav-logo'></router-link>
    </nav>
    <router-view/>
    <el-footer class='footer'>
      <router-link to='/about'>About</router-link>
      <router-link to='/getting-started'>Getting Started</router-link>
    </el-footer>
  </div>
</template>

<style lang="scss">
html, body {
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  // background: #202020;
}

input[type='text'], button {
  // background-color: #2e2e2e;
  // color: white;
}

.title {
  text-align: center;
}

.page {
  display: flex;
  flex-direction: column;
  width: 50vw;
  min-width: 350px;
  max-width: 850px;
  margin: 0 auto;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100%;
  width: 100%;
}

#nav {
  padding: 30px;
  text-align: center;

  .nav-logo {
    width: 64px;
    height: 64px;
  }

  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: #202020;
  a {
    color: white;
    text-decoration: none;
    margin: 4px;
  }
}

.footer::before {
  position: relative;
  display: block;
  content: '';
  border-top: 1px solid whitesmoke;
}
</style>
