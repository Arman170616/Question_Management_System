# Generated by Django 5.0.6 on 2024-05-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question_Title', models.TextField()),
                ('Option_1', models.TextField()),
                ('Option_2', models.TextField()),
                ('Option_3', models.TextField()),
                ('Option_4', models.TextField()),
                ('Answer', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='allquestions',
            constraint=models.CheckConstraint(check=models.Q(('Answer', models.F('Option_1')), ('Answer', models.F('Option_2')), ('Answer', models.F('Option_3')), ('Answer', models.F('Option_4')), _connector='OR'), name='answer_matches_option'),
        ),
    ]