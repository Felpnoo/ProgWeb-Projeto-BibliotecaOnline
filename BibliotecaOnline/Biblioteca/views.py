from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Autor, Livro, Aluno, Emprestimo
from .forms import AutorForm, LivroForm, AlunoForm, EmprestimoForm
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def autores(request):
    autor = None  # Nenhum autor selecionado por padrão
    autores = Autor.objects.all()
    
    # Inicializar o formulário apenas com autor válido ou deixar em branco
    form = AutorForm(instance=autor) if autor else AutorForm()
    
    content = {'autores': autores, 'form': form, 'autor': autor}
    return render(request, 'form_autores.html', content)

def livros(request):
    livro = None  # Nenhum livro selecionado por padrão
    livros = Livro.objects.all()
    
    # Inicializar o formulário apenas com livro válido ou deixar em branco
    form = LivroForm(instance=livro) if livro else LivroForm()
    
    content = {'livros': livros, 'form': form, 'livro': livro}
    return render(request, 'form_livros.html', content)

def alunos(request):
    aluno = None  # Nenhum aluno selecionado por padrão
    alunos = Aluno.objects.all()
    
    # Inicializar o formulário apenas com aluno válido ou deixar em branco
    form = AlunoForm(instance=aluno) if aluno else AlunoForm()
    
    content = {'alunos': alunos, 'form': form, 'aluno': aluno}
    return render(request, 'form_alunos.html', content)

def emprestimos(request):
    try:
        # Buscar todos os empréstimos no banco de dados
        emprestimos = Emprestimo.objects.all()
        
        # Criar o formulário, se for um novo empréstimo
        form = EmprestimoForm()  # Apenas criamos o formulário sem instância de emprestimo, a não ser que seja um caso de edição

        content = {'emprestimos': emprestimos, 'form': form}
        return render(request, 'form_emprestimos.html', content)
    
    except Exception as e:
        # Caso haja erro, mostrar uma mensagem amigável
        print(f"Erro ao carregar a página de empréstimos: {e}")
        return HttpResponse("Erro interno no servidor. Por favor, tente novamente mais tarde.", status=500)

"""def emprestimos(request):
    emprestimo = None  # Nenhum emprestimo selecionado por padrão
    emprestimos = Emprestimo.objects.all()
    
    # Inicializar o formulário apenas com emprestimo válido ou deixar em branco
    form = EmprestimoForm(instance=emprestimo) if emprestimo else EmprestimoForm()
    
    content = {'emprestimos': emprestimos, 'form': form, 'emprestimo': emprestimo}
    return render(request, 'form_emprestimos.html', content)
"""

def novo_autor(request, id=None):
    """Cria ou modifica um autor"""
    autor = get_object_or_404(Autor, pk=id) if id else None
    lista_autores = Autor.objects.all()
    if request.method != 'POST':
        form = AutorForm(instance=autor)
    else:
        form = AutorForm(instance=autor, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor salvo com sucesso')
            return redirect('autores')
    context = {'form': form, 'lista_autores': lista_autores, 'autor': autor}
    return render(request, 'form_autores.html', context)

def delete_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    autor.delete()
    messages.success(request, 'Autor deletado com sucesso')
    return redirect('autores')

def novo_livro(request, id=None):
    """Cria ou modifica um livro"""
    livro = get_object_or_404(Livro, pk=id) if id else None
    lista_livros = Livro.objects.all()
    if request.method != 'POST':
        form = LivroForm(instance=livro)
    else:
        form = LivroForm(instance=livro, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro salvo com sucesso')
            return redirect('livros')
    context = {'form': form, 'lista_livros': lista_livros, 'livro': livro}
    return render(request, 'form_livros.html', context)

def delete_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    messages.success(request, 'Livro deletado com sucesso')
    return redirect('livros')

def novo_aluno(request, id=None):
    """Cria ou modifica um aluno"""
    aluno = get_object_or_404(Aluno, pk=id) if id else None
    lista_alunos = Aluno.objects.all()
    if request.method != 'POST':
        form = AlunoForm(instance=aluno)
    else:
        form = AlunoForm(instance=aluno, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno salvo com sucesso')
            return redirect('alunos')
    context = {'form': form, 'lista_alunos': lista_alunos, 'aluno': aluno}
    return render(request, 'form_alunos.html', context)

def delete_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    messages.success(request, 'Aluno deletado com sucesso')
    return redirect('alunos')

def novo_emprestimo(request, id=None):
    """Cria ou modifica um emprestimo"""
    emprestimo = get_object_or_404(Emprestimo, pk=id) if id else None
    lista_emprestimos = Emprestimo.objects.all()
    if request.method != 'POST':
        form = EmprestimoForm(instance=emprestimo)
    else:
        form = EmprestimoForm(instance=emprestimo, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emprestimo salvo com sucesso')
            return redirect('emprestimos')
    context = {'form': form, 'lista_emprestimos': lista_emprestimos, 'emprestimo': emprestimo}
    return render(request, 'form_emprestimos.html', context)

def delete_emprestimo(request, id):
    """O delete emprestimo só modifica o campo data_devolucao para a data atual e o estado de emprestimo para devolvido e do livro para disponivel"""
    emprestimo = get_object_or_404(Emprestimo, pk=id)
    
    # Obtendo o livro relacionado ao empréstimo
    livro = emprestimo.livro  # Relacionamento entre empréstimo e livro
    
    emprestimo.devolvido = True
    emprestimo.data_devolucao = datetime.now()
    livro.reservado = False  # Desmarcando o livro como reservado
    
    emprestimo.save()
    livro.save()
    
    messages.success(request, 'Empréstimo devolvido com sucesso')
    return redirect('emprestimos')