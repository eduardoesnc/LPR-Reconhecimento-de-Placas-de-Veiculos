import requests
import base64
import json
import re

def textDetection(caminho):
    print("="*139)
    print("Envie uma imagem para retornar a placa do automóvel:")
    print("="*139)

    #Leitura da imagem em formato binário
    with open(caminho, 'rb') as f:
        image = f.read()

    #codificar os bytes da imagem em base64
    image64 = base64.b64encode(image).decode('utf-8')

    #dados para solicitação POST
    data = {
        'body': image64
    }

    #URL do endpoint da API Gateway para o POST
    post_url = 'https://hnh8wbvo4h.execute-api.us-east-1.amazonaws.com/prod/classify'
    response = requests.post(post_url, json=data)
    # print("Response:", response)
    if response.status_code == 200:         
        result = response.json()         
        # print("API Response:", result)     
    else:         
        print("API Request Failed. Status Code:", response.status_code)         
        print("Response Content:", response.text)

    placa_match = re.search(r'\b[A-Z]{3}-\d{4}\b', result['body'])

    # Verifique se uma correspondência foi encontrada
    if placa_match:
        placa = placa_match.group(0)
        print('Placa encontrada: ',placa)  # Isso imprimirá a placa encontrada (exemplo: "AVL-8477")
    else:
        print("Placa não encontrada na resposta da API.")

textDetection('car3.png')