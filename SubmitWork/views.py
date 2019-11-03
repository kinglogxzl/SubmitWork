from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from SubmitWork import settings
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.forms.models import model_to_dict
import json, os
import threading
from datetime import datetime, timedelta
import time
from django.shortcuts import redirect
import django.utils.timezone
import time


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def submit_file(request):
    if request.method == 'GET':
        return render(request, 'entity/train_model.html')
    else:
        print(request.POST)
        myfile = request.FILES.get('input_data')
        filename = myfile.name
        print(filename)

        # 文件路径
        filepath = os.path.join(settings.UPLOAD_DIR, filename)
        f = open(filepath, 'wb')
        for i in myfile.chunks():
            f.write(i)
        f.close()
        time.sleep(5)
        return render (request, 'result.html')
        #return redirect ('/entity')
        # return render(request, 'entity/index.html')
