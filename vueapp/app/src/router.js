import {createRouter, createWebHashHistory} from 'vue-router'
import Compo3 from './components/Compo3'
import Compo2 from './components/Compo2' 
import Compo4 from './components/Compo4' 
import Compo5 from './components/Compo5' 



const routes = [
    {path:'/dc-heros', component:Compo3},
    {path:'/d-compo', component:Compo2},
    {path:'/c-compo', component:Compo4},
    {path:'/t-compo/:id', component:Compo5},
    
    
    
   

];
const router = createRouter({
    history:createWebHashHistory(), 
    routes,
});

export default router;
