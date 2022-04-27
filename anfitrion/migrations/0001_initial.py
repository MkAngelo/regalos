# Generated by Django 4.0.4 on 2022-04-27 16:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anfitrion',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.customuser', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(choices=[('BO', 'Boda'), ('XV', 'XV Años'), ('BA', 'Bautizos'), ('IN', 'Infantiles'), ('PH', 'Para él'), ('PM', 'Para ella')], max_length=2)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('guests', models.TextField(max_length=2000)),
                ('address', models.TextField(max_length=500)),
                ('anfitrion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anfitrion_user_set', to='anfitrion.anfitrion')),
                ('festejado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_user_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
