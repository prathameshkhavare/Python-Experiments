
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0003_repair_attendance_columns"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                """
                ALTER TABLE portal_mark
                ADD COLUMN recorded_by_id bigint NULL
                REFERENCES auth_user(id);
                """,
                """
                ALTER TABLE portal_mark
                ADD COLUMN created_at datetime NULL;
                """,
            ],
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
