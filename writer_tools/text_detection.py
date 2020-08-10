import requests
import io
import base64
import json

def request_body():
    feature = dict(type='DOCUMENT_TEXT_DETECTION', maxResults="1", model="builtin/stable")
    feature_list = [feature]
    

    with open('resources/english.jpg', 'rb') as input_file:
        content = base64.b64encode(input_file.read()).decode('ascii')
        print(type(content))
    
    image = dict(content=content)

    annotate_image_request = dict(image=image, features=feature_list)

    return dict(requests=[annotate_image_request])


def authenticate():
    with open('resources/api.txt', 'r') as api_file:
        api = api_file.read()

    return str(api)


def make_request():
    endpoint = 'https://vision.googleapis.com/v1/images:annotate'
    response = requests.post(endpoint, json=request_body(), params={'key': authenticate()})
    
    return response.json()


def record_response(response):
    with open('resources/response.json', 'w') as json_file:
        json.dump(response, json_file)


def get_text(response):
    text = response['responses'][0]['textAnnotations'][0]["description"]
    return text


if __name__ == '__main__':
    response = make_request()
    print(get_text(response))