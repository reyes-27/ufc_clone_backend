from django.db import models
from apps.ufc_base import models as base_models
from django.utils.text import slugify
# Create your models here.
class RankingSpot(models.Model):
    fighter =                       models.ForeignKey(base_models.FighterProfile, on_delete=models.CASCADE, related_name="fighter_to_ranking")
    ranking =                       models.ForeignKey("Ranking", on_delete=models.CASCADE, related_name="ranking_to_fighter")
    rank_number =                   models.PositiveIntegerField(blank=True, null=True)
    champion =                      models.BooleanField(default=False)
    interm_champion =               models.BooleanField(default=False)
    class Meta:
        ordering=["rank_number"]
    
    def __str__(self):
        if self.champion == True:
            expression = f'Champion - {self.fighter}'
        elif self.interm_champion == True:
            expression = f'Interim champion - {self.fighter}'
        else:
            expression  = f'{self.rank_number} - {self.fighter}'

        return expression

class Ranking(models.Model):
    ranking_slug =                              models.SlugField(max_length=200, blank=True, null=False)
    weight_division =                           models.OneToOneField(base_models.WeightDivision, on_delete=models.CASCADE, related_name="ranking_weight")
    ranking_spot =                              models.ManyToManyField(base_models.FighterProfile, through=RankingSpot, through_fields = ('ranking', 'fighter'))
    
    def save(self, *args, **kwargs):
        if not self.ranking_slug:
            self.ranking_slug=slugify(self.weight_division)
        super(Ranking, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.weight_division} Ranking'