from django.contrib import admin
from django import forms

from company.models import Position, Department, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    ...


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'chief')


class EmployeeModelForm(forms.ModelForm):

    def clean(self):

        cleaned_data = super().clean()

        if self.instance and 'department' in self.changed_data \
                and Department.objects.filter(chief=self.instance).exists():
            self.add_error('department', 'У директора отдела нельзя менять отдел. Сначала назначьте другого директора.')

        return cleaned_data


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position', 'department', 'salary')
    list_filter = ('department',)
    search_fields = ('last_name', 'first_name', 'patronymic')
    form = EmployeeModelForm
