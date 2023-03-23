from rest_framework import serializers

from company.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    """ Сотрудники """

    class Meta:
        model = Employee
        fields = ('last_name', 'first_name', 'patronymic', 'fio', 'photo', 'age', 'position', 'department',
                  'salary', 'birth_date')
        read_only_fields = ['age']
        extra_kwargs = {
            'birth_date': {'write_only': True},
            'last_name': {'write_only': True},
            'first_name': {'write_only': True},
            'patronymic': {'write_only': True},
        }

    def validate(self, data):

        if self.instance and data.get('department', None) != self.instance.department \
                and Department.objects.filter(chief=self.instance).exists():
            raise serializers.ValidationError(
                {'department': 'У директора отдела нельзя менять отдел. Сначала назначьте другого директора.'})

        return data


class DepartmentSerializer(serializers.ModelSerializer):
    """ Отделы """

    chief = serializers.CharField(source='chief.fio')

    class Meta:
        model = Department
        fields = ('id', 'title', 'chief', 'employees_count', 'total_salary')
