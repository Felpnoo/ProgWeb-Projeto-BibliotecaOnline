# Generated by Django 5.1.3 on 2024-11-18 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0002_emprestimo_devolvido_livro_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='capa',
        ),
        migrations.CreateModel(
            name='LivroCapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(blank=True, default='capas/default.jpg', null=True, upload_to='capas')),
                ('livro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='capa', to='Biblioteca.livro')),
            ],
        ),
    ]