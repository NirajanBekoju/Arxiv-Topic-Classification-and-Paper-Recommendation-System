# Generated by Django 4.2.3 on 2023-07-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arxiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.CharField(max_length=20)),
                ('submitter', models.CharField(max_length=50)),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('comments', models.TextField()),
                ('doi', models.TextField()),
                ('abstract', models.TextField()),
                ('date', models.DateField()),
                ('categories', models.TextField()),
            ],
        ),
    ]