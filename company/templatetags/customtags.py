from django import template

register = template.Library()


@register.filter
def element(array, index):
    return array[index]


@register.filter
def keyvalue(dic, key):
    return dic[key]


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)
