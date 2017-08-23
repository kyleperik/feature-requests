vue_utils.push_component('feature_request', {
    props: ['feature_request', 'client'],
    data: function () {
        return {
            show_options: false,
            optionsTimeout: null
        };
    },
    methods: {
        remove: function () {
            if (!confirm('Are you sure you want to delete this feature request?')) {
                this.show_options = false;
                return;
            }
            fetch($SCRIPT_ROOT + '/feature_request/' + this.feature_request.id,
            {
                method: ['DELETE']
            })
            .then(() => this.$emit('reload'));
            this.show_options = false;
        },
        toggle_show_options: function () {
            clearTimeout(this.optionsTimeout);
            this.show_options = !this.show_options;
        },
        mouseonOptions: function () {
            clearTimeout(this.optionsTimeout);
        },
        mouseoffOptions: function () {
            clearTimeout(this.optionsTimeout);
            this.optionsTimeout = setTimeout(() => this.show_options = false, 300);
        }
    },
    computed: {
        moment_target_date: function () {
            return moment(this.feature_request.target_date)
        },
        target_date_formatted: function () {
            return this.moment_target_date.format('MMMM Do, YYYY');
        },
        deadline_soon: function () {
            return this.moment_target_date.diff(moment(), 'days') < 10;
        },
        client_color: function () {
            return this.client.is_archived ? 'grey' : colorHash.hex(this.client.name);
        }
    }
});