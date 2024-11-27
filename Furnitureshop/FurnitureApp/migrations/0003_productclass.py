# Generated by Django 5.1 on 2024-10-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FurnitureApp', '0002_categoryclass_cdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('productname', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('countryoforigin', models.CharField(blank=True, max_length=100, null=True)),
                ('manufacturedby', models.CharField(blank=True, max_length=100, null=True)),
                ('productimage1', models.ImageField(blank=True, null=True, upload_to='productpictures')),
                ('productimage2', models.ImageField(blank=True, null=True, upload_to='productpictures')),
                ('productimage3', models.ImageField(blank=True, null=True, upload_to='productpictures')),
            ],
        ),
    ]
