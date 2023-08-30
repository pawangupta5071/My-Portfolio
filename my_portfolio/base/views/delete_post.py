from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import Post


@login_required(login_url='home')
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'item': post}
    return render(request, 'base/delete.html', context)
