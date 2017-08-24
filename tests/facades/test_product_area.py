import feature_requests.facades.product_area as facade
from mock import Mock, patch, call

@patch('feature_requests.facades.product_area.data')
def test_get_all(data):
    #-arrange-
    data.product_area = Mock()
    data.product_area.get_all = Mock(side_effect=[['one', 'two']])
    
    #-act-
    result = facade.get()
    
    #-assert-
    assert len(result) == 2

    result_client = result[0]
    assert result_client  == 'one'

    result_client = result[1]
    assert result_client == 'two'
