from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.TextField()),
                ('address', models.TextField(null=True)),
                ('phone', models.TextField(null=True)),
                ('map_url', models.TextField(null=True)),
                ('hours', models.TextField(null=True)),
                ('picture1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('picture2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('picture3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('like_users', models.ManyToManyField(related_name='like_restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('grade', models.IntegerField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('restaurant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bars.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bars.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
