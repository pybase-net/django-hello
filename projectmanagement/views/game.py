from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def game(request):
    return render(request, 'game/index.html')


@login_required
def game_play(request):
    return render(request, 'game/game_play.html')


@login_required
def game_end(request):
    return render(request, 'game/game_end.html')


@login_required
def game_history(request):
    return render(request, 'game/history.html')


def game_rank(request):
    return render(request, 'game/rank.html')
