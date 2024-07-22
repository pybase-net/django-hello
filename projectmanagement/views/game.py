from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projectmanagement.game.factory import GameFactory


@login_required
def game(request):
    context = {}
    game_level = request.GET.get('level', 'default')
    context['game_level'] = game_level
    current_game = request.session.get('current_game')
    start_game = True if request.POST.get('start_game') else False
    restart = True if request.POST.get('restart') else False
    if not current_game:
        e, game, questions = GameFactory.start(request.user, game_level)
    else:
        e, game, questions = GameFactory.find_game(int(current_game), start_game, restart)
    if not e:
        request.session['current_game'] = game.id
    context['game'] = game
    context['e'] = e
    context['questions'] = questions

    return render(request, 'game/index.html', context)


@login_required
def game_play(request):
    context = {}
    answers = request.POST
    context['answers'] = answers
    return render(request, 'game/game_play.html', context)


@login_required
def game_end(request):
    return render(request, 'game/game_end.html')


@login_required
def game_history(request):
    return render(request, 'game/history.html')


def game_rank(request):
    return render(request, 'game/rank.html')
