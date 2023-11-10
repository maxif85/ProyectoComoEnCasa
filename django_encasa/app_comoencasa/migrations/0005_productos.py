# Generated by Django 4.1 on 2023-11-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comoencasa', '0004_perfilusuario_remove_elementopedido_pedido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=200)),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]