# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0025_auto_20190612_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='source',
        ),
        migrations.RemoveField(
            model_name='score',
            name='source',
        ),
        migrations.RemoveField(
            model_name='share',
            name='source',
        ),
        migrations.RemoveField(
            model_name='wmticket',
            name='score',
        ),
        migrations.RemoveField(
            model_name='wmticket',
            name='share',
        ),
        migrations.AddField(
            model_name='score',
            name='wm_ticket',
            field=models.ForeignKey(to='lite.WmTicket', null=True, blank=True, verbose_name='外卖码'),
        ),
        migrations.AddField(
            model_name='share',
            name='wm_ticket',
            field=models.ForeignKey(to='lite.WmTicket', null=True, blank=True, verbose_name='外卖码'),
        ),
    ]
