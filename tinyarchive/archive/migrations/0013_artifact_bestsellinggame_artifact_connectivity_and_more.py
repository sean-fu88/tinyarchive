# Generated by Django 4.0.5 on 2022-08-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0012_alter_artifact_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='bestSellingGame',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='connectivity',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='consoleType',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='cpu',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='developer',
            field=models.CharField(choices=[('nintendo', 'Nintendo'), ('microsoft', 'Microsoft'), ('meta', 'Meta'), ('sony computer entertainment', 'Sony Computer Entertainment')], default='nintendo', max_length=50),
        ),
        migrations.AddField(
            model_name='artifact',
            name='dimensions',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='discontinuedDate',
            field=models.CharField(default='N/a', max_length=20),
        ),
        migrations.AddField(
            model_name='artifact',
            name='generation',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='gpu',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='hardware',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='manufacturer',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='memory',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='operatingSystem',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='price',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='releaseDate',
            field=models.CharField(default='N/a', max_length=20),
        ),
        migrations.AddField(
            model_name='artifact',
            name='software',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='storage',
            field=models.CharField(default='N/a', max_length=200),
        ),
        migrations.AddField(
            model_name='artifact',
            name='unitsSold',
            field=models.CharField(default='N/a', max_length=200),
        ),
    ]
