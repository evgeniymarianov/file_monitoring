from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Document

@csrf_exempt
def upload_file(request):
    documents = Document.objects.all()
    print('Beg!!!!!!!!!!!!!!!!!!!!!!!!')
    if request.method=='GET':
        return render(request, 'main/index.html')
    if request.method=='POST':
        uploaded_file = Document(
            description = 'default_description',
            document = request.FILES['uploaded_file']
        )
        uploaded_file.save()
        return render(request, 'dashboard.html', {'documents': documents})
