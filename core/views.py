from django.shortcuts import render

# Create your views here.
# app/views.py
from django.views.generic import TemplateView

class ControlPageView(TemplateView):
    template_name = 'index.html'
class Oproekte(TemplateView):
    template_name = 'oproekte.html'

def game(request):
    return render(request, 'shariki_fanariki.html' )

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameScore
import json

@csrf_exempt
def submit_score(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            score = GameScore(
                player_name=data['name'],
                score=data['score']
            )
            score.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=405)

def leaderboard(request):
    scores = GameScore.objects.all().order_by('-score')[:10]  # Топ-10 результатов
    data = [{
        'name': score.player_name,
        'score': score.score,
        'date': score.date.strftime('%Y-%m-%d %H:%M')
    } for score in scores]
    return JsonResponse(data, safe=False)