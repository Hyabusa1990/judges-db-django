from django_unicorn.components import UnicornView
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class ListViewView(UnicornView):
    item_per_page = 20
    user_filtered = Paginator(User.objects.none, item_per_page)
    user_displayed = User.objects.none
    filter = {}

    def filter_judge(self):
        usr = User.objects.all()
        # TODO: ADD filters on QuerySet
        self.user_filtered = Paginator(usr, self.item_per_page)
        self.update_displayed_user()

    def update_displayed_user(self):
        self.user_displayed = self.user_filtered.object_list

    def mount(self):
        self.filter_judge()
