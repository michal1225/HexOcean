# Generated by Django 4.2.6 on 2023-10-11 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_imgenterprise_imgpremium_rename_img_imgbasic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImgEnterprise',
            new_name='Img',
        ),
        migrations.DeleteModel(
            name='ImgBasic',
        ),
        migrations.DeleteModel(
            name='ImgPremium',
        ),
    ]
