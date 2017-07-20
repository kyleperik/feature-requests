vue_utils.push_component('feature_request', {
    props: ['feature_request'],
    computed: {
        target_date_formatted: function () {
            return moment(this.feature_request.target_date).format('MMMM Do, YYYY');
        }
    }
});