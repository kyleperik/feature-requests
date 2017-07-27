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
        }
    }
});