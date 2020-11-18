from django.http import HttpResponse



def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    rse = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval :
        rse.set_cookie('zap', int(oldval)+1) 
    else :
        rse.set_cookie('zap', 42) 
    rse.set_cookie('sakaicar', 42, max_age=1000) 
    return rse


def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    rse = HttpResponse('view count='+str(num_visits))
    rse.set_cookie('dj4e_cookie', '4ac77841', max_age=1000)
    return rse