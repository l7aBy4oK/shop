from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "main_categories"


class ChildCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey("MainCategory", on_delete=models.CASCADE)

    class Meta:
        db_table = "child_categories"


