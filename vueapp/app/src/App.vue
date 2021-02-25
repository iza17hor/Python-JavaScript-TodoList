<template>
<div>
  <div>
  
    <div>
      <nav class="navbar navbar-dark bg-dark ">
        <router-link to="/c-compo">Cards</router-link>
        <router-link to="/dc-heros">Task List 1</router-link>
        <router-link to="/d-compo">Task List 2</router-link>
        
      </nav>
      
    </div>

</div>
  <Compo1 />

</div>
</template>

<script>

import Compo1 from "./components/Compo1";
export default {
  components :{  Compo1},

}
</script>

<style>

</style>