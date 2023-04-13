from flask_login import LoginManager, login_user, logout_user, current_user
from flask_admin.contrib.sqla import ModelView
from APIs.MMUser.model.user_model import TableA, TableB, TableC, TableD, User
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import BaseSQLAFilter, FilterEqual
from wtforms.fields import SelectField


adminModels = [TableA, TableB, TableC, TableD, User]
superUserModels = [TableA, TableB, TableC, User]
jobOperatorModel = []


class CustomModelView(ModelView):

    column_searchable_list = [User.name, User.email]
    column_exclude_list = []

    def is_accessible(self):

        # Check user role here and return True or False accordingly
        # Example code assuming current_user has a role attribute
        if (current_user.name == 'chandru' and self.model in adminModels) or \
                (current_user.name == 'gattu' and self.model in superUserModels):
            return True
        else:
            return False

    def get_query(self):
        # Filter the query based on the current user
        query = super().get_query()
        if 'email' in self.model.__table__.columns:
            return query.filter_by(email=current_user.email)
        else:
            return query

    def get_filters(self):
        "Here i applied all the filter"
        filters = []
        for column in self.model.__table__.columns:
            if column.name == 'id':
                # skip primary key column
                continue
            if column.type.__class__.__name__ in ('Integer', 'Float', 'Numeric'):
                # numeric filters
                filters.append(NumericFilter(column.name, column.name))
            elif column.type.__class__.__name__ in ('String', 'Text'):
                # text filters
                filters.append(TextFilter(column.name, column.name))
            elif column.type.__class__.__name__ == 'Boolean':
                # boolean filters
                filters.append(BooleanFilter(column.name, column.name))
            elif column.type.__class__.__name__ == 'DateTime':
                # datetime filters
                filters.append(DateTimeFilter(column.name, column.name))
            elif column.type.__class__.__name__ == 'Date':
                # date filters
                filters.append(DateFilter(column.name, column.name))
            elif column.type.__class__.__name__ == 'Time':
                # time filters
                filters.append(TimeFilter(column.name, column.name))
            elif column.type.__class__.__name__ == 'Enum':
                # enum filters
                choices = [(choice, choice) for choice in column.type.enums]
                filters.append(SelectFilter(
                    column.name, column.name, choices=choices))
        return filters


# Here i have defined all the filters class based on the column types.

class NumericFilter(BaseSQLAFilter):
    def apply(self, query, value):
        if value is not None:
            return query.filter(self.column == value)

    def operation(self):
        return 'equals'


class TextFilter(BaseSQLAFilter):
    def apply(self, query, value):
        if value is not None:
            return query.filter(self.column.like('%{}%'.format(value)))

    def operation(self):
        return 'like'


class BooleanFilter(FilterEqual):
    def operation(self):
        return 'is'


class DateTimeFilter(BaseSQLAFilter):
    def apply(self, query, value):
        if value is not None:
            return query.filter(self.column == value)

    def operation(self):
        return 'equals'


class DateFilter(BaseSQLAFilter):
    def apply(self, query, value):
        if value is not None:
            return query.filter(self.column == value)

    def operation(self):
        return 'equals'


class TimeFilter(BaseSQLAFilter):
    def apply(self, query, value):
        if value is not None:
            return query.filter(self.column == value)

    def operation(self):
        return 'equals'


class SelectFilter(FilterEqual):
    def __init__(self, column, name, options=None, **kwargs):
        super(SelectFilter, self).__init__(column, name, options, **kwargs)
        self.select_field = SelectField(choices=options or [])

    def get_options(self, *args, **kwargs):
        return self.select_field.choices

    def get_value(self):
        return self.select_field.data

    def operation(self):
        return 'equals'
