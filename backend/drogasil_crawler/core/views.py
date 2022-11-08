from textwrap import indent
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64

# url = "https://drogasil.com.br"
# query = "query tradeByParams($id: String, $store: String, $name: String, $pages: [String!], $platforms: [String!], $sizes: [String!], $slot: String, $enabled: String, $position: String, $type: String) {\n tradeByParams(\n params: {id: $id, store: $store, name: $name, pages: $pages, platforms: $platforms, sizes: $sizes, slot: $slot, enabled: $enabled, position: $position, type: $type}\n ) {\n id\n store\n name\n pages\n platforms\n sizes\n slot\n enabled\n position\n type\n createdAt\n updatedAt\n __typename\n }\n}\n"
@csrf_exempt
def return_info(request):

    if request.method == 'GET':
        print('request do metodo GET')
        print('**************')
        print(request.GET)

    if request.method == 'POST':
        print(request.POST)
        print('--------------')
        print(request.body)
        
        request_data_json = request.body.decode('utf8').replace("'", '"')
        print('request_data_json')
        print(request_data_json)

        data = json.loads(request_data_json)
        print(type(data))
        print(data['consulta'])
        busca = data['consulta']
        busca = busca.replace(' ','+') # Substitui espacos em branco ao passar param para URL
        
        # formated_string_data = json.dumps(data, indent=4, sort_keys=True)
        # print('formated_string_data')
        # print(formated_string_data)

        # object_data = {}
        # object_data.update(formated_string_data)
        # print('object_data')
        # print(object_data)
        # print(80*'-')
        # print("object_data.get('query')")
        # print(object_data.get('consulta'))

        # url = "https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGASIL/channel/SITE/product/search/live?term="+str(busca)+"&tokenCart=JORH5eyXMF9F7mqV2SDV1K9ZiHJeWrGY&limit=4&sort_by=relevance:desc&origin=searchSuggestion"
        url = "https://www.drogasil.com.br/_next/data/xJB_e_fCeSwKKZxI071Xq/search.json?w="+str(busca)
        # print(url)
        response = requests.get(url = url)
        # print(response.url)
        response_data = json.loads(response.content)
        # print(type(response_data))
        # print(response_data)
        products_list = response_data.get('pageProps').get('initialData').get('products')
        number_of_products = response_data.get('pageProps').get('initialData').get('productsSize')

        # print('numero total de produtos')
        # print(number_of_products)

        # print(50*'*')
        # print(products_list)
        # print(50*'*')

        """ 
            RETORNA DADOS DE OUTRAS PAGINAS!!!
            Sem o bloco abaixo, apenas os 24 primeiros produtos serão crawleados
        """
        # index = 2
        # while(len(products_list) < number_of_products):
        #     url = "https://www.drogasil.com.br/_next/data/xJB_e_fCeSwKKZxI071Xq/search.json?w="+str(busca)+"&p="+str(index)
        #     print(url)
        #     response = requests.get(url = url)
        #     response_data = json.loads(response.content)
        #     # print(type(response_data))
        #     # print(response_data)
        #     products_list.append(response_data.get('pageProps').get('initialData').get('products'))
        #     index += 1

        return JsonResponse({'products': products_list}, safe=False)