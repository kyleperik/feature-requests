vue_utils.push_component('app', {
    data: function () {
        return {
            feature_requests: null,
            edit_mode: false
        }
    },
    methods: {
        add: function () {
            this.edit_mode = true;
        }
    },
    created: function () {
        fetch($SCRIPT_ROOT + 'feature_request')
        .then(r => r.json())
        .then(r => {
            this.feature_requests = r;
        });
    }
});

function start() {
    Vue.component('flat-pickr', VueFlatpickr.default);
    
    new Vue({
        el: '#Root'
    });
}

window.addEventListener('load', function () {
    vue_utils.register_components(start);
})