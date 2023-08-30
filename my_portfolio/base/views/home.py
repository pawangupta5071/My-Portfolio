from django.shortcuts import render
from base.models import Post


def home(request):

    posts = Post.objects.filter(active=True, features=True)[0:3]
    context = {'posts': posts}
    return render(request, 'base/index.html', context)
