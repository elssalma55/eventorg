# Generated by Django 5.0.4 on 2024-05-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_prestataire_prestataire_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestataire',
            name='type',
            field=models.CharField(choices=[('Traiteur', 'Traiteur'), ('Photographe', 'Photographe'), ('DJ', 'DJ')], max_length=20, null=True),
        ),
    ]