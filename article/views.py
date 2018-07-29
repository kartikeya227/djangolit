from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        branch = request.POST['branch']
        year = request.POST['year']
        content = request.POST['content']
        obj = VisitorRecord.objects.create(name=name, branch=branch, year=year, content=content)
        obj.save()
    visitorRecord = VisitorRecord.objects.all().order_by('-pk')
    articleRecord = ArticleRecord.objects.all().order_by('-pk')
    return render(request, "index.html", {'vr':visitorRecord , 'ar':articleRecord})
