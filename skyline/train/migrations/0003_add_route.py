# Generated by Django 4.0.4 on 2022-04-30 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_remove_add_train_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='train.add_train')),
            ],
        ),
    ]
