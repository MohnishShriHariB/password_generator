# Generated by Django 4.2.3 on 2023-07-06 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_rename_txt_summa_title_remove_summa_imag_summa_dis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summa',
            name='dis',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='summa',
            name='ima',
            field=models.ImageField(upload_to='generator/images/'),
        ),
    ]
