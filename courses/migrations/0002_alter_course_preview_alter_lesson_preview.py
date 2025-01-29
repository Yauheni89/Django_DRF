
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="preview",
            field=models.ImageField(null=True, upload_to="course/photo"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="preview",
            field=models.ImageField(null=True, upload_to="course/photo"),
        ),
    ]
