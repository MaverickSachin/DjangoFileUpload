from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm


def index(request):

    message = "Upload as many files as you want!"

    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_document = Document(docfile=request.FILES['docfile'])
            new_document.save()

            return redirect('tutorial:index')
        else:
            message = 'The is not valid. Fix the following error.'

    else:
        form = DocumentForm()

    documents = Document.objects.all()

    context = {'documents': documents, 'form': form, 'message': message}

    return render(request, 'tutorial/index.html', context=context)
