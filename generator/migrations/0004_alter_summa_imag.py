# Generated by Django 4.2.3 on 2023-07-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_summa_imag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summa',
            name='imag',
            field=models.ImageField(upload_to='generator/images/'),
        ),
    ]
