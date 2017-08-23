window.vue_utils.push_component('settings', {
    props: ['initialClients'],
    data: function () {
        return {
            clients: this.initialClients.map(c => ({ 
                id: c.id,
                name: c.name,
                priority: c.priority
            }))
        }
    },
    methods: {
        move: function (e) {
            this.clients.forEach((c, i) => {
                c.priority = i + 1;
            });
        },
        save: function () {
            fetch($SCRIPT_ROOT + '/client/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(this.clients)
            })
            .then(r => r.json())
            .then(r => {
                this.$emit('close');
            });
        },
        cancel: function () {
            this.$emit('close');
        },
        colorHash: function (str) {
            return colorHash.hex(str);
        }
    }
});