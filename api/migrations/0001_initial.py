# Generated by Django 2.2.6 on 2019-11-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('disc', models.CharField(max_length=500)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
