<template>
  <div>    
<router-view></router-view>
  <form @submit.prevent="submitForm">
      <div class = "form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="zadanie" v-model="student.cele">
        <button class="btn btn-info" >Submit</button>
        <button class ="btn btn-danger" @click="deleteStudent(student)"> Delete</button>
      </div>
    </form>
  <tbody>
      <tr v-for="student in cele" :key="student.id" @dblclick="$data.student =student" >
           <th v-if="student.dni ==$route.params.id">
               
            <td class ="item">{{student.cele }}
             <input type="checkbox" @click="editStudent(student)" v-model="student.check">
            <label for="checkbox">{{ checked }}</label></td>
              </th>
            <td>
            </td>
          </tr>
        </tbody>
    </div>
</template>
<script>
export default 
{ 
  data(){
    return {
         student:{
        'cele': '',
        'check':'',
        'dni': '',  
      },
      cele :[],
        }
  },  
async created(){
    await this.getStudents();
    this.student.dni=this.$route.params.id;
    this.student.check=false;
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
        var response = await fetch('http://localhost:8000/api/cele/',)
        this.cele = await response.json();

    },

      async createStudent(){
      await this.getStudents();
      await fetch('http://localhost:8000/api/cele/', {
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
        
        await fetch(`http://localhost:8000/api/cele/${this.student.id}/`, {
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
        
        await fetch(`http://localhost:8000/api/cele/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)

      });
      await this.getStudents();
      

    },
    }}
</script>

<style>
.item{
  
  margin: 20px;
  padding:20px;
}
</style>