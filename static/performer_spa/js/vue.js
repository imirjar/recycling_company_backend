let a = axios.get('http://localhost:8000/api/requisition_items/?format=json');
console.log(a)



const NotFound = { template: '<a href="/">Страница не найдена</p>' }
const Home = { template: '<p>главная</p>' }
const About = { template: '<p>о нас</p>' }

const routes = {
  '/': Home,
  '/about': About
}



var vm = new Vue({
  el: '#app',
  data: {
    info: [],
    currentRoute: window.location.pathname
  },
  mounted() {
    axios
      .get('http://localhost:8000/api/requisition_items/?format=json')
      .then(response => (this.info = response));
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})