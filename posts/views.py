from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView): # GET Request -> List
    # template_name attribute renders a specific html
    template_name = "postsTemplates/list.html"
    # models attribute let django know from which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the variable name on how we call it inside of the template
    context_object_name = "posts"
    """
    SELECT * FROM table;
    """

class PostDetailView(DetailView): # GET Request -> Single object
    template_name = "postsTemplates/detail.html"
    model = Post
    context_object_name = "single_post"

    """
    SELECT * FROM table WHERE id = ?;
    """