# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Log.delta_seconds'
        db.alter_column(u'Tag_log', 'delta_seconds', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Log.delta_seconds'
        db.alter_column(u'Tag_log', 'delta_seconds', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'Tag.image': {
            'Meta': {'object_name': 'Image'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'primary_key': 'True'})
        },
        u'Tag.log': {
            'Meta': {'object_name': 'Log'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'delta_seconds': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Tag.Image']"}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['Tag']