from requests import get
from IPython.display import display, HTML

def request_dog():
    dog_request = 'https://dog.ceo/api/breeds/image/random'
    response = get(dog_request)
    data = response.json()
    return data

def render_dog(response):
    image_https = response['message']
    template = '''
    <center><h1> A Random Dog</h1></center><br><center><img src={} style="width:300px;"></center>'''
    display(HTML(template.format(image_https)))
    
def random_dog():
    api_request = request_dog()
    render_dog(api_request)