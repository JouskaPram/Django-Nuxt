# Generated by Django 4.1.5 on 2023-03-16 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='id_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restapi.category'),
            preserve_default=False,
        ),
    ]
