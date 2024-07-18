from django.shortcuts import render


def user_profile(request):
    return render(request, 'user/profile.html')


def user_detail(request, user_id: int):
    return render(request, 'user/profile.html')
