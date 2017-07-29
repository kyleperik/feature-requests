vue_utils.push_component('edit_feature_request', {
    props: ['existing_id'],
    beforeMount: function () {
        throw new Error("Not Implemented!")
    },
    data: function () {
        return {
            title: '',
            description: '',
            target_date: moment().format('YYYY-MM-DD'),
        };
    },
    methods: {
        textarea_change: function (e) {
            autosize(e.target);
        },
        save: function () {
            if (this.existing_id) {
                throw new Error('Not Implemented!')
            } else {
                this.save_new();
            }
        },
        save_new: function () {
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