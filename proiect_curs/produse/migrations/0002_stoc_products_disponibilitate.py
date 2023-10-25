from django.db import migrations, models

class Migration(migrations.Migration):


    dependencies = [
       ('produse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produs',
            name='disponibilitate',
            field=models.IntegerField(default=0),
        ),
    ]


    operations = [

    ]