vue_utils.push_component('app', {
    data: function () {
        return {
            feature_requests: null,
            clients: null,
            edit_mode: false,
            editing: null
        }
    },
    methods: {
        client: function (id) {
            if (!this.clients) {
                return;
            }
            var client = this.clients.filter(c => c.id === id)[0];
            return client ? client.name : null;
        },
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

            fetch($SCRIPT_ROOT + 'client/')
            .then(r => r.json())
            .then(r => {
                this.clients = r;
            });
        }
    },
    created: function () {
        this.load();
    }
});

var colorHash = new ColorHash({saturation: 0.5, lightness: 0.6});

function start() {
    Vue.component('flat-pickr', VueFlatpickr.default);
    
    new Vue({
        el: '#Root'
    });
}

window.addEventListener('load', function () {
    vue_utils.register_components(start);
})
