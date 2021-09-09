from django import forms
from django_filters import CharFilter, FilterSet

from readthedocs.audit.models import AuditLog


class UserSecurityLogForm(forms.ModelForm):

    class Meta:
        model = AuditLog
        fields = ['ip']


class UserSecurityLogFilter(FilterSet):

    ip = CharFilter(field_name='ip', lookup_expr='exact')
    project = CharFilter(field_name='log_project_slug', lookup_expr='exact')

    class Meta:
        model = AuditLog
        form = UserSecurityLogForm
        fields = ['ip']
