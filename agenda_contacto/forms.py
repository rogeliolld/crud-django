from django import forms  
from agenda_contacto.models import Contacto  
class ContactoForm(forms.ModelForm):  
    class Meta:  
        model = Contacto
        fields = "__all__"