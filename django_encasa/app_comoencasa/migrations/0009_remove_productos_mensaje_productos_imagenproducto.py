# Generated by Django 4.1 on 2023-11-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comoencasa', '0008_productos_mensaje_alter_itemcarrito_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='productos',
            name='imagenProducto',
            field=models.ImageField(null=True, upload_to='media\\static\\img\\Menu'),
        ),
    ]
