import itertools
from collections import Counter

from django.views.generic import ListView

from core.models import Report


class Analytics(ListView):
    template_name = "analytics.html"
    queryset = Report.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        qs = self.get_queryset()

        ctx["reports_by_time"] = [
            # (time, list(reports))
            (time, Counter([r.status for r in reports]))
            for time, reports in itertools.groupby(
                qs, key=lambda x: x.created_at.strftime("%Y-%m-%d %H:%M")
            )
        ]

        return ctx
