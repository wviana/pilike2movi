from pylike2movi import Movidesk
from pytest import raises

def test_instance_movidesk_with_token():
    token = 'test1234'
    md = Movidesk(token=token)
    assert md.token == token
    assert md.url == 'https://api.movidesk.com/public/v1'

def test_instance_with_token_and_url():
    token = 'anything'
    url = 'https://thatwillnotchange.movidesk.com/public/v1'
    md = Movidesk(token, url=url)
    assert md.token == token
    assert md.url == url

