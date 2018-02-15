# Generated by Django 2.0.1 on 2018-02-12 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_openehr', '0006_auto_20180212_1507'),
        ('django_openehr_demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferofcaresummary',
            name='admission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.InpatientAdmission'),
        ),
        migrations.AddField(
            model_name='transferofcaresummary',
            name='allergies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.AdverseReaction'),
        ),
        migrations.AddField(
            model_name='transferofcaresummary',
            name='demographic_professional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.DemographicProfessional'),
        ),
        migrations.AddField(
            model_name='transferofcaresummary',
            name='diagnoses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.ProblemDiagnosis'),
        ),
        migrations.AddField(
            model_name='transferofcaresummary',
            name='reason_for_encounter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.ReasonForEncounter'),
        ),
        migrations.AddField(
            model_name='transferofcaresummary',
            name='relevant_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_openehr.RelevantContact'),
        ),
    ]
