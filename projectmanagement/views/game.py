from django.shortcuts import render


def game(request):
    return render(request, 'game/index.html')


def game_play(request):
    return render(request, 'game/game_play.html')


def game_end(request):
    return render(request, 'game/game_end.html')


def game_history(request):
    return render(request, 'game/history.html')


def game_rank(request):
    return render(request, 'game/rank.html')
