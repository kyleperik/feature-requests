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

@patch('feature_requests.facades.client.data')
def test_save(data):
    #-arrange-
    clients = [
        domain.models.Client(id=0, name='Starting Client Name', priority=2),
        domain.models.Client(id=1, name='Client Name', priority=1),
    ]
    
    data.client = Mock()
    data.client.get_all = Mock(side_effect=[clients])
    data.client.update = Mock()
    data.client.add = Mock()

    updated_clients = [
        domain.models.Client(id=0, name='Edited Client Name', priority=1),
        domain.models.Client(id=1, name='Client Name', priority=2),
        domain.models.Client(id=2, name='Client Name', priority=3),
    ]
    
    #-act-
    facade.save_all(updated_clients)
    
    #-assert-
    assert data.client.update.mock_calls == [
        call(updated_clients[0]),
        call(updated_clients[1]),
    ]
    assert data.client.add.mock_calls == [
        call(updated_clients[2]),
    ]
