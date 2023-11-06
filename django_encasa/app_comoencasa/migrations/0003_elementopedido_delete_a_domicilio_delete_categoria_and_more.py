# Generated by Django 4.1 on 2023-11-05 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_comoencasa', '0002_a_domicilio_categoria_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='A_domicilio',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='pedidos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_comoencasa.clientes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='monto_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(through='app_comoencasa.ElementoPedido', to='app_comoencasa.productos'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='elementopedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_comoencasa.pedido'),
        ),
        migrations.AddField(
            model_name='elementopedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_comoencasa.productos'),
        ),
    ]
