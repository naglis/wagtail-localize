# Generated by Django 2.2.9 on 2020-01-28 17:25

# This migration was written before Wagtail localize was released so it assumes
# the multi-region feature hasn't been used by anyone

from django.db import migrations


def migrate_to_locale(apps, schema_editor):
    Locale = apps.get_model("wagtail_localize.Locale")
    Segment = apps.get_model("wagtail_localize_translation.Segment")
    SegmentTranslation = apps.get_model(
        "wagtail_localize_translation.SegmentTranslation"
    )

    language_to_locale_mapping = {}

    def get_locale(language_id):
        if language_id not in language_to_locale_mapping:
            language_to_locale_mapping[language_id] = Locale.objects.get(
                region__is_default=True, language_id=language_id
            )

        return language_to_locale_mapping[language_id]

    for segment in Segment.objects.iterator():
        segment.locale = get_locale(segment.language_id)
        segment.save(update_fields=["locale"])

    for translation in SegmentTranslation.objects.iterator():
        translation.locale = get_locale(translation.language_id)
        translation.save(update_fields=["locale"])


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize_translation", "0002_change_language_to_locale_1"),
    ]

    operations = [
        migrations.RunPython(migrate_to_locale),
    ]