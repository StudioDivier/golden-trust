from django import forms


class CallBackForm(forms.Form):
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'name': 'name-modal1', 'placeholder': 'Введите имя*',
                                      'id': 'name-modal1', 'class': 'form-control', 'type': 'text'}
                               )
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                     attrs={'name': 'tel-modal1', 'placeholder': 'Введите телефон*',
                                            'id': 'tel-modal1', 'class': 'form-control', 'type': 'text'}
                                     )
                               )


class BuyFeedForm(forms.Form):
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'name': 'name-modal3', 'placeholder': 'Введите имя*',
                                      'id': 'name-modal3', 'class': 'form-control', 'type': 'text'}
                               )
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                     attrs={'name': 'tel-modal3', 'placeholder': 'Введите телефон*',
                                            'id': 'tel-modal3', 'class': 'form-control', 'type': 'text'}
                                     )
                               )
    email = forms.EmailField(label='', max_length=128,
                           widget=forms.EmailInput(
                               attrs={'name': 'email-modal3', 'placeholder': 'Введите email',
                                      'id': 'email-modal3', 'class': 'form-control', 'type': 'text'}
                               )
                           )


class DownFeedForm(forms.Form):
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'name': 'name-modal2', 'placeholder': 'Введите имя*',
                                      'id': 'name-modal2', 'class': 'form-control', 'type': 'text'}
                               )
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                     attrs={'name': 'tel-modal2', 'placeholder': 'Введите телефон*',
                                            'id': 'tel-modal2', 'class': 'form-control', 'type': 'text'}
                                     )
                               )
    email = forms.EmailField(label='', max_length=128,
                           widget=forms.EmailInput(
                               attrs={'name': 'email-modal2', 'placeholder': 'Введите email',
                                      'id': 'email-modal2', 'class': 'form-control', 'type': 'text'}
                               )
                           )


class FooterFeedForm(forms.Form):
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'name': 'name', 'placeholder': 'Введите имя*',
                                      'id': 'name', 'class': 'form-control', 'type': 'text'}
                               )
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                     attrs={'name': 'tel', 'placeholder': 'Введите телефон*',
                                            'id': 'tel', 'class': 'form-control', 'type': 'text'}
                                     )
                               )
    email = forms.EmailField(label='', max_length=128,
                           widget=forms.EmailInput(
                               attrs={'name': 'email', 'placeholder': 'Введите email',
                                      'id': 'email', 'class': 'form-control', 'type': 'text'}
                               )
                           )
