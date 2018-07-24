import json
from json import dumps
from collections import OrderedDict
from django.http import HttpResponse

from api.presenter import render, datetime

from cms.models import Book


def list(request):
    """書籍と感想のJSONを返す"""
    books = []
    for book in Book.objects.all().order_by('id'):

        impressions = []
        for impression in book.impressions.order_by('id'):
            impression_dict = OrderedDict([
                ('id', impression.id),
                ('comment', impression.comment),
            ])
            impressions.append(impression_dict)

        book_dict = OrderedDict([
            ('id', book.id),
            ('name', book.name),
            ('publisher', book.publisher),
            ('page', book.page),
            ('created_at', datetime.format(book.created_at)),
            ('updated_at', datetime.format(book.updated_at)),
            ('impressions', impressions)
        ])
        books.append(book_dict)

    data = OrderedDict([ ('books', books) ])
    return render.response(request, data)
