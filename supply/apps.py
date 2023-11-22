from django.apps import AppConfig


class SupplyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "supply"
    verbose_name = "Supply Details"

    def ready(self) -> None:
        import supply.signals  # noqa: F401
