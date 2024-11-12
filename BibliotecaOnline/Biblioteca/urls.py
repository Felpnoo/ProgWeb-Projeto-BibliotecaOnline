from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autor/novo', views.novo_autor, name='novo_autor'),
    path('autor/editar/<int:id>', views.novo_autor, name='editar_autor'),
    path('autor/delete/<int:id>', views.delete_autor, name='delete_autor'),
    path('autores', views.autores, name='autores'),
    
    path('livro/novo', views.novo_livro, name='novo_livro'),
    path('livro/editar/<int:id>', views.novo_livro, name='editar_livro'),
    path('livro/delete/<int:id>', views.delete_livro, name='delete_livro'),
    path('livros', views.livros, name='livros'),
    
    path('aluno/novo', views.novo_aluno, name='novo_aluno'),
    path('aluno/editar/<int:id>', views.novo_aluno, name='editar_aluno'),
    path('aluno/delete/<int:id>', views.delete_aluno, name='delete_aluno'),
    path('alunos', views.alunos, name='alunos'),
    
    path('emprestimo/novo', views.novo_emprestimo, name='novo_emprestimo'),
    path('emprestimo/editar/<int:id>', views.novo_emprestimo, name='editar_emprestimo'),
    path('emprestimo/delete/<int:id>', views.delete_emprestimo, name='delete_emprestimo'),
    path('emprestimos', views.emprestimos, name='emprestimos'),
]