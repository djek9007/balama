
from import_export import resources, fields

from organizations.models import Organization


class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization
        exclude = ['published', 'created_date', 'edit_date',]

