vue_utils.push_component('app', {
    data: function () {
        return {
            feature_requests: null,
            edit_mode: false,
            editing: null
        }
    },
    methods: {
        add: function () {
            this.edit_mode = true;
        },
        edit: function (editing) {
            this.edit_mode = true;
            this.editing = editing;
        },
        close_edit: function () {
            this.edit_mode = false;
            this.editing = null;
            this.load();
        },
        load: function () {
            fetch($SCRIPT_ROOT + 'feature_request/')
            .then(r => r.json())
            .then(r => {
                this.feature_requests = r;
            });
        }
    },
    created: function () {
        this.load();
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
