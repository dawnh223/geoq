# Generated by Django 3.0.5 on 2020-07-22 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '__first__'),
        ('core', '0002_auto_20200623_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='vocabulary',
            field=models.ForeignKey(blank=True, help_text='Favorite words', null=True, on_delete=django.db.models.deletion.PROTECT, to='ontology.Vocabulary'),
        ),
    ]
