from django import template

register = template.Library()


@register.filter
def element(array, index):
    return array[index]


@register.filter
def keyvalue(dic, key):
    return dic[key]
