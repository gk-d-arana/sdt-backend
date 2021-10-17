from django.db import models


class MainSection(models.Model):
    main_section_name = models.CharField(max_length=255)
    main_section_description = models.TextField()

    def __str__(self):
        return self.main_section_name


class Section(models.Model):
    section_name = models.CharField(max_length=255)
    section_description = models.TextField()
    #main_section = models.ForeignKey(MainSection, on_delete=models.CASCADE, related_name='main_section')
    section_image = models.FileField(upload_to="static/images", blank=True)


    def __str__(self):
        return self.section_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_image = models.FileField(upload_to="static/images", blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section')

    def __str__(self):
        return self.product_name
