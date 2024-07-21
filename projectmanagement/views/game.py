from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projectmanagement.game.factory import GameFactory


@login_required
def game(request):
    context = {}
    game_level = request.GET.get('level', 'default')
    context['game_level'] = game_level
    context['questions'] = GameFactory.start(game_level)

    return render(request, 'game/index.html', context)


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
