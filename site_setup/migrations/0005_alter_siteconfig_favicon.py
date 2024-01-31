# Generated by Django 5.0.1 on 2024-01-31 17:59

import utils.model_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_siteconfig_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfig',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validator.validate_png]),
        ),
    ]
