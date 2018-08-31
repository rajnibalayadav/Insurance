from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This  will be a list of all bowlers</h1>")

def detail(request,bowler_id):
    return HttpResponse("<h2>Details for Bowler Id:" +str(bowler_id)+"</h2>")