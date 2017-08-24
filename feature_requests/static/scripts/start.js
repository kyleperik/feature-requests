vue_utils.push_component('app', {
    data: function () {
        return {
            feature_requests: null,
            clients: null,
            edit_mode: false,
            editing: null,
            settings: false
        }
    },
    methods: {
        client: function (id) {
            if (!this.clients) {
                return;
            }
            return this.clients.filter(c => c.id === id)[0];
        },
        add: function () {
            this.edit_mode = true;
        },
        edit: function (editing) {
            this.edit_mode = true;
            this.editing = editing;
        },
        close_settings: function () {
            this.settings = false;
            this.load();
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


// Taken from string-hash from npm
// ** https://www.npmjs.com/package/string-hash **
var customHash = function(str) {
    var hash = 5381;
    var i = str.length;

    while(i) {
      hash = (hash * 33) ^ str.charCodeAt(--i);
    }
    return hash >>> 0;
}
var colorHash = new ColorHash({
    hash: customHash,
    saturation: [ 0.6, 0.8, 1.0 ],
    lightness: [ 0.4, 0.45, 0.5 ]
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
