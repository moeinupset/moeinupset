# Generated by Django 2.2 on 2020-03-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now=True, verbose_name='created_time')),
                ('modified_time', models.DateField(auto_now_add=True, verbose_name='modified_time')),
                ('name', models.CharField(max_length=12, verbose_name='name')),
                ('category', models.ManyToManyField(related_name='sub_category', to='category.Category')),
            ],
            options={
                'verbose_name': 'sub_category',
                'verbose_name_plural': 'sub_categorys',
            },
        ),
    ]
