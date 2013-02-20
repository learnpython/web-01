from annoying.decorators import render_to

from .models import Bookmark


@render_to('bookmarks/index.html')
def index(request):
    """
    Show all available bookmarks.
    """
    bookmarks = Bookmark.objects.select_related()
    return {'bookmarks': bookmarks}
