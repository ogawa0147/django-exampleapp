from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.forms import ModelForm

from cms.models import Book


def list(request):
    """
    書籍の一覧
    """
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'book_list.html',     # 使用するテンプレート
                  {'books': books})     # テンプレートに渡すデータ


def edit(request, book_id=None):
    """
    書籍の編集
    """
    # return HttpResponse('書籍の編集')

    # book_id が指定されている (修正時)
    if book_id:

        book = get_object_or_404(Book, pk=book_id)

    # book_id が指定されていない (追加時)
    else:

        book = Book()

    if request.method == 'POST':

        # POST された request データからフォームを作成
        form = BookForm(request.POST, instance=book)
        
        # フォームのバリデーション
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book/list')

    # GET の時
    else:

        # book インスタンスからフォームを作成
        form = BookForm(instance=book)

    return render(request,
                  'book_edit.html',
                  dict(form=form, book_id=book_id))


def delete(request, book_id):
    """
    書籍の削除
    """
    # return HttpResponse('書籍の削除')

    book = get_object_or_404(Book, pk=book_id)
    book.delete()

    return redirect('cms:book/list')


class BookForm(ModelForm):
    """
    書籍のフォーム
    """
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page', )
