# Generated by Django 4.2.3 on 2023-07-08 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_rename_scopes_article_tags_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main'], 'verbose_name': 'Раздел статей', 'verbose_name_plural': 'Разделы статьи'},
        ),
    ]
