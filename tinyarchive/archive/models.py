
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects = InheritanceManager()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    creator = models.CharField(max_length=50, blank="True")
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )


class AssociatedImage(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(
        ArchiveDocument, blank=False, null=False, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200, blank=True)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=False
    )

    def __str__(self):
        return(self.photo_image.url)


class Photograph(ArchiveDocument):
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )


class Artifact(ArchiveDocument):

    DEVELOPER_NINTENDO = 'nintendo'
    DEVELOPER_MICROSOFT = 'microsoft'
    DEVELOPER_META = 'meta'
    DEVELOPER_SONY = 'sony computer entertainment'
    
    DEVELOPER_CHOICES = [(DEVELOPER_NINTENDO, "Nintendo"),
                        (DEVELOPER_MICROSOFT, "Microsoft"),
                        (DEVELOPER_META, "Meta"),
                        (DEVELOPER_SONY, "Sony Computer Entertainment")]
    developer = models.CharField(
        max_length=50, choices=DEVELOPER_CHOICES, default=DEVELOPER_NINTENDO)
    model3d = models.URLField(max_length=500, blank="True")
    releaseDate = models.CharField(max_length=20, default= "N/a")
    manufacturer = models.CharField(max_length=200, default= "N/a") 
    discontinuedDate = models.CharField(max_length=20, default= "N/a")
    hardware = models.CharField(max_length=200, default= "N/a")
    software =models.CharField(max_length=200, default= "N/a")
    generation = models.CharField(max_length = 200, default= "N/a")
    consoleType = models.CharField(max_length = 200, default= "N/a")
    operatingSystem = models.CharField(max_length = 200, default= "N/a")
    dimensions =models.CharField(max_length = 200, default= "N/a")
    gpu = models.CharField(max_length = 200, default= "N/a")
    cpu = models.CharField(max_length = 200, default= "N/a")
    price = models.CharField(max_length = 200, default= "N/a")
    memory =models.CharField(max_length = 200, default= "N/a")
    storage = models.CharField(max_length = 200, default= "N/a")
    connectivity =models.CharField(max_length = 200, default= "N/a")
    bestSellingGame =models.CharField(max_length = 200, default= "N/a")
    unitsSold = models.CharField(max_length = 200, default= "N/a")


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)
