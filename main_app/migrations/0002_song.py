# Generated by Django 3.2 on 2021-04-17 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=50)),
                ('rating', models.CharField(choices=[('G', 'Good'), ('O', 'Okay'), ('B', 'Bad')], default='G', max_length=1)),
                ('boyband', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.boyband')),
            ],
        ),
    ]
