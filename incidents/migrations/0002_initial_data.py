from django.db import migrations
import datetime

def create_initial_incidents(apps, schema_editor):
    Incident = apps.get_model('incidents', 'Incident')
    Incident.objects.create(
        title="Bias in AI hiring system",
        description="The AI system exhibited bias against candidates from minority backgrounds.",
        severity="High",
        reported_at=datetime.datetime.now()
    )
    Incident.objects.create(
        title="Self-driving car confusion",
        description="Autonomous vehicle incorrectly identified a stop sign, causing safety concerns.",
        severity="Medium",
        reported_at=datetime.datetime.now()
    )
    Incident.objects.create(
        title="Chatbot offensive language",
        description="Chatbot started generating offensive and inappropriate content.",
        severity="High",
        reported_at=datetime.datetime.now()
    )

def delete_initial_incidents(apps, schema_editor):
    Incident = apps.get_model('incidents', 'Incident')
    Incident.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),   # depends on your first migration
    ]

    operations = [
        migrations.RunPython(create_initial_incidents, delete_initial_incidents),
    ]
