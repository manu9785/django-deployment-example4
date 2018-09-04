from django import template

register = template.Library()
@register.filter(name='cut')
#upper line  is a method template filtering through decorators in python
def cutting(value,arg):
    """
    This cuts out all values of arg from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cutting)
#this upper comment is a method custom template filter function
