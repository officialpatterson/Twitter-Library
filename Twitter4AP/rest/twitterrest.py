from requests_oauthlib import OAuth1, OAuth2
import requests
class TwitterRest():
    def __init__(self):

        self._authenticate() #authenticate user using oauth1

    def _authenticate(self):
        
        self.api_url = 'https://api.twitter.com/%s'
        
        self.consumer_key = "9kdMoUXuvMYrjFZKUPxw"
        self.consumer_secret = "mPZPbMg3DV01uE6FKyqUtOz5OaFbiU40uaLfJsQ5TxM"
        self.oauth_token = "65512395-RYksZQI8a5zIOpyiqEs9WLR1bLcuZnd1xjo54UE"
        self.oauth_token_secret = "bqKe6zJo7Qn0KnPwmAeFWZf8LXHimZE8jOohlmcPGBs"
        
        self.request_token_url = 'https://api.twitter.com/oauth/request_token'
        self.access_token_url = 'https://api.twitter.com//oauth/access_token'
        self.authenticate_url = 'https://api.twitter.com/oauth/authenticate'
        
        self.client = requests.Session()
        if all([self.consumer_key, self.consumer_secret, self.oauth_token, self.oauth_token_secret]):
            self.client.auth = OAuth1(self.consumer_key, self.consumer_secret, self.oauth_token, self.oauth_token_secret)
        else:
            self.client.auth = None


    def search(self, trackwords):
        payload = trackwords
        self.response = self.client.get("https://api.twitter.com/1.1/search/tweets.json?", params=payload)
	return self.response
    def close(self):
	self.client.close()
	return
