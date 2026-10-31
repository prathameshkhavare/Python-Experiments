
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0002_repair_student_columns"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                """
                ALTER TABLE portal_attendance
                ADD COLUMN note varchar(250) NOT NULL DEFAULT '';
                """,
                """
                ALTER TABLE portal_attendance
                ADD COLUMN created_at datetime NULL;
                """,
                """
                ALTER TABLE portal_attendance
                ADD COLUMN recorded_by_id bigint NULL
                REFERENCES auth_user(id);
                """,
            ],
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
