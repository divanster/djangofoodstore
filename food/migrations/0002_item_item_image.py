# Generated by Django 5.0.4 on 2024-04-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://media.istockphoto.com/id/1426890025/es/foto/la-pizza-de-la-que-te-olvidaste-durante-una-semana-y-se-puso-mohosa.jpg?s=612x612&w=0&k=20&c=r0cHrYxEjoLUoSz9VQCglgXc6Win_fFu-fjDwWfoPu4=', max_length=500),
        ),
    ]
