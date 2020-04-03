from django.db import models

# Create your models here.
class Mylocation(models.Model):
	lat = models.TextField('Latitude')
	lon = models.TextField('Longitude')

	"""def 없으면 안 되나?"""
	"""따옴표시된 라벨은 어드민 db 제목?"""
	"""DecimalField를 TextField로 바꿈"""