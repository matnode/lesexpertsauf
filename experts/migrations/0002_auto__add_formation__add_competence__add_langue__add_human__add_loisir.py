# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Formation'
        db.create_table('experts_formation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experts.Human'])),
            ('intitule', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('diplome', self.gf('django.db.models.fields.TextField')()),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ecole', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datedebut', self.gf('django.db.models.fields.DateTimeField')()),
            ('datefin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('experts', ['Formation'])

        # Adding model 'Competence'
        db.create_table('experts_competence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experts.Human'])),
            ('nom', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('experts', ['Competence'])

        # Adding model 'Langue'
        db.create_table('experts_langue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experts.Human'])),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('niveau', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('experts', ['Langue'])

        # Adding model 'Human'
        db.create_table('experts_human', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('civilite', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('online', self.gf('django.db.models.fields.IntegerField')()),
            ('codepostale', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telephone', self.gf('django.db.models.fields.IntegerField')()),
            ('siteweb', self.gf('django.db.models.fields.TextField')()),
            ('adresse', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('niveauetude', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('signature', self.gf('django.db.models.fields.TextField')()),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datenaissance', self.gf('django.db.models.fields.DateTimeField')()),
            ('datecreation', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('experts', ['Human'])

        # Adding model 'Loisir'
        db.create_table('experts_loisir', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experts.Human'])),
            ('titre', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('experts', ['Loisir'])

        # Adding model 'Mission'
        db.create_table('experts_mission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['experts.Human'])),
            ('titre', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('competenceutilisee', self.gf('django.db.models.fields.TextField')()),
            ('fonction', self.gf('django.db.models.fields.TextField')()),
            ('entreprise', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datedebut', self.gf('django.db.models.fields.DateTimeField')()),
            ('datefin', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('experts', ['Mission'])

        # Adding M2M table for field competence on 'Mission'
        m2m_table_name = db.shorten_name('experts_mission_competence')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mission', models.ForeignKey(orm['experts.mission'], null=False)),
            ('competence', models.ForeignKey(orm['experts.competence'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mission_id', 'competence_id'])


    def backwards(self, orm):
        # Deleting model 'Formation'
        db.delete_table('experts_formation')

        # Deleting model 'Competence'
        db.delete_table('experts_competence')

        # Deleting model 'Langue'
        db.delete_table('experts_langue')

        # Deleting model 'Human'
        db.delete_table('experts_human')

        # Deleting model 'Loisir'
        db.delete_table('experts_loisir')

        # Deleting model 'Mission'
        db.delete_table('experts_mission')

        # Removing M2M table for field competence on 'Mission'
        db.delete_table(db.shorten_name('experts_mission_competence'))


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
        'experts.formation': {
            'Meta': {'object_name': 'Formation'},
            'datedebut': ('django.db.models.fields.DateTimeField', [], {}),
            'datefin': ('django.db.models.fields.DateTimeField', [], {}),
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
            'codepostale': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'datecreation': ('django.db.models.fields.DateTimeField', [], {}),
            'datenaissance': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'niveauetude': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'online': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'signature': ('django.db.models.fields.TextField', [], {}),
            'siteweb': ('django.db.models.fields.TextField', [], {}),
            'telephone': ('django.db.models.fields.IntegerField', [], {}),
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
            'datedebut': ('django.db.models.fields.DateTimeField', [], {}),
            'datefin': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'entreprise': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fonction': ('django.db.models.fields.TextField', [], {}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['experts.Human']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titre': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['experts']