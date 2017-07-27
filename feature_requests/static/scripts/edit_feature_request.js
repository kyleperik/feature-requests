vue_utils.push_component('edit_feature_request', {
    data: function () {
        return {
            title: '',
            description: '',
            target_date: new Date().toLocaleDateString(),
        };
    },
    methods: {
        textarea_change: function (e) {
            autosize(e.target);
        },
        save: function () {
            fetch($SCRIPT_ROOT + 'feature_request/', {
                credentials: 'include',
                method: 'POST',
                body: JSON.stringify({
                    title: this.title,
                    description: this.description,
                    target_date: this.target_date
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(() => this.$emit('close'))
        }
    }
});