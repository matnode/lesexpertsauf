# -*- encoding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404,render
from django.template import RequestContext, loader, Context
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from experts.models import Human, Competence, Mission, Formation, Langue, Loisir, Typecompte, Entreprise, Offre
from django.utils import timezone
from django.core import serializers
import random, sha, string, json


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
                  return HttpResponseRedirect(reverse('experts.views.routeur'))
            else:
                  message ='<div class="alert alert-danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close">&times;</button> Votre comte a été desactivé </div>'
        else:
             message ='<div class="alert alert-danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close">&times;</button> email ou mot de passe incorrecte </div>'
	
    return render_to_response("../templates/connexion.html",{'message':message}, context_instance=RequestContext(request))

def deconnexion(request):
	logout(request)
	return HttpResponseRedirect(reverse(index))

def routeur(request):	
	#On demarre avec le traitement des informations concernants     l'enregistrement d'un user
    currentuser = request
   
    return HttpResponseRedirect(reverse(acceuil))
   

def inscription(request):	
	#On demarre avec le traitement des informations concernants     l'enregistrement d'un user
	if request.method =='POST':
           
            user = User.objects.create_user(
                    username = request.POST['username'],
                    email = request.POST['email'],
                    password = request.POST['password'],
                 ) 
                  
            if request.POST['profil'] =="Expert":              
                 human = Human(
                          user= user,
                          datecreation = timezone.now(),
                          #par defaut on initialise certain champ qui ne peuvent pas avoir une valeur null
                          online=0,
                          telephone=0,
                          datenaissance=" ",    
                    )
                 human.save()
                 
                 typedecompte = Typecompte (
                    user = user,
                    typedecompte = request.POST['profil'],
                 )
                 typedecompte.save()  
                   
            else:
            #on initialise juste on le remplira plustard
                entreprise = Entreprise(
                        user = user,
                        telephone=0,
                        ville="",
                )
                entreprise.save()
                
                typedecompte = Typecompte (
                    user = user,
                    typedecompte = request.POST['profil'],
                  
               )
                typedecompte.save()          
            return HttpResponseRedirect(reverse(index))
           
            
	return render_to_response("../templates/inscription.html", context_instance=RequestContext(request))
	
def acceuil(request):	
	# on est sur la page d'acceuil
	#on envoi sur les informations de l'utilisateur courant
	
	currentuser =request
	
	# on compte le nombre d'expert
	experts= Typecompte.objects.filter(typedecompte="Expert")
	countexpert= experts.count()
	
	# on compte le nombre d'entreprise
	entreprises= Typecompte.objects.filter(typedecompte="Entreprise")
	countentreprise= entreprises.count()
	
	#on compte le nombre d'opportunité 
	offres = Offre.objects.all()
	countoffre = offres.count()
	
	return render_to_response("../templates/acceuil.html",{
	'currentuser':currentuser,
	'countexpert':countexpert,
	'countentreprise':countentreprise,
	'countoffre':countoffre
	}, context_instance=RequestContext(request))

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
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	   
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
                human.pays = request.POST['pays']
                
        human.save()
        return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	
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
                nomlangue = request.POST['nom'],
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
                langue.nomlangue = request.POST['nom'],
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
	
def recherchedesdonnees(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	typedecompte='';
	cesexperts='';
	countdonnee='';
	if request.method== 'POST':
	    typedecompte=request.POST['typedecompte']
	    if request.POST['typedecompte'] == 'Offre':   
	        lesoffres = Offre.objects.filter(intitule=request.POST['donnee'])
	         
	        return render_to_response('../templates/listeoffre.html', {'currentuser':currentuser,'lesoffres': lesoffres},context_instance=RequestContext(request))
	    else:	    
	        cesexperts = User.objects.filter(username__contains=request.POST['donnee'])
	        countdonnee=cesexperts.count()
	
	return render_to_response("../templates/searchexpert.html",{
	                                                            'countdonnee':countdonnee,
	                                                            'currentuser':currentuser,
	                                                            'typedecompte':typedecompte,
	                                                            'cesexperts':cesexperts}, context_instance=RequestContext(request))
	


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

def profilentreprise(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	user= User.objects.get(pk=currentuser.user.id)
	

	return render_to_response("../templates/profilentreprise.html",{'currentuser':currentuser}, context_instance=RequestContext(request))

def profilentrepriseinfo(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	entreprise= Entreprise.objects.get(pk=currentuser.user.entreprise.id)
	
	
        if request.method== 'POST':             
            if request.POST['nom']: 
                                
                   entreprise.nom = request.POST['nom']
                   entreprise.datedefondation = request.POST['datefondation']
                   entreprise.taille = request.POST['taillentreprise']  
                   entreprise.save()
                   return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
                 
	return render_to_response("../templates/profilentreprise.html",
	{'currentuser':currentuser}, 
	 context_instance=RequestContext(request))

def profilentrepriseactivite(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	entreprise= Entreprise.objects.get(pk=currentuser.user.entreprise.id)
	
	
        if request.method== 'POST':             
            if request.POST['activite']:
                   entreprise.activite = request.POST['activite']           
                   entreprise.save()
                   return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
                 
	return render_to_response("../templates/profilentreprise.html",
	{'currentuser':currentuser}, 
	 context_instance=RequestContext(request))

def profilentreprisedescription(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	entreprise= Entreprise.objects.get(pk=currentuser.user.entreprise.id)
	
	
        if request.method== 'POST':
            if request.POST['description']:
                   entreprise.description = request.POST['description']
                   entreprise.save()
                   return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
                 
	return render_to_response("../templates/profilentreprise.html",
	{'currentuser':currentuser}, 
	 context_instance=RequestContext(request))
	 
def profilentreprisecoord(request):	
	# on est sur la page de reglage
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	entreprise= Entreprise.objects.get(pk=currentuser.user.entreprise.id)
	
	
        if request.method== 'POST':             
            if request.POST['telephone']: 
                            
                    entreprise.telephone = request.POST['telephone']
                    entreprise.siteweb = request.POST['siteweb']
                    entreprise.codepostale = request.POST['codepostale']
                    entreprise.ville = request.POST['ville'] 
                    entreprise.adresse = request.POST['adresse']                  
                    entreprise.save()
                    return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
                 
	return render_to_response("../templates/profilentreprise.html",
	{'currentuser':currentuser}, 
	 context_instance=RequestContext(request))

def listentreprise(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	lesentreprises = Entreprise.objects.all()
	
	return render_to_response("../templates/listentreprise.html",{'currentuser':currentuser,'lesentreprises': lesentreprises}, context_instance=RequestContext(request))
	
def detailentreprise(request,user_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	entreprise = Entreprise.objects.get(pk=user_id)
	
	return render_to_response("../templates/detailentreprise.html",{'currentuser':currentuser,'entreprise': entreprise}, context_instance=RequestContext(request))

def mesoffres(request):
    currentuser =request
    mesoffres = Offre.objects.all()
    countoffre = mesoffres.count() 
    if request.method == 'POST':
        monoffre = Offre(
            entreprise = Entreprise.objects.get(pk=currentuser.user.entreprise.id),
            reference = request.POST['reference'],
            intitule = request.POST['intitule'],
            typeoffre = request.POST['typeoffre'],
            datedebut = request.POST['datedebut'],
            datefin = request.POST['datefin'],
            salairemin = request.POST['salairemin'],
            salairemax = request.POST['salairemax'],
            region = request.POST['region'],
            ville= request.POST['ville'],
            contactoffre = request.POST['contactoffre'],
            description = request.POST['description'],
            mission = request.POST['mission'],
            secteuractivite = request.POST['secteuractivite'],
        )
        monoffre.save()
    return render_to_response("../templates/mesoffres.html",{'currentuser':currentuser, 'mesoffres':mesoffres, 'countoffre': countoffre}, context_instance=RequestContext(request))
    
def deloffres(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	if request.method== 'POST':
           offre = Offre.objects.get(pk=request.POST['idoffretodel'])
           offre.delete()            
             #prevoir un message qui va notifié que l'on a supprimer le message
        return HttpResponseRedirect(reverse('experts.views.mesoffres'))
	
	return render_to_response("../templates/mesoffres.html",{'currentuser':currentuser}, context_instance=RequestContext(request))
	
def detailoffre(request, offre_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	offre = Offre.objects.get(pk=offre_id)	
	return render_to_response("../templates/detailoffre.html",{'currentuser':currentuser,'offre':offre}, context_instance=RequestContext(request))

def detailmonoffre(request, offre_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	offre = Offre.objects.get(pk=offre_id)	
	return render_to_response("../templates/detailmonoffre.html",{'currentuser':currentuser,'offre':offre}, context_instance=RequestContext(request))

def lesoffres(request):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	lesoffres = Offre.objects.all()
	return render_to_response("../templates/listeoffre.html",{'currentuser':currentuser, 'lesoffres':lesoffres}, context_instance=RequestContext(request))

def misajouroffre(request,offre_id):	
	# on est sur la page de profil
	# on recucupère les identifiants de l'utilisateurs courant
	currentuser =request
	offre = Offre.objects.get(pk=offre_id)   
	if request.method == 'POST':
	    offre.reference = request.POST['reference']
	    offre.intitule = request.POST['intitule']
	    offre.typeoffre = request.POST['typeoffre']
	    offre.datedebut = request.POST['datedebut']
	    offre.datefin = request.POST['datefin']
	    offre.salairemin = request.POST['salairemin']
	    offre.salairemax = request.POST['salairemax']
	    offre.region = request.POST['region']
	    offre.ville= request.POST['ville']
	    offre.contactoffre = request.POST['contactoffre']
	    offre.description = request.POST['description']
	    offre.mission = request.POST['mission']
	    offre.secteuractivite = request.POST['secteuractivite']
	    offre.save()
	    return HttpResponseRedirect(reverse('experts.views.mesoffres'))    
  
	return render_to_response("../templates/moduneoffre.html",{'currentuser':currentuser,'offre':offre}, context_instance=RequestContext(request))

def photoprofil(request, human_id):
	context_instance=RequestContext(request)
	currentuser=request
	human = Human.objects.get(pk=human_id)	
	if request.method == 'POST':
		human.photo=request.FILES['photo']
		human.save()
		return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))
	return HttpResponseRedirect(reverse('experts.views.profil', args=(currentuser.user.id,)))

def photoprofilentreprise(request):
	context_instance=RequestContext(request)
	currentuser=request
	entreprise = Entreprise.objects.get(pk=currentuser.user.entreprise.id)	
	if request.method == 'POST':
		entreprise.photo=request.FILES['photo']
		entreprise.save()
		return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
	return HttpResponseRedirect(reverse('experts.views.profilentreprise'))
