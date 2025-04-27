import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/aura-dark-green/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

import Toolbar from 'primevue/toolbar'
import Button from 'primevue/button'
import Tooltip from 'primevue/tooltip'
import InputText from 'primevue/inputtext'
import Card from 'primevue/card';
import ProgressSpinner from 'primevue/progressspinner';

const app = createApp(App)

app.use(PrimeVue, {
    ripple: true,
    unstyled: false,
    pt: {
        button: {
            root: { class: 'dark-button' }
        },
        toolbar: {
            root: { class: 'dark-toolbar' }
        }
    }
})

app.component('Toolbar', Toolbar)
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Card', Card);
app.component('ProgressSpinner', ProgressSpinner);
app.directive('tooltip', Tooltip)
app.use(router)
app.mount('#app')
