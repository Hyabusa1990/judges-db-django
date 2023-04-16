from django_unicorn.components import UnicornView
from django.contrib.auth.models import User


class ListViewView(UnicornView):
    user_filtered = User.objects.none()
    filter = []

    operator_options = ["contains", "startswith", "endswith", "iexact"]

    filter_first_name = ""
    filter_opt_first_name = "contains"
    filter_first_name_en = False

    filter_last_name = ""
    filter_opt_last_name = "startswith"
    filter_last_name_en = False

    filter_email = ""
    filter_opt_email = "contains"
    filter_email_en = False

    filter_region = ""
    filter_opt_region = "contains"
    filter_region_en = False

    filter_club = ""
    filter_opt_club = "contains"
    filter_club_en = False

    filter_city = ""
    filter_opt_city = "contains"
    filter_city_en = False

    filter_postcode = ""
    filter_opt_postcode = "contains"
    filter_postcode_en = False

    def filter_judge(self):
        usr = User.objects.all()
        # TODO: ADD filters on QuerySet
        self.user_filtered = usr.filter(judge__street__contains="")

    def mount(self):
        self.filter_judge()
