from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
escolha_sexo = (
	('MASCULINO', 'Masculino'),
	('FEMININO', 'Feminino'),
	)
class Perfil(models.Model):
	nome = models.CharField('Nome:', max_length=10)
	sobre_nome = models.CharField('Sobre nome:', max_length=20)
	genero = models.CharField('Sexo:', max_length=10, choices= escolha_sexo)
	facebook = models.URLField('Facebook:')
	email = models.EmailField('Digite seu E-mail:')
	favorito = models.BooleanField('Favorito:')
	def __str__(self):
		return self.nome
class Post(models.Model):
    author = models.ForeignKey ('auth.User')
    #pode se criar o campo em ingles padronizado internacionalmente e colocar em potugues
    title = models.CharField(verbose_name=u'Título',max_length=255)
    text = models.TextField('Texto')
    create_date = models.DateTimeField('Data de criação',default=timezone.now)
    publish_date = models.DateTimeField('Data para publicar',blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug / URL", help_text="Preenchido automaticamente, não editar.",)
    #
    def publish(self):
    	self.publish_date = timezone.now()
    	self.save()
    def __str__(self):
    	return self.title
    	

class Img(models.Model):
    title = models.CharField('Titulo da Imagen', max_length=150)
    id_img = models.ForeignKey('Post', on_delete=models.CASCADE,)
    img = models.ImageField(upload_to='static/img')


