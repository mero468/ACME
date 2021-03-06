import json

import requests
from django.shortcuts import render, redirect

from events.models import Candidates


# Create your views here.
def home(request):
    XD=True
    return render(request, 'home.html', {"XD":XD})


def error(request):
    return render(request, 'error.html', {})


def candidates(request):
    users = Candidates.objects.all()
    return render(request, 'candidates.html', {'Users_list': users})

def delete_cand(request,user_id):
    object = Candidates.objects.get(pk=user_id)
    object.delete()
    users = Candidates.objects.all()
    return redirect('home')
def result(request):
    # We Get the form's value
    if request.method == 'GET':
        username = request.GET.get('username', '')
        language = request.GET.get('language', '')
        location = request.GET.get('location', '')
        repos = request.GET.get('repos', '')
        count = 0
        flag = True
        if (username == '') or (len(username) <= 1):
            XD = False
            return render(request, 'home.html', {"XD": XD})

        list_user = []
        # Url builder we specify that we need 100 people per page maximum amount that can be viewed by the github api
        # Github's api is limited for 10 requests 1000 users only thats why be specific in your searches
        #search api
        url = 'https://api.github.com/search/users?q=' + username + '+location:' + location + '+language:' + language + '+repos:%3E' + repos + '&page=1' + '&per_page=100'
        r = requests.get(url)
        data = r.json()
        jsonString = json.dumps(data)
        with open('json_data.json', 'w') as outfile:
            outfile.write(jsonString)
        outfile.close()
        with open('json_data.json', 'r') as readfile:
            data2 = json.load(readfile)
        readfile.close()
        if "message" in data2:
            return render(request, "error.html", {})
        if "total_count" in data2:
            for item in data2['items']:
                readfile.close()
                login = item['login']
                id = item['id']
                avatar = item['avatar_url']
                url = item['html_url']
                email = ''
                name = ''
                user = Candidates(login=login ,name=name, email=email, id=id, avatar=avatar, url=url, location=location)
                user.save()
                list_user.append(user)
        return render(request, "result.html", {'Users_list': list_user})