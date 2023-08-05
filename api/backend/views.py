from django.http import HttpResponse
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view


def make_post_call(plan):
    
    # Replace the following URL with the endpoint of the API you want to make a POST call to.
    url = 'https://www.licpremiumcalculator.in/forms/plan'+plan+'.php'
    print(url)
    # Make the POST request and get the response.
    response = requests.post(url)
    print(response)
    # Check if the request was successful and the response has content.
    if response.status_code == 200 and response.content:
        return response.content
    else:
        # If there's an error or empty response, return a default message.
        return b"Unable to fetch HTML page."

def get_api_call(request):
    # Call the function to make the POST API call.
    plan = request.GET.get('plan')
    html_page = make_post_call(plan)
    
    # Return the HTML page as a response.
    return HttpResponse(html_page, content_type='text/html')

@api_view(['POST'])
def calculate(request):
    html_page = get_premium(request)

    return HttpResponse(html_page, content_type='text/html')
    
def get_premium(request):

    params = request.data
    plan = request.data.get('table')
    print(plan)
    api_url = 'https://www.licpremiumcalculator.in/calc/calc'+plan+'.php'

    # Make the POST request and get the response.
    response = requests.post(api_url, data=params)
    print(response)
    # Check if the request was successful and the response has content.
    if response.status_code == 200 and response.content:
        return response.content
    else:
        # If there's an error or empty response, return a default message.
        return b"Unable to fetch HTML page."
