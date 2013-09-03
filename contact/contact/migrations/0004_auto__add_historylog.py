# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoryLog'
        db.create_table(u'contact_historylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('objectModel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'contact', ['HistoryLog'])


    def backwards(self, orm):
        # Deleting model 'HistoryLog'
        db.delete_table(u'contact_historylog')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contact.historylog': {
            'Meta': {'ordering': "['-time']", 'object_name': 'HistoryLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objectModel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'contact.requestlog': {
            'Meta': {'ordering': "['time']", 'object_name': 'RequestLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']