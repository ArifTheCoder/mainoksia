from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Company name")
    logo = models.ImageField(
        upload_to="company_logos", null=True, blank=True, verbose_name="Company logo"
    )
    webshop_link = models.URLField(blank=True, default="", verbose_name="Company's webshop link"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Week(models.Model):
    company = models.ForeignKey(
        Company,
        related_name="company_add_week",
        on_delete=models.CASCADE,
        verbose_name="Select company"
    )
    week_number = models.PositiveIntegerField(null=False, blank=False, verbose_name="Week number")

    def __str__(self):
        return "{company_name}, week number: {company_add_week}".format(
            company_name=self.company.name,
            company_add_week=self.week_number,
        )


    
class Image(models.Model):
    week= models.ForeignKey(
        Week,
        related_name="image_of_week",
        on_delete=models.CASCADE,
        verbose_name="Select week number"
    )
    image = models.ImageField(
        upload_to="images_of_mainoksia", null=True, blank=True,
        verbose_name="Upload image"
    )
    parent_link = models.URLField(blank=True, default="",
    verbose_name="Image's original link"
    )
    is_default = models.BooleanField(default=False, verbose_name="Use as default image?")

    

