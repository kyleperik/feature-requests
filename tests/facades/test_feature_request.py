import feature_requests.facades.feature_request as facade
from mock import Mock, patch, call

@patch('feature_requests.facades.feature_request.data')
def test_get(data):
    #-arrange-
    data.feature_request = Mock()
    data.feature_request.get_all = Mock(side_effect=[['one', 'two']])
    
    #-act-
    result = facade.get()
    
    #-assert-
    assert len(result) == 2

    result_feature = result[0]
    assert result_feature == 'one'

    result_feature = result[1]
    assert result_feature == 'two'
