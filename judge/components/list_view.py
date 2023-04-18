from django_unicorn.components import UnicornView
from django.contrib.auth.models import User


class ListViewView(UnicornView):
    user_filtered = User.objects.none()
    regions = []
    filter = []

    operator_options = ["contains", "startswith", "endswith", "exact"]

    show_filters = False

    filter_first_name = ""
    filter_opt_first_name = "contains"
    filter_first_name_en = False

    filter_last_name = ""
    filter_opt_last_name = "startswith"
    filter_last_name_en = False

    filter_region = ""
    filter_region_en = False

    filter_club = ""
    filter_opt_club = "contains"
    filter_club_en = False

    filter_email = ""
    filter_opt_email = "contains"
    filter_email_en = False

    filter_postcode = ""
    filter_opt_postcode = "contains"
    filter_postcode_en = False

    filter_city = ""
    filter_opt_city = "contains"
    filter_city_en = False

    def toggle_filters(self):
        self.show_filters = not self.show_filters

    def filter_judge(self):
        usr = User.objects.all()
        # filter first_name
        if self.filter_first_name_en:
            if self.filter_opt_first_name is "contains":
                usr = usr.filter(first_name__icontains=self.filter_first_name)
            elif self.filter_opt_first_name is "startswith":
                usr = usr.filter(
                    first_name__istartswith=self.filter_first_name)
            elif self.filter_opt_first_name is "endswith":
                usr = usr.filter(first_name__iendswith=self.filter_first_name)
            elif self.filter_opt_first_name is "exact":
                usr = usr.filter(first_name__iexact=self.filter_first_name)

        # filter last_name
        if self.filter_last_name_en:
            if self.filter_opt_last_name is "contains":
                usr = usr.filter(last_name__icontains=self.filter_last_name)
            elif self.filter_opt_last_name is "startswith":
                usr = usr.filter(
                    last_name__istartswith=self.filter_last_name)
            elif self.filter_opt_last_name is "endswith":
                usr = usr.filter(last_name__iendswith=self.filter_last_name)
            elif self.filter_opt_last_name is "exact":
                usr = usr.filter(last_name__iexact=self.filter_last_name)

        # filter region
        if self.filter_region_en:
            usr = usr.filter(judge__region__icontains=self.filter_region)

        # filter club
        if self.filter_club_en:
            if self.filter_opt_club is "contains":
                usr = usr.filter(judge__club__icontains=self.filter_club)
            elif self.filter_opt_club is "startswith":
                usr = usr.filter(judge__club__istartswith=self.filter_club)
            elif self.filter_opt_club is "endswith":
                usr = usr.filter(judge__club__iendswith=self.filter_club)
            elif self.filter_opt_club is "exact":
                usr = usr.filter(judge__club__iexact=self.filter_club)

        # filter email
        if self.filter_email_en:
            if self.filter_opt_email is "contains":
                usr = usr.filter(email__icontains=self.filter_email)
            elif self.filter_opt_email is "startswith":
                usr = usr.filter(
                    email__istartswith=self.filter_email)
            elif self.filter_opt_email is "endswith":
                usr = usr.filter(email__iendswith=self.filter_email)
            elif self.filter_opt_email is "exact":
                usr = usr.filter(email__iexact=self.filter_email)

         # filter postcode
        if self.filter_postcode_en:
            if self.filter_opt_postcode is "contains":
                usr = usr.filter(
                    judge__postcode__icontains=self.filter_postcode)
            elif self.filter_opt_postcode is "startswith":
                usr = usr.filter(
                    judge__postcode__istartswith=self.filter_postcode)
            elif self.filter_opt_postcode is "endswith":
                usr = usr.filter(
                    judge__postcode__iendswith=self.filter_postcode)
            elif self.filter_opt_postcode is "exact":
                usr = usr.filter(judge__postcode__iexact=self.filter_postcode)

        # filter city
        if self.filter_city_en:
            if self.filter_opt_city is "contains":
                usr = usr.filter(judge__city__icontains=self.filter_city)
            elif self.filter_opt_city is "startswith":
                usr = usr.filter(judge__city__istartswith=self.filter_city)
            elif self.filter_opt_city is "endswith":
                usr = usr.filter(judge__city__iendswith=self.filter_city)
            elif self.filter_opt_city is "exact":
                usr = usr.filter(judge__city__iexact=self.filter_city)

        self.user_filtered = usr

    def updating(self, name, value):
        self.filter_judge()

    def mount(self):
        self.filter_judge()
        self.regions = self.request.user.judge.managed_regions.all()
