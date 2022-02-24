import json

import requests
from django.shortcuts import render

from events.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def error(request):
    return render(request, 'error.html', {})


def candidates(request):
    users = User.objects.all()
    return render(request, 'candidates.html', {'Users_list': users})


def result(request):
    # We Get the form's value
    if request.method == 'GET':
        username = request.GET.get('username', '')
        language = request.GET.get('language', '')
        location = request.GET.get('location', '')
        repos = request.GET.get('repos', '')
        count = 0
        flag = True
        list_user = []
        # Url builder we specify that we need 100 people per page maximum amount that can be viewed by the github api
        while (flag):
            count += 1
            url = 'https://api.github.com/search/users?q=' + username + '+location:' + location + '+language:' + language + '+repos:%3E' + repos + '&page=' + str(
                count) + '&per_page=100'
            r = requests.get(url)
            data = r.json()
            jsonString = json.dumps(data)
            with open('json_data.json', 'w') as outfile:
                outfile.write(jsonString)
            outfile.close()
            with open('json_data.json', 'r') as readfile:
                data2 = json.load(readfile)
            readfile.close()
            x = data2['total_count'] - (count * 100)
            if x <= 0:
                flag = False
            for item in data2['items']:
                name = item['login']
                id = item['id']
                avatar = item['avatar_url']
                url = item['html_url']
                user = User(name=name, id=id, avatar=avatar, url=url, language=language, location=location)
                user.save()
                list_user.append(user)
                print("user saved")

        return render(request, "result.html", {'Users_list': list_user})
    else:
        return render(request, "error.html", {})
