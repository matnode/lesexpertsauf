# -*- encoding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from experts.models import Human, Competence, Mission, Formation
from django.utils import timezone
import random, sha, string


def index(request):	
	#on demarre le processus dauthentification des utilisateurs
    message=""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                  login(request, user)
                  return HttpResponseRedirect(reverse('experts.views.acceuil'))
            else:
                  message ='<div class="alert alert-danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close">&times;</button> Votre comte a été desactivé </div>'
        else:
             message ='<div class="alert alert-danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close">&times;</button> email ou mot de passe incorrecte </div>'
	
    return render_to_response("../templates/connexion.html",{'message':message}, context_instance=RequestContext(request))

def deconnexion(request):
	logout(request)
	return HttpResponseRedirect(reverse(index))



def inscription(request):	
	#On demarre avec le traitement des informations concernants     l'enregistrement d'un user
	if request.method =='POST':
           
            user = User.objects.create_user(
                    username = request.POST['username'],
                    email = request.POST['email'],
                   password = request.POST['password'],
                 ) 
                                
            human = Human(
                  user= user,
                  datecreation = timezone.now(),
                  #par defaut on initialise certain champ qui ne peuvent pas avoir une valeur null
                  online=0,
                  telephone=0,
                  datenaissance=" ",
                  
           )
                	
            human.save()
            	
            return HttpResponseRedirect(reverse(index))
	return render_to_response("../templates/inscription.html", context_instance=RequestContext(request))
	
def acceuil(request):	
	# on est sur la page d'acceuil
	#on envoi sur les informations de l'utilisateur courant
	
	currentuser =request
	
	return render_to_response("../templates/acceuil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profil(request,user_id):	
	# on est sur la page de profil
	#on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	#on reccupère les competences de l'utilisateur courant
	competenceuser = Competence.objects.filter(human=currentuser.user.human.id)
	countcompetence = competenceuser.count()
	#on reccupère les missions de l'utilisateur courant
	missionuser = Mission.objects.filter(human=currentuser.user.human.id)
	countmission = missionuser.count()
	#on reccupère les formations de l'utilisateur courant
	formationuser = Formation.objects.filter(human=currentuser.user.human.id)
	countformation = formationuser.count()
        if request.method== 'POST':
            if request.POST['nom']:        
                human.civilite = request.POST['civilite']
                human.nom = request.POST['nom']
                human.prenom = request.POST['prenom']
                human.datenaissance = request.POST['dateanniv']
                human.signature = request.POST['signature']                
            
        human.save()
	return render_to_response("../templates/profil.html",
	                          {'currentuser':currentuser,
	                           'countcompetence':countcompetence,
	                           'competenceuser':competenceuser,
	                           'missionuser':missionuser,
	                           'countmission':countmission,
	                           'formationuser':formationuser,
	                           'countformation':countformation}, 
	                           context_instance=RequestContext(request))
	
def profilcords(request,user_id):	
	# on est sur la page de profil
	#on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
        if request.method== 'POST':
                           
            if request.POST['telephone']:            
                human.siteweb = request.POST['siteweb']
                human.telephone = request.POST['telephone']
                human.adresse = request.POST['adresse']
                human.codepostale = request.POST['bp']
                human.ville = request.POST['ville']
                
        human.save()
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profilcompetence(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
                           
            if request.POST['titre']:
             competence = Competence( 
                human= human,           
                nom = request.POST['titre'],
                description = request.POST['description']
            )
                               
             competence.save()
             return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def modprofilcompetence(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	competenceuser = Competence.objects.filter(human=currentuser.user.human.id)
        if request.method== 'POST':
                           
            if request.POST['titre']:
                competenceuser = Competence.objects.get(pk=request.POST['idcompetence'])            
                competenceuser.nom = request.POST['titre']
                competenceuser.description = request.POST['description']
                competenceuser.save()
            return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))
	
	
def delprofilcompetence(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
        if request.method== 'POST':
             competenceuser = Competence.objects.get(pk=request.POST['idcompetencetodel'])
             competenceuser.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))
	
def profilmission(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
                                   
            if request.POST['titre']:
             mission = Mission( 
                human= human,           
                datedebut = request.POST['datedebut'],
                datefin = request.POST['datefin'],
                titre = request.POST['titre'],
                fonction = request.POST['fonction'],
                entreprise = request.POST['entreprise'],
                description = request.POST['description'],
                competenceutilisee = request.POST['competence']
            )
                               
             mission.save()
             return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profilformation(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
                                   
            if request.POST['titre']:
             formation = Formation( 
                human= human,           
                datedebut = request.POST['datedebut'],
                datefin = request.POST['datefin'],
                intitule = request.POST['titre'],
                lieu = request.POST['lieu'],
                ecole = request.POST['ecole'],
                diplome = request.POST['diplome'],
                description = request.POST['description']
            )
                               
             formation.save()
             return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))
