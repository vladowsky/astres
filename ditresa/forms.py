from django import forms
from ditresa.models import Natal

PLANET_CHOICES = (
    ('', ''),
    ('ARI', 'Aries'),
    ('TAU', 'Taurus'),
    ('GEM', 'Gemini'),
    ('CAN', 'Cancer'),
    ('LEO', 'Leo'),
    ('VIR', 'Virgo'),
    ('LIB', 'Libra'),
    ('SCO', 'Scorpio'),
    ('SAG', 'Sagittarius'),
    ('CAP', 'Capricorn'),
    ('AQU', 'Aquarius'),
    ('PIS', 'Pisces'),
)


class NatalForm(forms.ModelForm):
    # user = forms.CharField(max_length=50, label="Имя пользователя")
    # uuid = forms.CharField(max_length=255, label="Код UUID")
    person = forms.CharField(max_length=50, label="Person name")
    # birth_date_time = forms.DateTimeField(default=timezone.now(), 
        # label='Дата рождения')
    birth_date_time = forms.CharField(max_length=50, label='Birth date')
    birth_place = forms.CharField(max_length=255, label='Birth place')
    # birth_latitude = forms.FloatField(label='Birth latitude', 
        # required=False)
    # birth_longitude = forms.FloatField(label='Birth longitude', 
        # required=False)


    sun = forms.CharField(max_length=20, label='Sun', 
        widget=forms.Select(choices=PLANET_CHOICES), required=True)
    moon = forms.CharField(max_length=20, label='Moon', 
        widget=forms.Select(choices=PLANET_CHOICES), required=True)
    mercury = forms.CharField(max_length=20, label='Mercury', 
        widget=forms.Select(choices=PLANET_CHOICES))
    venus = forms.CharField(max_length=20, label='Venus', 
        widget=forms.Select(choices=PLANET_CHOICES))
    mars = forms.CharField(max_length=20, label='Mars', 
        widget=forms.Select(choices=PLANET_CHOICES))
    jupiter = forms.CharField(max_length=20, label='Jupiter', 
        widget=forms.Select(choices=PLANET_CHOICES))
    saturn = forms.CharField(max_length=20, label='Saturn', 
        widget=forms.Select(choices=PLANET_CHOICES))
    uran = forms.CharField(max_length=20, label='Uran', 
        widget=forms.Select(choices=PLANET_CHOICES))
    neptun = forms.CharField(max_length=20, label='Neptun', 
        widget=forms.Select(choices=PLANET_CHOICES))
    pluto = forms.CharField(max_length=20, label='Pluto', 
        widget=forms.Select(choices=PLANET_CHOICES))

    class Meta:
        model = Natal
        # fields = '__all__'
        fields = ('person', 'birth_date_time', 'birth_place', 
                  'sun', 'moon','mercury','venus','mars',
                  'jupiter', 'saturn','uran', 'neptun','pluto')
        exclude = ('user', 'uuid', 'birth_latitude', 'birth_longitude')


class ReadNatalForm(forms.ModelForm):
    person = forms.CharField(max_length=50, label="Person name")
    # birth_date_time = forms.DateTimeField(default=timezone.now(), 
        # label='Дата рождения')
    birth_date_time = forms.CharField(max_length=50, label='Birth date')
    birth_place = forms.CharField(max_length=255, label='Birth place')
    # birth_latitude = forms.FloatField(label='Birth latitude', 
        # required=False)
    # birth_longitude = forms.FloatField(label='Birth longitude', 
        # required=False)

    sun = forms.CharField(max_length=20, label='Sun')
    moon = forms.CharField(max_length=20, label='Moon')
    mercury = forms.CharField(max_length=20, label='Mercury')
    venus = forms.CharField(max_length=20, label='Venus')
    mars = forms.CharField(max_length=20, label='mars')
    jupiter = forms.CharField(max_length=20, label='Jupiter')
    saturn = forms.CharField(max_length=20, label='Saturn')
    uran = forms.CharField(max_length=20, label='Uran')
    neptun = forms.CharField(max_length=20, label='Neptun')
    pluto = forms.CharField(max_length=20, label='Pluto')

    class Meta:
        model = Natal
        # fields = '__all__'
        fields = ('person', 'birth_date_time', 'birth_place', 
                  'sun', 'moon','mercury','venus','mars',
                  'jupiter', 'saturn','uran', 'neptun','pluto')
        exclude = ('user', 'uuid', 'birth_latitude', 'birth_longitude')
        readonly_fields = ('person', 'birth_date_time', 'birth_place', 
                  'sun', 'moon','mercury','venus','mars',
                  'jupiter', 'saturn','uran', 'neptun','pluto')
