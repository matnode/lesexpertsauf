# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

class Typecompte (models.Model):
       user =  models.OneToOneField(User)
       typedecompte = models.CharField(max_length=200)
       
       def __unicode__(self):
          return self.typedecompte

class Human(models.Model):
    user = models.OneToOneField(User)
    nom = models.CharField(max_length=200) 
    prenom = models.CharField(max_length=200) 
    civilite = models.CharField(max_length=200) 
    online = models.IntegerField()	
    codepostale = models.TextField()
    telephone = models.IntegerField() 
    siteweb = models.TextField() 
    adresse = models.TextField() 
    photo = models.ImageField(upload_to="photos/")
    niveauetude = models.CharField(max_length=200)
    signature= models.TextField() 
    ville = models.CharField(max_length=255)
    datenaissance= models.TextField()
    datecreation= models.DateTimeField()
	
    def __unicode__(self):
          return self.nom
    def __unicode__(self):
          return self.prenom
    def __unicode__(self):
          return self.civilite
    def __unicode__(self):
          return self.online
    def __unicode__(self):
          return self.codepostale
    def __unicode__(self):
          return self.telephone
    def __unicode__(self):
          return self.siteweb
    def __unicode__(self):
          return self.adresse
    def __unicode__(self):
          return self.niveauetude 
    def __unicode__(self):
          return self.signature
    def __unicode__(self):
          return self.ville


class Competence(models.Model):
    human = models.ForeignKey(Human)
    nom = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
          return self.nom
    def __unicode__(self):
          return self.description     

class Mission(models.Model):
    human = models.ForeignKey(Human)
    competence = models.ManyToManyField(Competence)
    titre = models.TextField()
    description = models.TextField()
    competenceutilisee = models.TextField()
    fonction = models.TextField()
    entreprise = models.CharField(max_length=255)
    datedebut = models.CharField(max_length=255)
    datefin = models.CharField(max_length=255)
        
    def __unicode__(self):
          return self.titre
    def __unicode__(self):
          return self.description
    def __unicode__(self):
          return self.competenceutilisee     
    def __unicode__(self):
          return self.fonction
    def __unicode__(self):
          return self.entreprise 


class Formation(models.Model):
    human = models.ForeignKey(Human)
    intitule = models.TextField()
    description = models.TextField()
    diplome = models.TextField()
    lieu = models.CharField(max_length=255)
    ecole = models.CharField(max_length=255)
    datedebut = models.CharField(max_length=255)
    datefin = models.CharField(max_length=255)
    
    def __unicode__(self):
          return self.intitule
    def __unicode__(self):
          return self.description      
    def __unicode__(self):
          return self.diplome
    def __unicode__(self):
          return self.lieu 
    def __unicode__(self):
          return self.ecole

class Loisir(models.Model):
    human = models.ForeignKey(Human)
    titre = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
          return self.titre
    def __unicode__(self):
          return self.description  

class Langue(models.Model):
    human = models.ForeignKey(Human)
    nom = models.CharField(max_length=255)
    niveau = models.CharField(max_length=255)
    
    def __unicode__(self):
          return self.nom
    def __unicode__(self):
          return self.niveau

class Entreprise(models.Model):
    user = models.OneToOneField(User)
    nom = models.TextField()
    description = models.TextField()
    datedefondation = models.CharField(max_length=200)
    codepostale = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    taille = models.CharField(max_length=200)
    siteweb = models.TextField()
    telephone = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    activite = models.TextField()

class Offre(models.Model):
    entreprise = models.ForeignKey(Entreprise)
    reference = models.CharField(max_length=200)
    intitule = models.TextField()
    ville = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    secteuractivite = models.TextField()
    mission = models.TextField()
    typedecontra = models.CharField(max_length=200)
    periodaffichage = models.CharField(max_length=255)
    grillesalaire = models.TextField(max_length=255)
    datelimite = models.CharField(max_length=255)
    description= models.TextField()
    dureecontrat = models.CharField(max_length=200)
    dateprisefonction = models.CharField(max_length=200)
