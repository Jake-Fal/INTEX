# Generated by Django 4.1.2 on 2022-12-01 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_alter_fooditem_phosphate_mg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('HeightFt', models.SmallIntegerField()),
                ('HeightIn', models.SmallIntegerField()),
                ('Weight', models.SmallIntegerField()),
                ('Sex', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AlterField(
            model_name='actuals',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='foodentry',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Phosphate_mg',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Potassium_mg',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Protein_g',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Sodium_mg',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Water_L',
            field=models.SmallIntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='waterentry',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
