<template>
  <div >
    
  <router-view></router-view>
    <form @submit.prevent="submitForm">
      <div class = "form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="task" v-model="student.title">
        <input type="text" class="form-control col-3 mx-2" placeholder="typ" v-model="student.detail">
        
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
        
      <table class = "table">
        <thead>
          <th>Task</th>
          <th>Typ</th>
          
        </thead>
        <tbody>
          <tr v-for="student in apka" :key="student.id" @dblclick="$data.student =student">
            <td>{{ student.title}}</td>
            <td>{{ student.detail}}</td>
            
            <td> 
              
              <router-link :to="`/t-compo/${student.id}`" @click="getStudent1(student)"><button class = "btn btn-secondary">View</button></router-link>
              <button class ="btn btn-danger" @click="deleteStudent(student)"> Delete </button>
              
            </td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script>

export default {
  name: 'Compo3',
  
  data(){
    return {
      student:{
        'title': '',
        'detail': '',
        
      },
      apka: []
    }
  },
 
  
  async created(){
    await this.getStudents();
  },

  methods: {
    submitForm(){
       if (this.student.id == undefined){
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
        body: JSON.stringify(this.student)

      });
      await this.getStudents();
      },
      async editStudent(){
        await this.getStudents();
        
        await fetch(`http://localhost:8000/api/apka/${this.student.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)

      });
      await this.getStudents();
      this.student = {};

    },

    async deleteStudent(student){
      await this.getStudents();
        
        await fetch(`http://localhost:8000/api/apka/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)

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
