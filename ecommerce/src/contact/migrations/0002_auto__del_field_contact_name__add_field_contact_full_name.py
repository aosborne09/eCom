# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.name'
        db.delete_column(u'contact_contact', 'name')

        # Adding field 'Contact.full_name'
        db.add_column(u'contact_contact', 'full_name',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Contact.name'
        db.add_column(u'contact_contact', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Contact.full_name'
        db.delete_column(u'contact_contact', 'full_name')


    models = {
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']