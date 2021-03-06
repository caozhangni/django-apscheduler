# Generated by Django 2.2.14 on 2020-07-16 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django_apscheduler", "0002_auto_20180412_0758"),
    ]

    operations = [
        migrations.AlterField(
            model_name="djangojob",
            name="name",
            field=models.CharField(
                help_text="Unique name for this job.", max_length=255, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="djangojob",
            name="next_run_time",
            field=models.DateTimeField(
                blank=True,
                db_index=True,
                help_text="Date and time at which this job is scheduled to be executed next.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="duration",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                help_text="Total run time of this job (in seconds).",
                max_digits=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="exception",
            field=models.CharField(
                help_text="Details of exception that occurred during job execution (if any).",
                max_length=1000,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="finished",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                help_text="Timestamp at which this job was finished.",
                max_digits=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="job",
            field=models.ForeignKey(
                help_text="The job that this execution relates to.",
                on_delete=django.db.models.deletion.CASCADE,
                to="django_apscheduler.DjangoJob",
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="run_time",
            field=models.DateTimeField(
                db_index=True, help_text="Date and time at which this job was executed."
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="started",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                help_text="Timestamp at which this job was started.",
                max_digits=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="status",
            field=models.CharField(
                choices=[
                    ["Added", "Added"],
                    ["Started execution", "Started execution"],
                    ["Max instances reached!", "Max instances reached!"],
                    ["Missed!", "Missed!"],
                    ["Modified!", "Modified!"],
                    ["Removed!", "Removed!"],
                    ["Error!", "Error!"],
                    ["Executed", "Executed"],
                ],
                help_text="The current status of this job execution.",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="djangojobexecution",
            name="traceback",
            field=models.TextField(
                help_text="Traceback of exception that occurred during job execution (if any).",
                null=True,
            ),
        ),
    ]
