
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                """
                ALTER TABLE portal_student
                ADD COLUMN is_active bool NOT NULL DEFAULT 1
                """,
                """
                ALTER TABLE portal_student
                ADD COLUMN updated_at datetime NULL
                """,
                """
                UPDATE portal_student
                SET updated_at = created_at
                WHERE updated_at IS NULL
                """,
            ],
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
