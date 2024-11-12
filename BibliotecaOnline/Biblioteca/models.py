from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    paginas = models.IntegerField()
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo + ' - ' + self.autor.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return self.livro.titulo + ' - ' + self.aluno.nome
    


# Create your models here.
