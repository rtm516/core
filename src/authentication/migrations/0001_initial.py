# Generated by Django 3.0.5 on 2020-08-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InviteCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, unique=True)),
                ('uses', models.IntegerField(default=0)),
                ('max_uses', models.IntegerField()),
                ('fully_used', models.BooleanField(default=False)),
            ],
        ),
    ]
