# Generated by Django 4.0 on 2023-06-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_note', models.TextField(max_length=500)),
                ('support', models.CharField(choices=[('Busy', 'Busy'), ('Need_Help', 'Help'), ('NPC _Call', 'NPC _Call'), ('Support_Call', 'Support_Call'), ('Payment_Call', 'Payment_Call')], default='Busy', max_length=500)),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
