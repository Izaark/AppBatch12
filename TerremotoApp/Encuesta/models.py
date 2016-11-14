from __future__ import unicode_literals

from django.db import models

Tipo_CHOICES= (
        ("Texto","Texto"),
        ("Booleno", "Boolean"),
    )

class Pregunta(models.Model):
       	#Attributes
       	tipo_respuesta = models.CharField(max_length=10, choices=Tipo_CHOICES)
    	def __str__(self):
        	return self.tipo_respuesta
class Cuestionario(models.Model):
		nombre_cuestionario = models.CharField(max_length=20, blank=False, null=False)
		pregunta = models.ForeignKey(Pregunta,blank=False,null=False,on_delete=models.CASCADE)

		def __str__(self):
			return self.nombre_cuestionario 

class Respuesta(models.Model):
        
        #Attributs
        respuesta_Bool = models.BooleanField(max_length=20,blank=False,null=False)
        respuesta_Single = models.CharField(max_length=200,blank=False,null=False)
        #Relations
        relacion_pregunta = models.ForeignKey(Pregunta, blank=False,null=False,on_delete=models.CASCADE)
        def __str__(self):
        	return self.relacion_pregunta
