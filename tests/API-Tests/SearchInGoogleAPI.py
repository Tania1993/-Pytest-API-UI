import configparser
import pytest
import requests


class TestSearchInGoogleAPI:
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config['URLs']['google']

    @pytest.mark.API
    @pytest.mark.parametrize('search_word', ['python'])
    def test_response_should_contain_search_word(self, set_params, search_word):
        set_params['q'] = search_word
        resp = requests.get(url=self.url, params=set_params)

        assert resp.status_code == 200
        assert search_word in resp.text
