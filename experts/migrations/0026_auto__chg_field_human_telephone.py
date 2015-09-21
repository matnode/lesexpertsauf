# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Human.telephone'
        db.alter_column('experts_human', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Human.telephone'
        db.alter_column('experts_human', 'telephone', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'experts.competence': {
            'Meta': {'object_name': 'Competence'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {})
        },
        'experts.entreprise': {
            'Meta': {'object_name': 'Entreprise'},
            'activite': ('django.db.models.fields.TextField', [], {}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'codepostale': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'datedefondation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'siteweb': ('django.db.models.fields.TextField', [], {}),
            'taille': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'experts.formation': {
            'Meta': {'object_name': 'Formation'},
            'datedebut': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'datefin': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diplome': ('django.db.models.fields.TextField', [], {}),
            'ecole': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intitule': ('django.db.models.fields.TextField', [], {}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'experts.human': {
            'Meta': {'object_name': 'Human'},
            'adresse': ('django.db.models.fields.TextField', [], {}),
            'civilite': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'codepostale': ('django.db.models.fields.TextField', [], {}),
            'datecreation': ('django.db.models.fields.DateTimeField', [], {}),
            'datenaissance': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'niveauetude': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'online': ('django.db.models.fields.IntegerField', [], {}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'signature': ('django.db.models.fields.TextField', [], {}),
            'siteweb': ('django.db.models.fields.TextField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'experts.langue': {
            'Meta': {'object_name': 'Langue'},
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'niveau': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'experts.loisir': {
            'Meta': {'object_name': 'Loisir'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titre': ('django.db.models.fields.TextField', [], {})
        },
        'experts.mission': {
            'Meta': {'object_name': 'Mission'},
            'competence': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['experts.Competence']", 'symmetrical': 'False'}),
            'competenceutilisee': ('django.db.models.fields.TextField', [], {}),
            'datedebut': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'datefin': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entreprise': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fonction': ('django.db.models.fields.TextField', [], {}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titre': ('django.db.models.fields.TextField', [], {})
        },
        'experts.offre': {
            'Meta': {'object_name': 'Offre'},
            'contactoffre': ('django.db.models.fields.TextField', [], {}),
            'datedebut': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'datefin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entreprise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Entreprise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intitule': ('django.db.models.fields.TextField', [], {}),
            'mission': ('django.db.models.fields.TextField', [], {}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salairemax': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salairemin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'secteuractivite': ('django.db.models.fields.TextField', [], {}),
            'typeoffre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'experts.typecompte': {
            'Meta': {'object_name': 'Typecompte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typedecompte': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['experts']