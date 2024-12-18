# Generated by Django 5.1.1 on 2024-12-12 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidder', '0018_profile_is_forced_out'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VipItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guess_range_min', models.IntegerField()),
                ('guess_range_max', models.IntegerField()),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guessed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closeness', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guesser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guesses', to=settings.AUTH_USER_MODEL)),
                ('vip_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guesses', to='bidder.vipitem')),
            ],
        ),
    ]
