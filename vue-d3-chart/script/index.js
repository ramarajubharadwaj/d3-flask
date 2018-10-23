
import chart1 from './chart1.vue'
/**********example **********/
import chart2 from './chart2.vue'
/**********example **********/
import VueRouter from 'vue-router'
Vue.use(VueRouter)
const router = new VueRouter({
	mode: 'history',
	routes: [
    {
    	path: '/',
    	component: chart1,
    },
    {
        path: '/page1',
        component: chart1,
    },
    {
    	path: '/page2',
    	component: chart2,
    }
  ]
})
new Vue({ // eslint-disable-line no-new
  router
}).$mount('#app')
