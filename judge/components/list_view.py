from django_unicorn.components import UnicornView
from django.contrib.auth.models import User
from django.contrib import messages


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

    filter_postcode_range = ""
    filter_postcode_range_plz = ""
    filter_postcode_range_en = False

    def toggle_filters(self):
        self.show_filters = not self.show_filters

    def filter_judge(self):
        usr = self.get_managed_judges()
        # filter first_name
        if self.filter_first_name_en:
            if self.filter_opt_first_name == "contains":
                usr = usr.filter(first_name__icontains=self.filter_first_name)
            elif self.filter_opt_first_name == "startswith":
                usr = usr.filter(
                    first_name__istartswith=self.filter_first_name)
            elif self.filter_opt_first_name == "endswith":
                usr = usr.filter(first_name__iendswith=self.filter_first_name)
            elif self.filter_opt_first_name == "exact":
                usr = usr.filter(first_name__iexact=self.filter_first_name)

        # filter last_name
        if self.filter_last_name_en:
            if self.filter_opt_last_name == "contains":
                usr = usr.filter(last_name__icontains=self.filter_last_name)
            elif self.filter_opt_last_name == "startswith":
                usr = usr.filter(
                    last_name__istartswith=self.filter_last_name)
            elif self.filter_opt_last_name == "endswith":
                usr = usr.filter(last_name__iendswith=self.filter_last_name)
            elif self.filter_opt_last_name == "exact":
                usr = usr.filter(last_name__iexact=self.filter_last_name)

        # filter region
        if self.filter_region_en:
            usr = usr.filter(judge__region__name__icontains=self.filter_region)

        # filter club
        if self.filter_club_en:
            if self.filter_opt_club == "contains":
                usr = usr.filter(judge__club__icontains=self.filter_club)
            elif self.filter_opt_club == "startswith":
                usr = usr.filter(judge__club__istartswith=self.filter_club)
            elif self.filter_opt_club == "endswith":
                usr = usr.filter(judge__club__iendswith=self.filter_club)
            elif self.filter_opt_club == "exact":
                usr = usr.filter(judge__club__iexact=self.filter_club)

        # filter email
        if self.filter_email_en:
            if self.filter_opt_email == "contains":
                usr = usr.filter(email__icontains=self.filter_email)
            elif self.filter_opt_email == "startswith":
                usr = usr.filter(
                    email__istartswith=self.filter_email)
            elif self.filter_opt_email == "endswith":
                usr = usr.filter(email__iendswith=self.filter_email)
            elif self.filter_opt_email == "exact":
                usr = usr.filter(email__iexact=self.filter_email)

         # filter postcode
        if self.filter_postcode_en:
            if self.filter_opt_postcode == "contains":
                usr = usr.filter(
                    judge__postcode__icontains=self.filter_postcode)
            elif self.filter_opt_postcode == "startswith":
                usr = usr.filter(
                    judge__postcode__istartswith=self.filter_postcode)
            elif self.filter_opt_postcode == "endswith":
                usr = usr.filter(
                    judge__postcode__iendswith=self.filter_postcode)
            elif self.filter_opt_postcode == "exact":
                usr = usr.filter(judge__postcode__iexact=self.filter_postcode)

        # filter postcode range
        if self.filter_postcode_range_en:
            try:
                usr_in_range = []
                for u in usr:
                    if u.judge.is_in_range(self.filter_postcode_range_plz, self.filter_postcode_range):
                        usr_in_range.append(u.pk)
                print(usr_in_range)
                usr = usr.filter(pk__in=usr_in_range)
            except ValueError:
                messages.error(self.request, "PLZ ist nicht korrekt")

        # filter city
        if self.filter_city_en:
            if self.filter_opt_city == "contains":
                usr = usr.filter(judge__city__icontains=self.filter_city)
            elif self.filter_opt_city == "startswith":
                usr = usr.filter(judge__city__istartswith=self.filter_city)
            elif self.filter_opt_city == "endswith":
                usr = usr.filter(judge__city__iendswith=self.filter_city)
            elif self.filter_opt_city == "exact":
                usr = usr.filter(judge__city__iexact=self.filter_city)

        self.user_filtered = usr

    def get_managed_judges(self):
        usr = User.objects.all()

        if self.request.user.is_superuser:
            return usr
        else:
            usrTMP = User.objects.none()
            for reg in self.request.user.judge.managed_regions.all():
                usrTMP = usrTMP | usr.filter(
                    judge__region__name__icontains=reg.name)
            return usrTMP

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.filter_judge()
        self.regions = self.request.user.judge.managed_regions.all()
