import datetime as dt
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.forms import  Select, SlugField, ChoiceField, CharField, DateTimeField, DateInput, Form, IntegerField, ModelChoiceField, ModelForm, PasswordInput, Textarea, TextInput, TimeField, TimeInput, URLField
from .models import * 
from django import forms 
from ckeditor.widgets import CKEditorWidget

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class PostForm(ModelForm):
    title = CharField()
    author = CharField()
    status = ChoiceField(choices=STATUS)
    content = CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'author','status', 'content']