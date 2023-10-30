from django.db import models
import uuid
from django.utils.text import slugify
from django_resized import ResizedImageField

# Create your models here.


class FighterTag(models.Model):
    name =              models.CharField(max_length=20)
    description =       models.TextField()

    def __str__(self):
        return self.name


class FighterStatus(models.Model):
    status=             models.CharField(max_length=30)
    
    def __str__(self):
        return self.status


class WeightDivision(models.Model):
    name =          models.CharField(max_length=30)
    min_weight =    models.FloatField()
    max_weight =    models.FloatField()

    def __str__(self):
        return self.name


def c_photo(instance, filename):
    return "fighters/c_photo/{0}/{1}".format(instance, filename)


def f_photo(instance, filename):
    return "fighters/f_photo/{0}/{1}".format(instance, filename)


def p_photo(instance, filename):
    return "fighters/p_photo/{0}/{1}".format(instance, filename)


class FighterProfile(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fighter_slug =      models.SlugField(max_length=200, blank=True, null=False)
    full_name =         models.CharField(max_length=155)
    nickname =          models.CharField(max_length=30)
    birthdate =         models.DateField()
    native_city =       models.CharField(max_length=155)
    f_photo =           ResizedImageField(size=[190, 588], upload_to=f_photo, force_format='PNG')
    c_photo =           models.ImageField(upload_to=c_photo)
    # p_photo =           ResizedImageField(size=[329, 500], force_format='PNG', null=True, blank=False)
    weight_division =   models.ForeignKey(WeightDivision, on_delete=models.CASCADE)
    status =            models.ForeignKey(FighterStatus, on_delete=models.SET_NULL, null=True)
    fighter_tag =       models.ForeignKey(FighterTag, on_delete=models.PROTECT, blank=True, null=True)
    # physical attributes
    age =               models.PositiveIntegerField()
    reach =             models.FloatField()
    height =            models.FloatField()
    leg_reach =         models.FloatField()
    weight =            models.FloatField()
    # fighter stats
    number_of_fights =              models.PositiveIntegerField(blank=True, null=True)
    victories =                     models.PositiveIntegerField()
    losses =                        models.PositiveIntegerField()
    draws =                         models.PositiveIntegerField()
    no_contest =                    models.PositiveIntegerField()
    
    @property
    def get_c_photo_url(self) -> str:
        if self.c_photo and hasattr(self.c_photo, "url"):
            return f'http://localhost:8000/media/fighters/{self.c_photo}/'

    @property
    def get_f_photo_url(self) -> str:
        if self.f_photo and hasattr(self.f_photo, "url"):
            return f'http://localhost:8000/media/fighters/{self.f_photo}/'
        
    def save(self, *args, **kwargs):
        if not self.fighter_slug:
            self.fighter_slug = slugify(self.full_name)
        if not self.number_of_fights:
            self.number_of_fights = self.victories + self.losses + self.draws + self.no_contest
        super(FighterProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class Participation(models.Model):
    corner_choices = (
        ("RC", "Red corner"),
        ("BC", "Blue corner"),
    )

    fight =                 models.ForeignKey("Fight", on_delete=models.SET_NULL, null=True, related_name="fight_to_fighter")
    fighter =               models.ForeignKey(FighterProfile, on_delete=models.SET_NULL, null=True, related_name="fighter_to_fight")
    corner =                models.CharField(max_length=155, choices=corner_choices, blank=True, null=False)
    loss =                  models.BooleanField(default=False)
    victory =               models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fight} --X {self.fighter}'


class Fight(models.Model):
    name = models.CharField(max_length=155)
    status_choices = (
        ("CE", "CANCELLED"),
        ("UP", "UPCOMING"),
        ("FT", "FOUGHT"),
    )
    result_choices = (
        ("NC", "NO CONTEST"),
        ("DW", "DRAW"),
    )
    method_choices = (
        ("SM", "SUBMISSION"),
        ("KO", "KNOCKOUT"),
        ("TKO", "TECHNICAL KNOCKOUT"),
    )
    card_choices = (
        ("0", "MAIN CARD"),
        ("1", "PRELIMS"),
        ("2", "EARLY PRELIMS"),
    )
    tier_choices = (
        ("0", "fight-0"),
        ("1", "fight-1"),
        ("2", "fight-2"),
        ("3", "fight-3"),
        ("4", "fight-4"),
    )
    fighter_participation =         models.ManyToManyField(FighterProfile, through=Participation, through_fields=(
        "fight",
        "fighter")
        )
    number_of_rounds =              models.PositiveIntegerField()
    # weight_division =               models.ForeignKey(WeightDivision, on_delete=models.CASCADE)
    t_round =                       models.FloatField()
    status =                        models.CharField(max_length=155, choices=status_choices)
    result =                        models.CharField(max_length=155, choices=result_choices,  null=True, blank=True)
    method =                        models.CharField(max_length=155, choices=method_choices,  null=True, blank=True)
    card =                          models.CharField(max_length=155, choices=card_choices,  null=True, blank=True)
    tier =                          models.CharField(max_length=155, choices=tier_choices,  null=True, blank=True)
    # early_prelimns =                models.BooleanField(default=False)
    # prelimns =                      models.BooleanField(default=False)
    # main_card =                     models.BooleanField(default=False)

    def __str__(self):
        return self.name
