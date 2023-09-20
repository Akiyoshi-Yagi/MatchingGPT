from django.shortcuts import render
import openai
from django.conf import settings

openai.api_key = settings.API_KEY
fix = "マッチングアプリで使われるような自己紹介文を、次の情報をもとに生成してください。情報："

def index(request):
    intro_text = ''
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": fix+user_input}, 
        ]
        )

        intro_text = response["choices"][0]["message"]["content"]


    return render(request, 'index.html', {'intro_text': intro_text})
