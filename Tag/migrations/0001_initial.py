# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'Tag_image', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'Tag', ['Image'])

        # Adding model 'Log'
        db.create_table(u'Tag_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tag.Image'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('delta_seconds', self.gf('django.db.models.fields.IntegerField')()),
            ('result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'Tag', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'Tag_image')

        # Deleting model 'Log'
        db.delete_table(u'Tag_log')


    models = {
        u'Tag.image': {
            'Meta': {'object_name': 'Image'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'primary_key': 'True'})
        },
        u'Tag.log': {
            'Meta': {'object_name': 'Log'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'delta_seconds': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Tag.Image']"}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['Tag']