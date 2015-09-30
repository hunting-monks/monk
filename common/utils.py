def list2dict(data):
    """given a list of tuples, return a dict, where the first elements
    are keys, and the second elements are values"""
    dict = {}
    for d in data:
        dict[d[0]] = d[1]
    return dict

def list2map(data):
    """given a list of tuples, return a dict, where the second elements
    are keys, and the frist elements are values"""
    dict = {}
    for d in data:
        dict[d[1]] = d[0]
    return dict


def gen_class_with_kwargs(cls, **additionalkwargs):
    """class generator for subclasses with additional 'stored' parameters (in a closure)
     This is required to use a formset_factory with a form that need additional 
     initialization parameters (see http://stackoverflow.com/questions/622982/django-passing-custom-form-parameters-to-formset)
    """
    class ClassWithKwargs(cls):
        def __init__(self, *args, **kwargs):
            kwargs.update(additionalkwargs)
            super(ClassWithKwargs, self).__init__(*args, **kwargs)
    return ClassWithKwargs