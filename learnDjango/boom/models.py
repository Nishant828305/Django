from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class chaiVariety(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('CD', 'CARDAMOM'),
    ('TL', 'TULSI'),
    ('LM', 'LEMON'),
    ('AD', 'ADAKAHWA'),  # a Kashmiri spiced tea
    ('EL', 'ELAICHI'),
    ('BM', 'BOMBAY CUTTING'),
    ('SK', 'SAFFRON KESAR'),
    ('IC', 'ICE CHAI')
]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type  = models.CharField(max_length=2,choices =CHAI_TYPE_CHOICE)
  description = models.TextField(default='')
  
  def __str__(self):
    return self.name 
  
  # one to many
  
class chaiReview(models.Model):
  chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name="reviews")
  user = models.ForeignKey(User , on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)