from django.shortcuts import render
import requests

def getUserFriends(token:str):
    resp=requests.get('https://api.vk.com/method/friends.get?v=5.52&access_token={}&count=1000000'.format(token))
    friends=resp.json()

    return friends.get('response').get('count')

def index(request):
    context={"is_authenticated":False}
    return render(request, 'index.html', context)

def getUserInfo(token:str):
    resp= requests.get('https://api.vk.com/method/users.get?v=5.52&access_token={}&fields=photo_max&name_case=nom'.format(token))
    userInfo=resp.json()
    return  userInfo

def search(token:str,query:str):
    resp=requests.get('https://api.vk.com/method/friends.search?v=5.52&access_token={}&q={}&fields=nickname'.format(token,query))
    queryResult=resp.json().get('response').get('items')


def callback(request):
    code=request.GET.get('code')
    resp=requests.get('https://oauth.vk.com/access_token?client_id=7396296&client_secret=hcSFV9SDvpLw19NdiwrX&redirect_uri=https://vladtestvk.herokuapp.com/callback&code={}'.format(code))
    token=resp.json()
    context={"user_token":token.get('access_token'),"user_id":token.get('user_id')}
    if context.get('user_token') != None:
        userInfo= getUserInfo(context['user_token'])
        context['username']=userInfo.get('response')[0].get('first_name')+' '+userInfo.get('response')[0].get('last_name')
        context['photo']=userInfo.get('response')[0].get('photo_max')
        context['friends_count']=getUserFriends(context['user_token'])
    return render(request,'callback.html',context)

def enterToAccount(request):
    auth=request.GET.get('auth')
    context = {"is_authenticated": False}
    query=request.GET.get('search')
    if query!=None:
        result=search()
    if auth=='true':
        context["is_authenticated"]=True
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)