from haystack import indexes

from .models import Bookmark


class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):
    """
    Bookmark search index needed for Haystack app.
    """
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')

    def get_model(self):
        return Bookmark
