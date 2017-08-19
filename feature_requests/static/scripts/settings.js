window.vue_utils.push_component('settings', {
    props: ['initialClients'],
    data: function () {
        return {
            clients: this.initialClients
        }
    },
    methods: {
        move: function (e) {
            this.clients.forEach((c, i) => {
                c.priority = i + 1;
            });
        },
        save: function () {
            this.$emit('close');
        },
        cancel: function () {
            this.$emit('close');
        },
        colorHash: function (str) {
            return colorHash.hex(str);
        }
    }
});