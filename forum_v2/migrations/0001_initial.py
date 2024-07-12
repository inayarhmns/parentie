# Generated by Django 5.0.7 on 2024-07-12 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_registereduser_agama'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registereduser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user_commenting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registereduser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='forum_v2.discussion')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=300)),
                ('detail', models.TextField()),
                ('penyelenggara', models.CharField(max_length=300)),
                ('lokasi', models.TextField()),
                ('tanggal_mulai', models.DateField(null=True)),
                ('tanggal_selesai', models.DateField(blank=True, null=True)),
                ('waktu_mulai', models.TimeField(null=True)),
                ('waktu_selesai', models.TimeField(blank=True, null=True)),
                ('link_event', models.URLField(blank=True, null=True)),
                ('nama_contact_person', models.CharField(blank=True, max_length=50, null=True)),
                ('nomor_contact_person', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registereduser')),
            ],
        ),
        migrations.CreateModel(
            name='PesertaEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peserta', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_v2.event')),
            ],
        ),
    ]