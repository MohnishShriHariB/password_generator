# Generated by Django 4.2.3 on 2023-07-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_remove_summa_imag_alter_summa_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='summa',
            name='imag',
            field=models.ImageField(blank=True, upload_to='\\generator\\media'),
        ),
    ]
