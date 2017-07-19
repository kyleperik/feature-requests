#from feature_requests import facades
import feature_requests.facades.feature_request as facade
from mock import Mock, patch, call

def test_get():
    #-arrange-
    
    #-act-
    result = facade.get()
    
    #-assert-
    assert len(result) == 2
