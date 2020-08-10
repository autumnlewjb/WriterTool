import requests
import io
import base64

def request_body():
    feature = dict(type='DOCUMENT_TEXT_DETECTION', maxResults="", model="builtin/stable")
    feature_list = [feature]
    

    with open('../resources/english.jpg', 'rb') as input_file:
        content = str(base64.encodebytes(input_file.read()))
        print(type(content))
    
    image = dict(content=content)

    annotate_image_request = dict(image=image, features=feature_list)

    return dict(requests=[annotate_image_request])


def make_request():
    endpoint = 'https://vision.googleapis.com/v1/images:annotate'
    response = requests.post(endpoint, data=request_body())
    print(response.status_code)


if __name__ == '__main__':
    make_request()