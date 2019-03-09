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

# RESULT:

{'attributes': [{'id': 200000661,
                 'name': 'Compatible Brand',
                 'value': 'Blackberry,Palm,LG,Toshiba,Samsung,Panasonic,HTC,Nokia,SONY,Motorola',
                 'value_id': '365297,34,361795,361800,7470,361798,361794,361797,100012870,361796'},
                {'id': 2,
                 'name': 'Brand Name',
                 'value': 'OLAUDEM',
                 'value_id': '201627849'},
                {'id': 351,
                 'name': 'Type',
                 'value': 'Micro USB',
                 'value_id': '200005570'},
                {'id': 200001037,
                 'name': 'Has Retail Package',
                 'value': 'No',
                 'value_id': '350215'}],
 'category_id': '440504',
 'company_id': '230027728',
 'count_per_lot': 1,
 'html_description': None,
 'id': '32886025338',
 'multi_unit': 'pieces',
 'price_summary': {'bulk_amount': {'max': {'currency': 'USD', 'value': 0.89},
                                   'min': {'currency': 'USD', 'value': 0.61}},
                   'discounted_amount': {'max': {'currency': 'USD',
                                                 'value': 0.89},
                                         'min': {'currency': 'USD',
                                                 'value': 0.61}},
                   'original_amount': {'max': {'currency': 'USD',
                                               'value': 0.97},
                                       'min': {'currency': 'USD',
                                               'value': 1.41}},
                   'unit_bulk_amount': {'max': {'currency': 'USD',
                                                'value': 0.89},
                                        'min': {'currency': 'USD',
                                                'value': 0.61}},
                   'unit_discounted_amount': {'max': {'currency': 'USD',
                                                      'value': 0.61},
                                              'min': {'currency': 'USD',
                                                      'value': 0.89}},
                   'unit_original_amount': {'max': {'currency': 'USD',
                                                    'value': 0.97},
                                            'min': {'currency': 'USD',
                                                    'value': 1.41}}},
 'prices': [],
 'product_images': ['https://ae01.alicdn.com/kf/HTB17YycJxnaK1RjSZFtq6zC2VXac.jpg_960x960.jpg_.webp',
                    'https://ae01.alicdn.com/kf/HTB1kPV6iGAoBKNjSZSyq6yHAVXaK.jpg_960x960.jpg_.webp',
                    'https://ae01.alicdn.com/kf/HTB1UcrtyL5TBuNjSspcq6znGFXaA.jpg_960x960.jpg_.webp',
                    'https://ae01.alicdn.com/kf/HTB15_ZuiHArBKNjSZFLq6A_dVXal.jpg_960x960.jpg_.webp',
                    'https://ae01.alicdn.com/kf/HTB1FrLHyHGYBuNjy0Foq6AiBFXax.jpg_960x960.jpg_.webp',
                    'https://ae01.alicdn.com/kf/HTB1KL_8yKuSBuNjSsziq6zq8pXaw.jpg_960x960.jpg_.webp'],
 'promotion': {'discount': 37.0,
               'time_left': {'days': 3,
                             'hours': 14,
                             'minutes': 18,
                             'seconds': 43}},
 'reviews': {'five_star_count': 2735,
             'four_star_count': 191,
             'negative_count': 102,
             'neutral_count': 50,
             'one_star_count': 82,
             'positive_count': 2926,
             'ratings': 4.8,
             'three_star_count': 50,
             'total_count': 0,
             'two_star_count': 20},
 'seller': {'positive_feedback_rate': 97.3,
            'seller_level': '32-s',
            'store_id': 1082085,
            'store_name': 'OLAUDEM Official Store',
            'store_url': 'http://m.aliexpress.com/store/storeHome.htm?sellerAdminSeq=220013409'},
 'seller_id': '220013409',
 'shipping': [],
 'status': 'active',
 'status_id': 0,
 'title': 'Olaudem Cable Charging USB Micro USB Cables Charger Data Cord '
          'Charge Wire For Samsung Huawei charging Mobile Phone Cables CB029 ',
 'trade': {'sold': 13199, 'stock': None},
 'unit': 'piece',
 'wish_list_count': 5156}
