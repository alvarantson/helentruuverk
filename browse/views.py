from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, social_media
from .models import browse_lang
# Create your views here.
def browse(request):
#	print(request.user.is_authenticated)
#	if request.user.is_authenticated == False:
#		return HttpResponseRedirect('/admin')
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('browse/') #browse\i puhul '/'

	return render(request, 'browse.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang':browse_lang.objects.get(lang=request.session['lang']),
		'social_media': social_media.objects.all()
		})