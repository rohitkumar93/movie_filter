import django_filters
from django import forms

from .models import Movie


# class GenreMultipleChoiceFilter(django_filters.MultipleChoiceFilter):
#     def filter(self, qs, value):
#         if not value:
#             return qs
#         return super().filter(qs, value.split(','))

class CheckboxSelectMultipleWithAll(forms.CheckboxSelectMultiple):
    option_template_name = 'django/forms/widgets/checkbox_option.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value == '__all__':
            option['attrs']['class'] = 'select-all-checkbox'
        return option



GENRE_CHOICES = [
    ('War', 'War'),
    ('Animation', 'Animation'),
    ('Biography', 'Biography'),
    ('Adventure', 'Adventure'),
    ('Sport', 'Sport'),
    ('Crime', 'Crime'),
    ('Action', 'Action'),
    ('Romance', 'Romance'),
    ('Fantasy', 'Fantasy'),
    ('Documentary', 'Documentary'),
    ('Music', 'Music'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Family', 'Family'),
    ('Thriller', 'Thriller'),
    ('Sci-Fi', 'Sci-Fi'),
    ('History', 'History'),
]


class MovieFilter(django_filters.FilterSet):

    print('GENRE_CHOICES',GENRE_CHOICES)
    genre = django_filters.MultipleChoiceFilter(
        field_name='genre',
        widget=CheckboxSelectMultipleWithAll,
        label='Genre',
        choices=GENRE_CHOICES,
    )

    class Meta:
        model = Movie
        fields = ['genre']