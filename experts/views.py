# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from experts.models import Human
from django.utils import timezone
import random, sha, string


def index(request):	
	#On demarre avec le traitement des informations concernants l'enregistrement d'un user
	
	#return HttpResponse("Hello, world. You're at the experts index.")
	return render_to_response("../templates/connexion.html", context_instance=RequestContext(request))

def inscription(request):	
	#On demarre avec le traitement des informations concernants l'enregistrement d'un user
	
	#return HttpResponse("Hello, world. You're at the experts index.")
	return render_to_response("../templates/inscription.html", context_instance=RequestContext(request))
