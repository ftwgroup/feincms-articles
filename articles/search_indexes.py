from django.db.models.fields import FieldDoesNotExist
from haystack import indexes

from models import Article


class TempArticleIndex(indexes.SearchIndex):
    title = indexes.CharField(model_attr='title')
    name = indexes.CharField(model_attr='title')
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, *args, **kwargs):
        return self.get_model().objects.active()

    def get_updated_field(self, *args, **kwargs):
        try:
            self.get_model()._meta.get_field('modification_date')
        except FieldDoesNotExist:
            return None
        else:
            return 'modification_date'


# from haystack import site
class ArticleIndex(TempArticleIndex, indexes.Indexable):
    pass


# site.register(Article, ArticleIndex)
