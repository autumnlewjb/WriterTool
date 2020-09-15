import requests
import io
import base64
import json

def _request_body(annotate_image_request):
    total_request = []
    for request in annotate_image_request:
        total_request.append(request)
    
    return dict(requests=total_request)


def make_image_request(filename):
    feature = dict(type='DOCUMENT_TEXT_DETECTION', maxResults="1", model="builtin/stable")
    feature_list = [feature]
    

    with open(f'resources/{filename}.jpg', 'rb') as input_file:
        content = base64.b64encode(input_file.read()).decode('ascii')
        print(type(content))
    
    image = dict(content=content)

    annotate_image_request = dict(image=image, features=feature_list)

    return annotate_image_request


def authenticate():
    with open('resources/api.txt', 'r') as api_file:
        api = api_file.read()

    return str(api)


def make_request(annotate_image_request):
    endpoint = 'https://vision.googleapis.com/v1/images:annotate'
    response = requests.post(endpoint, json=_request_body(annotate_image_request), params={'key': authenticate()})
    
    return response.json()


def record_response(response):
    with open('resources/response.json', 'w') as json_file:
        json.dump(response, json_file)


def record_text(text_list):
    index = 1
    for text in text_list:
        with open(f'resources/output/output-{index}.txt', 'w+') as output_file:
            output_file.write(text)
        index += 1
    print('done')


def get_text(responses):
    result = []
    for response in responses['responses']:
        text = response['fullTextAnnotation']['text']
        result.append(text)

    return result


if __name__ == '__main__':
    filenames = ['question1', 'question2', 'passage1', 'passage2']
    annotate_image_requests = []
    for filename in filenames:
        annotate_image_requests.append(make_image_request(filename))
    
    responses = make_request(annotate_image_requests)
    text_list = get_text(responses)
    record_text(text_list)