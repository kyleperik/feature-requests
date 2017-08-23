window.vue_utils.push_component('settings', {
    props: ['initialClients'],
    data: function () {
        return {
            clients: this.initialClients.map(c => ({ 
                id: c.id,
                name: c.name,
                priority: c.priority,
                is_archived: c.is_archived,
                is_new: false
            }))
        }
    },
    beforeMount: function () {
        this.resort();
    },
    methods: {
        resort: function () {
            this.clients = this.clients.slice().sort(c => c.is_archived)
                .map((c, i) => {
                    c.priority = c.is_archived ? null : (i + 1);
                    return c;
                });
        },
        add: function () {
            this.clients.push({
                id: null,
                name: '',
                priority: this.clients.length + 1,
                is_archived: false,
                is_new: true
            });
            this.resort();
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
        del: function (client) {
            if (client.is_new) {
                var i = this.clients.indexOf(client);
                this.clients.splice(i, 1);
            } else {
                client.is_archived = true;
                this.resort();
            }
        },
        unarchive: function (client) {
            client.is_archived = false;
            this.resort();
        },
        cancel: function () {
            this.$emit('close');
        },
        colorHash: function (client) {
            return client.is_archived ? 'grey' : colorHash.hex(client.name);
        }
    }
});