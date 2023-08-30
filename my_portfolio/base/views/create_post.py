from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.forms import PostForm


@login_required(login_url='home')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)
