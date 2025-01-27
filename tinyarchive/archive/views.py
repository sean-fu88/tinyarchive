from re import template
from django.shortcuts import render
from django.http import HttpResponse
from archive.models import ArchiveDocument, Photograph, AssociatedImage, Artifact
from model_utils.managers import InheritanceManager
from archive.consts import Choices


def index(request):
    context = {}
    items_to_list = []
    """ Tries to get any items. If there aren't any, list won't 
        be filled and the template will receive a blank list.
    """
    try:
        archive_items = ArchiveDocument.objects.all()
        for item in archive_items:
            #get all available photos.
            photos = AssociatedImage.objects.filter(associated_doc = item.id)
            thumb = None
            if photos:
                thumb = photos[0].photo_image.thumbnail
            archive_item_info = {
                "id": item.id,
                "thumbnail": thumb,
                "name": item.name,
                "description": item.description,
            }

            items_to_list.append(archive_item_info)
    except ArchiveDocument.DoesNotExist as e:
        #This exception gets suppressed and we pass an empty context to the template.
        #the template will know what to do with it. All other exceptions get raised.
        print(e)
   
    context["archive_items"] = items_to_list
    print(context)
    return render(request, "archive/index.html", context)

def photo_detail(request,item_id):
    print(request)
    img = AssociatedImage.objects.get(id=item_id)
    context = {}
    context["item"]={
        "name":img.name,
        "creator:":img.creator,
        "description":img.description,
        "picture":img.photo_image,
        "related_id":img.associated_doc.id,
        "related_name":img.associated_doc.name
    }
    return render(request,"archive/photo.html",context)

def item_detail(request, item_id):
    context = {}
    template_to_render = ""
    try:
        archive_item = ArchiveDocument.objects.get_subclass(id=item_id)
        pictures = []
        pics = AssociatedImage.objects.filter(associated_doc = item_id)
        for pic in pics:
            pictures.append({"picture":pic.photo_image.thumbnail,"id":pic.id})
        context["item"] = {
            "name": archive_item.name,
            "pictures": pictures,
            "description": archive_item.description,
        }
        if isinstance(archive_item, Photograph):
            # Photo type is the user-readable version of the Photo Type, as described in Consts.
            context["item"]["photo_type"] = Choices.PHOTO_TYPE_CHOICES[
                archive_item.photo_type
            ]
            template_to_render = "archive/item_photograph.html"
        elif isinstance(archive_item, Artifact):
            context["item"]["3dmodel"] = archive_item.model3d
            context["item"]["developer"] = archive_item.developer
            context["item"]["releaseDate"] = archive_item.releaseDate
            context["item"]["manufacturer"] = archive_item.manufacturer
            context["item"]["discontinuedDate"] = archive_item.discontinuedDate
            context["item"]["hardware"] = archive_item.hardware
            context["item"]["software"] = archive_item.software
            context["item"]["generation"] = archive_item.generation
            context["item"]["consoleType"] = archive_item.consoleType
            context["item"]["operatingSystem"] = archive_item.operatingSystem
            context["item"]["dimensions"] = archive_item.dimensions
            context["item"]["gpu"] = archive_item.gpu
            context["item"]["cpu"] = archive_item.cpu
            context["item"]["price"] = archive_item.price
            context["item"]["memory"] = archive_item.memory
            context["item"]["storage"] = archive_item.storage
            context["item"]["connectivity"] = archive_item.connectivity
            context["item"]["bestSellingGame"] = archive_item.bestSellingGame
            context["item"]["unitsSold"] = archive_item.unitsSold
            template_to_render = "archive/item_artifact.html"
        else:
            context["item"]["transcription"] = archive_item.transcription
            context["item"]["language"] = archive_item.language
            template_to_render = "archive/item_document.html"

    except Exception as e:
        print(e)
        raise e
    print(context)
    return render(request, template_to_render, context)
