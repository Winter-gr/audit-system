# Generated by Django 4.0.4 on 2022-05-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('unit', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
    ]