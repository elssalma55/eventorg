# Generated by Django 5.0.4 on 2024-05-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_event_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='lieu',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='titre',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Wedding', 'Wedding'), ('Birthday', 'Birthday'), ('Corporate', 'Corporate Event'), ('Conference', 'Conference'), ('Exhibition', 'Exhibition'), ('Baptism', 'Baptism'), ('Gender Reveal', 'Gender Reveal')], max_length=100),
        ),
    ]
