from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test_text"] = "This is Django test text!"
        return context
