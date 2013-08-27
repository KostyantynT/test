# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactInfo'
        db.create_table(u'contact_contactinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('bio', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=254)),
            ('jabber', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('skype', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('other', self.gf('django.db.models.fields.CharField')(default='', max_length=256)),
        ))
        db.send_create_signal(u'contact', ['ContactInfo'])


    def backwards(self, orm):
        # Deleting model 'ContactInfo'
        db.delete_table(u'contact_contactinfo')


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
        }
    }

    complete_apps = ['contact']