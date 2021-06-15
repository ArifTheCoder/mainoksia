# Generated by Django 3.2.3 on 2021-06-15 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210605_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logos', verbose_name='Company logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Company name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='webshop_link',
            field=models.URLField(blank=True, default='', verbose_name="Company's webshop link"),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images_of_mainoksia', verbose_name='Upload image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Use as default image?'),
        ),
        migrations.AlterField(
            model_name='image',
            name='parent_link',
            field=models.URLField(blank=True, default='', verbose_name="Image's original link"),
        ),
        migrations.AlterField(
            model_name='image',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_of_week', to='api.week', verbose_name='Select week number'),
        ),
        migrations.AlterField(
            model_name='week',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_add_week', to='api.company', verbose_name='Select company'),
        ),
        migrations.AlterField(
            model_name='week',
            name='week_number',
            field=models.PositiveIntegerField(verbose_name='Week number'),
        ),
    ]