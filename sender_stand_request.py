import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
def get_order(parameter):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER,
                        params=parameter)
