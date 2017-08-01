vue_utils.push_component('feature_request', {
    props: ['feature_request'],
    data: function () {
        return {
            show_options: false
        };
    },
    methods: {
        remove: function () {
            fetch($SCRIPT_ROOT + '/feature_request/' + this.feature_request.id,
            {
                method: ['DELETE']
            })
            .then(() => this.$emit('reload'))
            this.show_options = false;
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
        }
    }
});