"""Views."""

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
@permission_required("example.basic_access")
def index(request):
    """Render index view."""
    context = {"text": "Hello, World!", "page_title": "Welcome"}
    return render(request, "example/index.html", context)
