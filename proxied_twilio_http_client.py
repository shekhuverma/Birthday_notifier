from requests import Request, Session
from twilio.http import HttpClient
class ProxiedTwilioHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """
    def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None,
                allow_redirects=False):

        session = Session()
        session.proxies = {
                              "https" : "https://proxy.server:3128"
                          }

        request = Request(method.upper(), url, params=params, data=data, headers=headers, auth=auth)
        prepped_request = session.prepare_request(request)
        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

        return Response(int(response.status_code), response.content.decode('utf-8'))
