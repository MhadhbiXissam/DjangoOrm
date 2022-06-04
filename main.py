from ModelsLab import migrate
migrate()
from ModelsLab.models import Person


for i in range(100) : 
	data_dict={'name':'Nimish','age':23,"email":'nimishverma@ymail.com' , 'w' : "hhhhhhhhhhhh"}
	person = Person(**data_dict)
	person.save()

