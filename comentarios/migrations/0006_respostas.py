# Generated by Django 3.1.4 on 2021-01-18 19:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0005_auto_20210104_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField()),
                ('data_resposta', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicado_resposta', models.BooleanField(default=True)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comentarios.comentarios')),
            ],
            options={
                'verbose_name_plural': 'Respostas',
            },
        ),
    ]
