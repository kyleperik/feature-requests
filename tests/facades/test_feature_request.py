import feature_requests.facades.feature_request as facade
from feature_requests import domain
import feature_requests.domain.models
from mock import Mock, patch, call

@patch('feature_requests.facades.feature_request.data')
def test_get_all(data):
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

@patch('feature_requests.facades.feature_request.data')
def test_get(data):
    #-arrange-
    data.feature_request = Mock()
    data.feature_request.get = Mock(return_value='one')
    
    #-act-
    result = facade.get(id=2)

    #-assert-
    assert result == 'one'

    data.feature_request.get.assert_called_with(2)

@patch('feature_requests.facades.feature_request.data')
def test_add(data):
    #-arrange-
    data.feature_request = Mock()
    data.feature_request.add = Mock(side_effect=[5])

    feature_request = domain.models.FeatureRequest(
        title = 'A great Feature Request'
    )
    
    #-act-
    result = facade.add(feature_request)
    
    #-assert-
    assert result == 5

    data.feature_request.add.assert_called_with(feature_request)
