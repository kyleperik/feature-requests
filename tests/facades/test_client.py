import feature_requests.facades.client as facade
from feature_requests import domain
import feature_requests.domain.models
from mock import Mock, patch, call

@patch('feature_requests.facades.client.data')
def test_get_all(data):
    #-arrange-
    data.client = Mock()
    data.client.get_all = Mock(side_effect=[['one', 'two']])
    
    #-act-
    result = facade.get()
    
    #-assert-
    assert len(result) == 2

    result_client = result[0]
    assert result_client  == 'one'

    result_client = result[1]
    assert result_client == 'two'
