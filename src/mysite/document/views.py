from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Document

@login_required
def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = request.user.document.all()

    if docid != 0:
        document = Document.objects.filter(pk=docid)
        document = list(document)
        if document == []:
            return redirect('/editor')
        else:
            document = document[0]
        if document not in documents:
            return redirect('/editor')

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        public = False
        if request.POST.get('public') == "clicked":
            public = True
        # public = request.POST.get('public')

        if docid > 0:
            document = Document.objects.filter(pk=docid)
            document = list(document)
            if document == []:
                return redirect('/editor')
            else:
                document = document[0]
            if document not in documents:
                return redirect('/editor')
            document.title = title
            document.content = content
            document.public = public
            document.save()

            return redirect('/editor/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content, public=public)
            
            request.user.document.add(document)
            return redirect('/editor/?docid=%i' % document.id)

    if docid > 0:
        document = Document.objects.filter(pk=docid)
        document = list(document)
        if document == []:
            return redirect('/editor')
        else:
            print(document,"-----------------")
            document = document[0]
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document,
        # 'public': public
    }

    return render(request, 'document/editor.html', context)

@login_required
def delete_document(request, docid):
    documents = request.user.document.all()
    document = Document.objects.filter(pk=docid)
    document = list(document)
    if document == []:
        return redirect('/editor')
    else:
        document = document[0]

    if document in documents:
        document.delete()

    return redirect('/editor/?docid=0')