# Generated by Django 4.1.5 on 2023-02-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='productColourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productmainmodel')),
            ],
        ),
    ]
