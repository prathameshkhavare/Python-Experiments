from django.contrib.auth.decorators import user_passes_test


def role_names(user):
    if not user.is_authenticated:
        return set()

    if user.is_superuser or user.is_staff:
        return {"Admin"}

    return set(user.groups.values_list("name", flat=True))


def can_manage_students(user):
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(
                name__in=["Admin", "Teacher"]
            ).exists()
        )
    )


def can_edit_academics(user):
    return can_manage_students(user)


def admin_required(view_func):
    return user_passes_test(
        lambda user: (
            user.is_authenticated
            and (
                user.is_superuser
                or user.groups.filter(name="Admin").exists()
            )
        )
    )(view_func)