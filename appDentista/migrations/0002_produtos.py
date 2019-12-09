# Generated by Django 3.0 on 2019-12-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDentista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lab', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]