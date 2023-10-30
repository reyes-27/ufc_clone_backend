from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from .models import (
    FighterProfile,
    WeightDivision,
    FighterTag,
    FighterStatus,
)
from .views import ParticipationListView
from django.urls import reverse
import datetime
from django.conf import settings
from django.core.files.base import ContentFile
from PIL import Image
import io

# Create your tests here.


class UfcBaseViewsTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        weight_division = WeightDivision.objects.create(name="LightHeavyWeight", min_weight=185, max_weight=205)
        fighter_tag = FighterTag.objects.create(
            name="title contender",
            description="A fighter that is got a high chance to fight for the title",
        )
        status = FighterStatus.objects.create(status="Active")
        byteImgIO1 = io.BytesIO()
        f_photo_png = Image.open(f"{settings.MEDIA_ROOT}/fighters/f_photo/Alex Pereira/PEREIRA_ALEX_R_07-29.png")
        f_photo_png.save(byteImgIO1, "PNG")
        f_photo = ContentFile(byteImgIO1.getvalue(), 'PEREIRA_ALEX_R_07-29.png')

        byteImgIO2 = io.BytesIO()
        c_photo_png = Image.open(f"{settings.MEDIA_ROOT}/fighters/c_photo/Alex Pereira/PEREIRA_ALEX_07-29.png")
        c_photo_png.save(byteImgIO2, "PNG")
        c_photo = ContentFile(byteImgIO2.getvalue(), 'PEREIRA_ALEX_07-29.png')

        cls.fighter = FighterProfile.objects.create(
            full_name="Alex Pereira",
            nickname="Poatan",
            birthdate=datetime.datetime(year=1987, month=7, day=7),
            native_city="São Paulo, Brazil",
            f_photo=f_photo,
            c_photo=c_photo,
            weight_division=weight_division,
            status=status,
            fighter_tag=fighter_tag,
            age=36,
            reach=79,
            height=75,
            leg_reach=56,
            weight=230,

            victories=7,
            losses=2,
            draws=0,
            no_contest=0,
        )

    def setUp(self):
        self.client = APIClient()
        self.response_part = self.client.get(path=reverse(viewname="participations-list", kwargs={"slug"}))
        self.response_fighter = self.client.get(path=reverse(
            viewname="fighter-detail", kwargs={"slug": self.fighter.fighter_slug}
        )
        )

    def test_fighter_view(self):
        response_data = self.response_fighter.json()
        self.assertEqual(self.response_fighter.status_code, 200)
        self.assertEquals(response_data["fighter"]["full_name"], "Alex Pereira")

    def test_participations(self):
        pass
    


