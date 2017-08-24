vue_utils.push_component('edit_feature_request', {
    props: ['existing_id', 'clients', 'product_areas'],
    beforeMount: function () {
        if (this.existing_id) {
            fetch($SCRIPT_ROOT + 'feature_request/' + this.existing_id)
            .then(r => r.json())
            .then(r => {
                this.title = r.title;
                this.description = r.description;
                this.target_date = r.target_date;
                this.client_id = r.client_id;
                this.product_area_id = r.product_area_id;
                Vue.nextTick(() => autosize(this.$el.querySelector('textarea')));
            });
        }
    },
    data: function () {
        return {
            title: '',
            description: '',
            target_date: moment().format('YYYY-MM-DD'),
            client_id: '',
            product_area_id: '',
        };
    },
    computed: {
        isValid: function () {
            return this.client_id && this.product_area_id;
        }
    },
    methods: {
        textarea_change: function (e) {
            autosize(e.target);
        },
        save: function () {
            if (!this.isValid) {
                return;
            }
            if (this.existing_id) {
                this.save_update();
            } else {
                this.save_new();
            }
        },
        save_update: function () {
            fetch($SCRIPT_ROOT + 'feature_request/' + this.existing_id, {
                method: 'PATCH',
                body: JSON.stringify({
                    title: this.title,
                    description: this.description,
                    target_date: this.target_date,
                    client_id: this.client_id,
                    product_area_id: this.product_area_id,
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(() => this.$emit('close'))
        },
        save_new: function () {
            fetch($SCRIPT_ROOT + 'feature_request/', {
                method: 'POST',
                body: JSON.stringify({
                    title: this.title,
                    description: this.description,
                    target_date: this.target_date,
                    client_id: this.client_id,
                    product_area_id: this.product_area_id,
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(() => this.$emit('close'))
        }
    }
});