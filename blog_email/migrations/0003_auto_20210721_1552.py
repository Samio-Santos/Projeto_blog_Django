# Generated by Django 3.1.4 on 2021-07-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_email', '0002_alter_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]