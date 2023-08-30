from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.forms import PostForm
from base.models import Post


@login_required(login_url='home')
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)
