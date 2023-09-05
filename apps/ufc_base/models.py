from django.db import models
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
    

class FighterProfile(models.Model):
    full_name =         models.CharField(max_length=155)
    nickname =          models.CharField(max_length=30)
    birthdate =         models.DateField()
    native_city =       models.CharField(max_length=155)
    f_photo =           models.ImageField()
    c_photo =           models.ImageField()
    weight_division =   models.ForeignKey(WeightDivision, on_delete=models.CASCADE)
    status =            models.ForeignKey(FighterStatus, on_delete=models.SET_NULL, null=True)
    fighter_tag =       models.ForeignKey(FighterTag, on_delete=models.PROTECT, blank=True, null=True)
    #physical attributes
    age =               models.PositiveIntegerField()
    reach =             models.FloatField()
    height =            models.FloatField()
    leg_reach =         models.FloatField()
    weight =            models.FloatField()
    #fighter stats
    number_of_fights =              models.PositiveIntegerField()
    victories =                     models.PositiveIntegerField()
    losses =                        models.PositiveIntegerField()
    draws =                         models.PositiveIntegerField()
    no_contest =                    models.PositiveIntegerField()

    
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
        return str(self.fighter)


class Fight(models.Model):
    name=models.CharField(max_length=155)
    status_choices = (
        ("CE", "CANCELLED"),
        ("UP", "UPCOMING"),
        ("FT", "FOUGHT"),
    )
    result_choices = (
        ("NC", "NOCONTEST"),
        ("DW", "DRAW"),
    )
    method_choices = (
        ("SM", "SUBMISSION"),
        ("KO", "KNOCKOUT"),
        ("TKO", "TECHNICAL KNOCKOUT"),
    )
    fighter_participation =         models.ManyToManyField(FighterProfile, through=Participation, through_fields=("fight", "fighter"))
    number_of_rounds =              models.PositiveIntegerField()
    t_round =                       models.FloatField()
    status =                        models.CharField(max_length=155, choices=status_choices)
    result =                        models.CharField(max_length=155, choices=result_choices,  null=True, blank=True)
    method =                        models.CharField(max_length=155, choices=method_choices,  null=True, blank=True)
    early_prelimns =                models.BooleanField(default=False)
    prelimns =                      models.BooleanField(default=False)
    main_card =                     models.BooleanField(default=False)
    def __str__(self):
        return self.name


