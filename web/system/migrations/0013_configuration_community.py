# Generated by Django 2.1.2 on 2019-03-28 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.Community'),
        ),
    ]