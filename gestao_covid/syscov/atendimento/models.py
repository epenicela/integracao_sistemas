from django.db import models

# Create your models here.


#cadastro de vacinasS
class Vacina(models.Model):
    nome_vac = models.CharField(max_length=255)
    nr_dose = models.IntegerField()
    validade = models.DateField()
    quantidade = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Vacinas"
        ordering = ('nome_vac',)

    def __str__(self):
        return self.nome_vac

#entrada de vacinas no estoque
class Entrada(models.Model):
    data_entrada = models.DateField()
    quantidade_entrada = models.IntegerField(default=1)
    vacina_entrada = models.ForeignKey(Vacina, on_delete=models.CASCADE)



#vacina que serao usadas
class Saida(models.Model):
    data_saida = models.DateField()
    quantidade_saida = models.IntegerField(default=1)
    vacina_saida = models.ForeignKey(Vacina, on_delete=models.CASCADE)


#pacientes que serao testados
class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

#processo de vacinacao aos pacientes
class Vacinacao(models.Model):
    data_vacinacao = models.DateField()
    nr_dose = models.CharField(max_length=255)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Vacinações"

#Resultado de exame de covid 19
class Exame(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_exame = models.DateField()
    resultado_exame = models.BooleanField(default=False)
