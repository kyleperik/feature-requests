vue_utils.push_component('feature_request', {
    props: ['feature_request'],
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