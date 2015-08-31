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
from experts.models import Human, Competence, Mission, Formation, Langue, Loisir
from django.utils import timezone
from django.core import serializers
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
	#on reccupère les langues de l'utilisateur courant
	langueuser = Langue.objects.filter(human=currentuser.user.human.id)
	countlangue = langueuser.count()
	#on reccupère les loisirs de l'utilisateur courant
	loisiruser = Loisir.objects.filter(human=currentuser.user.human.id)
	countloisir = loisiruser.count()

	return render_to_response("../templates/profil.html",
	                          {'currentuser':currentuser,
	                           'countcompetence':countcompetence,
	                           'competenceuser':competenceuser,
	                           'missionuser':missionuser,
	                           'countmission':countmission,
	                           'formationuser':formationuser,
	                           'countformation':countformation,
	                           'langueuser':langueuser,
	                           'countlangue':countlangue,
	                           'loisiruser':loisiruser,
	                           'countloisir':countloisir}, 
	                           context_instance=RequestContext(request))
	
def profilinfo(request,user_id):	
	# on est sur la page de profil
	#on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
        if request.method== 'POST':
            if request.POST['nom'] != "":        
                human.civilite = request.POST['civilite']
                human.nom = request.POST['nom']
                human.prenom = request.POST['prenom']
                human.datenaissance = request.POST['dateanniv']
                human.signature = request.POST['signature']
        human.save()
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))
	
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

def modprofilmission(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	if request.method== 'POST':
	    mission = Mission.objects.get(pk=request.POST['idthismission'])
	    if request.POST['titre']:
	        mission.datedebut = request.POST['datedebut']
	        mission.datefin = request.POST['datefin']
	        mission.titre = request.POST['titre']
	        mission.fonction = request.POST['fonction']
	        mission.entreprise = request.POST['entreprise']
	        mission.description = request.POST['description']
	        mission.competenceutilisee = request.POST['competence']
	        mission.save()
            return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def delprofilmission(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
        if request.method== 'POST':
             missionuser = Mission.objects.get(pk=request.POST['idmissiontodel'])
             missionuser.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
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

def modprofilformation(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	if request.method== 'POST':
	    formation = Formation.objects.get(pk=request.POST['idthisformation'])
	    if request.POST['titre']:
	        formation.datedebut = request.POST['datedebut']
	        formation.datefin = request.POST['datefin']
	        formation.intitule = request.POST['titre']
	        formation.diplome = request.POST['diplome']
	        formation.ecole = request.POST['ecole']
	        formation.lieu = request.POST['lieu']
	        formation.description = request.POST['description']
	        formation.save()
            return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))



def delprofilformation(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
        if request.method== 'POST':
             formationuser = Formation.objects.get(pk=request.POST['idformationtodel'])
             formationuser.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profilangue(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
                           
            if request.POST['nom']:
             langue = Langue( 
                human= human,           
                nom = request.POST['nom'],
                niveau = request.POST['niveau']
            )
                               
             langue.save()
             return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def modprofilangue(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
            langue = Langue.objects.get(pk=request.POST['idthislangue'])              
            if request.POST['nom']:       
                langue.nom = request.POST['nom'],
                langue.niveau = request.POST['niveau']
                                           
            langue.save()
            return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def delprofilangue(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	if request.method== 'POST':
           langueuser = Langue.objects.get(pk=request.POST['idlanguetodel'])
           langueuser.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profiloisir(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
                           
            if request.POST['nom']:
             loisir = Loisir( 
                human= human,           
                titre = request.POST['nom'],
                description = request.POST['description']
            )
                               
             loisir.save()
             return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def modprofiloisir(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	
        if request.method== 'POST':
            loisir = Loisir.objects.get(pk=request.POST['idthisloisir'])              
            if request.POST['nom']:       
                loisir.nom = request.POST['nom'],
                loisir.description = request.POST['description']
                                           
            loisir.save()
            return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def delprofiloisir(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human= Human.objects.get(pk=currentuser.user.human.id)
	if request.method== 'POST':
           loisiruser = Loisir.objects.get(pk=request.POST['idloisirtodel'])
           loisiruser.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
	return render_to_response("../templates/profil.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def lesexperts(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	human = Human.objects.all()
	if request.method== 'POST':
	    human = User.objects.filter(username__contains=request.POST['username'])
	return render_to_response("../templates/listexpert.html",{'currentuser':currentuser,'human': human}, context_instance=RequestContext(request))
	
def voirlesexperts(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	if request.method== 'POST':
	    cesexperts = User.objects.filter(username__contains=request.POST['username'])
	
	return render_to_response("../templates/searchexpert.html",{'currentuser':currentuser,'cesexperts':cesexperts}, context_instance=RequestContext(request))
	
def voirlesexperts(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	if request.method== 'POST':
	    cesexperts = User.objects.filter(username__contains=request.POST['username'])
	
	return render_to_response("../templates/searchexpert.html",{'currentuser':currentuser,'cesexperts':cesexperts}, context_instance=RequestContext(request))

def detailexpert(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	cetexpert=0
	
	cetexpert = User.objects.get(pk=user_id)
	#on reccupère les competences de l'utilisateur 
	competenceuser = Competence.objects.filter(human=cetexpert.human.id)
	countcompetence = competenceuser.count()
	#on reccupère les missions de l'utilisateur 
	missionuser = Mission.objects.filter(human=cetexpert.human.id)
	countmission = missionuser.count()
	#on reccupère les formations de l'utilisateur
	formationuser = Formation.objects.filter(human=cetexpert.human.id)
	countformation = formationuser.count()
	#on reccupère les langues de l'utilisateur courant
	langueuser = Langue.objects.filter(human=cetexpert.human.id)
	countlangue = langueuser.count()
	#on reccupère les loisirs de l'utilisateur courant
	loisiruser = Loisir.objects.filter(human=cetexpert.human.id)
	countloisir = loisiruser.count()
	
	return render_to_response("../templates/detailexpert.html",{
	'currentuser':currentuser,
	'cetexpert':cetexpert,
	'competenceuser':competenceuser,
	'countcompetence':countcompetence,
	'missionuser':missionuser,
	'countmission':countmission,
	'formationuser':formationuser,
	'countformation':countformation,
	'langueuser':langueuser,
	'countlangue':countlangue,
	'loisiruser':loisiruser,
	'countloisir':countloisir}, context_instance=RequestContext(request))
	
def reglages(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	user= User.objects.get(pk=currentuser.user.id)
	message=""
	
        if request.method== 'POST':             
            if request.POST['username']:       
                user.username = request.POST['username']
                message="votre nom d'utilisateur a été mis à jour"                                           
                user.save()
                return HttpResponseRedirect(reverse('experts.views.reglages'))
	return render_to_response("../templates/reglages.html",
	{'currentuser':currentuser,
	'message':message}, 
	 context_instance=RequestContext(request))

def motdepasse(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	user= User.objects.get(username__exact=currentuser.user.username)
	message=""
        if request.method== 'POST':             
            if request.POST['password'] != request.POST['confpassword']:
                message="les mots de passe ne correspondes pas"
            else:
                user.set_password(request.POST['password'])
                message="mot de passe modifié avec succès"
                user.save()
	return render_to_response("../templates/reglages.html",
	{'currentuser':currentuser,
	 'message':message
	}, context_instance=RequestContext(request))
