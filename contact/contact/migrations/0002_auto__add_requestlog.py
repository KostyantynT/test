# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestLog'
        db.create_table(u'contact_requestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'contact', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'RequestLog'
        db.delete_table(u'contact_requestlog')


    models = {
        u'contact.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contact.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']