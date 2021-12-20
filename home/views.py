from django.db.models.fields import NullBooleanField
from django.http import response
from django.shortcuts import render
from home.models import users
from django.template.defaulttags import register
from home.models import stackusers
import requests

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def get_item(dictionary, key):
    return dictionary.get(key)

def firstpage(request):
    return render(request, "firstpage.html")

def index(request):
    result = requests.get('https://api.github.com/users/').json()
    return render(request, "index.html", {'response': result})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        response = requests.get('https://api.github.com/users/' + str(search)).json()
        if  len(str(response)) < 100  :
             return render(request, "searchbar.html", {'response': response})  
        else:     
            saveRecord = users()
            saveRecord.loginname = response['login']
            saveRecord.username = response['name']
            saveRecord.locationu = response['location']
            saveRecord.company = response['company']
            saveRecord.repos = response['public_repos']
            saveRecord.gists = response['public_gists']
            saveRecord.followers = response['followers']
            saveRecord.followingu = response['following']
            saveRecord.htmlurl = response['html_url']
            saveRecord.save()
            return render(request, "searchbar.html", {'response': response})    

def stackindex(request):
    return render(request, "stackindex.html")


def stacksearchbar(request):
    search = request.GET.get('search')
    getter = requests.get('https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&inname=' + str(search) +'&site=stackoverflow').json()
    items = getter['items']
    response = "none"
    if len(items) == 0:
        return render(request, "stacksearchbar.html")   
    else:
        response = items[0]
        saveRecord = stackusers()
        saveRecord.stackname = response['display_name']
        saveRecord.isemployee = response['is_employee']
        saveRecord.reputation = response['reputation']
        saveRecord.weeklyrepchange = response['reputation_change_week']
        saveRecord.monthlyrepchange = response['reputation_change_month']
        saveRecord.linkurl = response['link']
        saveRecord.save()
        return render(request, "stacksearchbar.html", {'response': response})        