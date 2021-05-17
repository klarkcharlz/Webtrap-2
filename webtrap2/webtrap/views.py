from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from loguru import logger
from datetime import datetime


logger.add('log/webtrap2/webtrap2.log', format='{time} {level} {message}', level='DEBUG')


# Create your views here.
@csrf_exempt
def main(request):
    if request.method == "POST":
        data = request.POST
        log_data = {
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'url': request.path,
            'method': request.method,
            'status': 200,
            'params': data.get("email", None)
        }

        logger.info(log_data)
    return render(request, 'webtrap/main.html')


@csrf_exempt
def api(request):
    if request.method == "GET":
        status = 404
    elif request.method == "POST":
        data = json.loads(request.body)
        if data.get('method', None) == 'ping':
            status = 200
        else:
            status = 400
    else:
        return HttpResponse("INVALID METHOD")

    log_data = {
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'url': request.path,
        'method': request.method,
        'status': status,
        'params': data if request.method == "POST" else dict(request.GET)
    }

    logger.info(log_data)

    return HttpResponse(status=status)
