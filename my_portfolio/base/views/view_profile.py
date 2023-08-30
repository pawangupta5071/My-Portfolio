from django.shortcuts import render


def view_profile(request):
    return render(request, 'base/profile.html')
