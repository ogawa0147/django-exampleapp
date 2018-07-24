from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.forms import ModelForm

from cms.models import Book, Impression


class ImpressionList(ListView):
    """
    感想の一覧
    """
    context_object_name = 'impressions'
    template_name = 'impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])  # 親の書籍を読む
        impressions = book.impressions.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)    
        return self.render_to_response(context)


def edit(request, book_id, impression_id=None):
    """
    感想の編集
    """
    book = get_object_or_404(Book, pk=book_id)  # 親の書籍を読む

    # impression_id が指定されている (修正時)
    if impression_id:

        impression = get_object_or_404(Impression, pk=impression_id)

    # impression_id が指定されていない (追加時)
    else:

        impression = Impression()

    if request.method == 'POST':

        # POST された request データからフォームを作成
        form = ImpressionForm(request.POST, instance=impression)

        # フォームのバリデーション
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book  # この感想の、親の書籍をセット
            impression.save()
            return redirect('cms:impression/list', book_id=book_id)

    # GET の時
    else:

        # impression インスタンスからフォームを作成
        form = ImpressionForm(instance=impression)

    return render(request,
                  'impression_edit.html',
                  dict(form=form, book_id=book_id, impression_id=impression_id))


def delete(request, book_id, impression_id):
    """
    感想の削除
    """
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression/list', book_id=book_id)


class ImpressionForm(ModelForm):
    """
    感想のフォーム
    """
    class Meta:
        model = Impression
        fields = ('comment', )
