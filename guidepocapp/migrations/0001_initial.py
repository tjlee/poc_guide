# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'guidepocapp_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('region_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'guidepocapp', ['Region'])

        # Adding model 'Place'
        db.create_table(u'guidepocapp_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('place_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guidepocapp.Region'])),
        ))
        db.send_create_signal(u'guidepocapp', ['Place'])

        # Adding model 'Guide'
        db.create_table(u'guidepocapp_guide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('activity', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(default='', max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=60)),
            ('phone1', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('phone2', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('skype', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('comments', self.gf('django.db.models.fields.CharField')(default='', max_length=2048)),
        ))
        db.send_create_signal(u'guidepocapp', ['Guide'])

        # Adding model 'GuideToPlace'
        db.create_table(u'guidepocapp_guidetoplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guidepocapp.Place'])),
            ('guide_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guidepocapp.Guide'])),
        ))
        db.send_create_signal(u'guidepocapp', ['GuideToPlace'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'guidepocapp_region')

        # Deleting model 'Place'
        db.delete_table(u'guidepocapp_place')

        # Deleting model 'Guide'
        db.delete_table(u'guidepocapp_guide')

        # Deleting model 'GuideToPlace'
        db.delete_table(u'guidepocapp_guidetoplace')


    models = {
        u'guidepocapp.guide': {
            'Meta': {'object_name': 'Guide'},
            'activity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'comments': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60'}),
            'phone1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60'})
        },
        u'guidepocapp.guidetoplace': {
            'Meta': {'object_name': 'GuideToPlace'},
            'guide_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guidepocapp.Guide']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guidepocapp.Place']"})
        },
        u'guidepocapp.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guidepocapp.Region']"}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'})
        },
        u'guidepocapp.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['guidepocapp']