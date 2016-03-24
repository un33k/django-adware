from django.contrib import messages
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _

from toolware.utils.mixin import LoginRequiredMixin
from toolware.utils.mixin import CsrfProtectMixin

from .form import AdSenseForm


class AdSenseView(LoginRequiredMixin, CsrfProtectMixin, UpdateView):
    """
    AdSense View
    """
    form_class = AdSenseForm
    success_url = reverse_lazy('adware:update_adsense')

    def get_template_names(self):
        template_name = util.get_template_path("adsense_form.html")
        return template_name

    def get_context_data(self, **kwargs):
        context = super(AccountAdView, self).get_context_data(**kwargs)
        context['adsense'] = self.object
        return context

    def get_object(self, queryset=None):
        ad = self.request.user.ad
        return ad

    def form_valid(self, form):
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, _('Your AdSense code was saved.'))
        return HttpResponseRedirect(self.get_success_url())
