from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def getUserFriends(id):
    print('test')

def index(request):
    if request.user.is_authenticated:
        dict = request.user.get_full_name()
        user = SocialAccount.objects.get(user__username=request.user.username)
        user_uid = user.uid
        user_friends = getUserFriends(user_uid)
    else:
        dict = 'Unknow username'
        user_friends = ''
    context = {
        'username': dict,
        'user_friends': user_friends
    }
    return render(request, 'index.html', context)
