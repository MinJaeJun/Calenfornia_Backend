# Generated by Django 3.2 on 2022-09-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0003_auto_20220823_1036'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Commentid', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('commnetInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.info')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislike_comment', to='accounts.User')),
                ('likes', models.ManyToManyField(blank=True, related_name='like_comment', to='accounts.User')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]