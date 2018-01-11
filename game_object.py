class GameObject(object):
    def __init__(self, **kwargs):
        pass

    def parse_kwargs(self, kwargs, defaults):
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("Character accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)
