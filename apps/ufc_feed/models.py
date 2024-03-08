from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
import uuid
from django.utils.text import slugify
from datetime import datetime
from django.core.validators import FileExtensionValidator
from django_cleanup import cleanup
# Create your models here.


def cover_loc(instance, filename):
    ext = filename.split(".")[-1]
    name = datetime.now()
    uuid_name = uuid.uuid4()
    filename = f'{uuid_name}.{ext}'
    return 'covers/{0}/{1}'.format(instance, filename)


def demo_loc(instance, filename):
    ext = filename.split(".")[-1]
    uuid_name = uuid.uuid4()
    filename = f'{uuid_name}.{ext}'
    return 'demos/{0}/{1}'.format(instance, filename)


#@cleanup.select
class Post(models.Model):
    id =                        models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    cover =                     ResizedImageField(scale=1, quality=100, force_format="PNG", upload_to=cover_loc)
    title =                     models.CharField(max_length=155)
    description =               RichTextField()
    demo =                      models.FileField(upload_to=demo_loc, validators=[FileExtensionValidator(allowed_extensions=["mp4"])])

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        _ = slugify(self.title)
        return _

