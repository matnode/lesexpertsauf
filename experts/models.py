# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

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
    datedebut = models.DateTimeField()
    datefin = models.DateTimeField()
        
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
    datedebut = models.DateTimeField()
    datefin = models.DateTimeField()
    
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
             
