# Generated by Django 4.0.4 on 2022-05-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0008_remove_register_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='As',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.IntegerField(null=True)),
                ('train_name', models.CharField(max_length=30, null=True)),
                ('date3', models.DateField(null=True)),
            ],
        ),
    ]