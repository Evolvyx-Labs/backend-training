from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services.do_cal import exp_parser
from.models import Calculations
from django.forms.models import model_to_dict


@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        expression = data.get('expression')
        try:
            result = exp_parser(expression)
            new_record = Calculations.objects.create(given_expression=expression, end_result= result[0])
            return JsonResponse({'result': result[0]})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def history(request):
    records = Calculations.objects.all().order_by ('-created_at')
    records_dict= [model_to_dict(record) for record in records]
    return JsonResponse({'records': records_dict})

@csrf_exempt
def delete_record(request, exp_id):
    record = get_object_or_404(Calculations,id = exp_id)
    record.delete()
    return JsonResponse({'id':exp_id})












import random
from math import ceil, log2
from .models import Match

def generate_single_elimination_bracket(knights, event):

    random.shuffle(knights)


    total_players = len(knights)
    total_slots = 2 ** ceil(log2(total_players))

    
    while len(knights) < total_slots:
        knights.append(None)

    matches = []
    round_number = 1

    for i in range(0, len(knights), 2):
        k1 = knights[i]
        k2 = knights[i + 1]

        match = Match.objects.create(
            event=event,
            round=round_number,
            knight1=k1,
            knight2=k2,
        )
        matches.append(match)

    tournament.bracket_generated = True
    tournament.save()

    return matches










from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Tournament, Knight
from .services.bracket_generator import generate_single_elimination_bracket

def generate_bracket_view(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if tournament.bracket_generated:
        return JsonResponse({'error': 'Bracket already generated.'}, status=400)

    knights = list(Knight.objects.all())  # or filter by tournament if needed

    matches = generate_single_elimination_bracket(knights, tournament)

    return JsonResponse({
        'message': 'Bracket generated',
        'matches_created': len(matches),
    })










from .models import Match

def advance_to_next_round(tournament, current_round):
    current_matches = Match.objects.filter(tournament=tournament, round=current_round)

    winners = [m.winner for m in current_matches if m.winner is not None]

    next_round = current_round + 1

    for i in range(0, len(winners), 2):
        Match.objects.create(
            tournament=tournament,
            round=next_round,
            knight1=winners[i],
            knight2=winners[i + 1] if i + 1 < len(winners) else None
        )
