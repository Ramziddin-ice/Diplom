# Generated by Django 4.2.1 on 2023-05-18 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_storge', '0002_mytext'),
        ('shingle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shingle_text_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.PositiveSmallIntegerField()),
                ('as_like', models.CharField(max_length=250)),
                ('text_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_text', to='file_storge.mytext')),
                ('text_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_text', to='file_storge.mytext')),
            ],
        ),
    ]
