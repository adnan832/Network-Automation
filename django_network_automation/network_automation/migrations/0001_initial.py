# Generated by Django 4.0.3 on 2022-03-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('ssh_port', models.IntegerField(default=22)),
                ('vendor', models.CharField(choices=[('mikrotik', 'Mikrotik'), ('cisco', 'Cisco')], max_length=255)),
            ],
        ),
    ]