# Generated by Django 4.1.7 on 2023-04-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_alter_movie_director_alter_movie_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='img',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=1, upload_to='gallery', verbose_name='Images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Moive name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveBigIntegerField(verbose_name='release year'),
        ),
    ]
