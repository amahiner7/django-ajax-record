# Generated by Django 3.2.5 on 2021-07-16 20:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('voice_record', models.FileField(upload_to='records')),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
            },
        ),
    ]
