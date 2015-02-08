from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, RequestContext


@login_required(login_url='/')
def my_home(request):
    return render_to_response('my-home.html')
