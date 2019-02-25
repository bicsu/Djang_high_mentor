# Generated by Django 2.1.3 on 2018-11-28 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_id', models.TextField()),
                ('uni_intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='University_major_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_infor.University')),
            ],
        ),
        migrations.CreateModel(
            name='University_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_infor.University_major_data')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_infor.University')),
            ],
        ),
    ]
