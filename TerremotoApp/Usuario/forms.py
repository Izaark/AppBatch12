from django.contrib.auth.forms import UserCreationForm
#from .models import Usuario

class RegisterForm(UserCreationForm):
	class Meta:
		#model = Usuario
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
		]
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',			
}