from django.http.response import HttpResponse

def SampleView(request):
    html = '<body><h1>Django Caching<h1><br><p>Welcome to Caching Tutorial</p></body>'
    
    return HttpResponse(html)