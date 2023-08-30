from django.shortcuts import render

from base.models import Post


def view_post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'base/project.html', context)
