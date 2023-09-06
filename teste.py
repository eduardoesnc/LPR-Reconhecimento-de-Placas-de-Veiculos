def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # Extrair a imagem em base64 da solicitação
    image_base64 = event['body']

    # Decodificar a imagem base64
    image_bytes = base64.b64decode(image_base64)

    # Nome do arquivo no bucket S3
    file_name = 'teste3.jpg'

    # Nome do bucket S3
    bucket_name = 'leituradeplacas'

    # Fazer o upload da imagem para o bucket S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=image_bytes)
    
    # response = 'Imagem enviada para o S3 com sucesso!'
    
    client = boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket_name, 'Name': file_name}})

    # placas = [placa['DetectedText']] for placa in response['TextDetections']]
    
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({
    #         'mesage': 'Ok!',
    #         'placas': placas
    #     })
    # }
    return{
        'statusCode': 200,
        'body': json.dumps(response)
    }