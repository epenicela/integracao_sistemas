from django.contrib import admin
from .models import Vacina, Entrada, Saida, Paciente, Vacinacao, Exame
# Register your models here.


class VacinaAdmin(admin.ModelAdmin):
    list_display = (
        #'index',
        'nome_vac', 'nr_dose', 'validade', 'quantidade')
    i = 0

    @admin.display(description="#")
    def index(self, obj):
        self.i=self.i+1
        return self.i
    #index.short_description = "#"

admin.site.register(Vacina, VacinaAdmin)

admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(Paciente)
admin.site.register(Vacinacao)
admin.site.register(Exame)
