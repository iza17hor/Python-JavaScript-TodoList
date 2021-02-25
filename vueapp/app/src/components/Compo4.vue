<template>
 <div >
<router-view></router-view>
   <form @submit.prevent="submitForm">
      <div class = "form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="task" v-model="student1.title">
        <input type="text" class="form-control col-3 mx-2" placeholder="details" v-model="student1.detail">
        
        <button class="btn btn-success">Submit</button>
      </div>
    </form>



  <div class ="d-flex flex-wrap p-4">
  <tr v-for="student1 in apka" :key="student1.id" @dblclick="$data.student1 =student1">
  <div class="card p-2 " style="width: 18rem;">   
  <div class="card-body p-4 ">
    <h2 class="card-title">{{student1.title}}</h2>
    <h6>{{student1.detail}}</h6>
    
   
  <router-link :to="`/t-compo/${student1.id}`" @click="getStudent1(student1)"><h3>View</h3></router-link>
  
  <button class ="btn btn-link" @click="deleteStudent(student1)"> Delete </button>
  

</div> 
</div>   
</tr>
</div>
</div>
</template>

<script>

export default {
  name: 'Compo3',
  
  data(){
    return {
      student:{
        
        'cele': '',
        'dni':'',
          
      },
      student1:{
      'title': '',
      },
     apka: [],
     cele :[]
      
    }
  },
 
  async created(){
    await this.getStudents();
  },

  methods: {
    submitForm(){
       if (this.student1.id == undefined){
         this.createStudent();
         }
         else {
           this.editStudent();
         }

    },


    async getStudents(){
      var response = await fetch('http://localhost:8000/api/apka/',)
      this.apka = await response.json();

    },
     async createStudent(){
      await this.getStudents();
      await fetch('http://localhost:8000/api/apka/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student1)

      });
      await this.getStudents();
      },

            async editStudent(){
        await this.getStudents();

        
        await fetch(`http://localhost:8000/api/apka/${this.student1.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student1)

      });
      await this.getStudents();
      this.student1= {};

    },


        async deleteStudent(student1){
      await this.getStudents();
        
        await fetch(`http://localhost:8000/api/apka/${student1.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student1)

      });
      await this.getStudents();
      

    },
  } 
}
</script>

<style>
#app {
 
  text-align: center;
  background-color: rgb(194, 194, 194);
}
</style>
