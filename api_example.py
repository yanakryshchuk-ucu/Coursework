from __future__ import print_function
import time
import aliseeksapi
from aliseeksapi.rest import ApiException
from pprint import pprint


# Configure API key authorization: ApiKeyAuth
configuration = aliseeksapi.Configuration()
configuration.api_key['X-API-CLIENT-ID'] = 'YOUR_API'

# create an instance of the API class
api_instance = aliseeksapi.ProductsApi(aliseeksapi.ApiClient(configuration))
product_request = aliseeksapi.ProductRequest() # ProductRequest | The request body of get product  (optional)
product_request.product_id='32886025338'
try:
    # Get products details as an aggregated request from AliExpress in realtime.
    api_response = api_instance.get_product(product_request=product_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product: %s\n" % e)
