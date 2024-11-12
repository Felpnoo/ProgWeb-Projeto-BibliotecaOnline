from django import forms
from .models import Autor, Livro, Aluno, Emprestimo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome',
                  'sobrenome',
                  'email']
        labels = {'nome': 'Nome',
                  'sobrenome': 'Sobrenome',
                  'email': 'Email'}
        widget = {'nome': forms.TextInput(attrs={'class': 'form-control'}),
                  'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'})}
        
        
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo',
                  'autor',
                  'isbn',
                  'paginas',
                  'reservado']
        labels = {'titulo': 'Titulo',
                  'autor': 'Autor',
                  'isbn': 'ISBN',
                  'paginas': 'Paginas',
                  'reservado': 'Reservado'}
        widget = {'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                  'autor': forms.Select(attrs={'class': 'form-control'}),
                  'isbn': forms.TextInput(attrs={'class': 'form-control'}),
                  'paginas': forms.NumberInput(attrs={'class': 'form-control'}),
                  'reservado': forms.CheckboxInput(attrs={'class': 'form-control'})}
        
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome',
                  'sobrenome',
                  'email']
        labels = {'nome': 'Nome',
                  'sobrenome': 'Sobrenome',
                  'email': 'Email'}
        widget = {'nome': forms.TextInput(attrs={'class': 'form-control'}),
                  'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'})}
        
class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro',
                  'aluno',
                  'data_emprestimo',
                  'data_devolucao',
                  'devolvido']
        labels = {'livro': 'Livro',
                  'aluno': 'Aluno',
                  'data_emprestimo': 'Data de Emprestimo',
                  'data_devolucao': 'Data de Devolucao',
                  'devolvido': 'Devolvido'}
        widget = {'livro': forms.Select(attrs={'class': 'form-control'}),
                  'aluno': forms.Select(attrs={'class': 'form-control'}),
                  'data_emprestimo': forms.DateInput(attrs={'class': 'form-control'}),
                  'data_devolucao': forms.DateInput(attrs={'class': 'form-control'}),
                  'devolvido': forms.CheckboxInput(attrs={'class': 'form-control'})}
        
