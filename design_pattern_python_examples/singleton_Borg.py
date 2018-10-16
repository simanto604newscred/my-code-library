__author__ = 'MAK'


class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


if __name__ == '__main__':
    x = Singleton(HTTP="Hyper Test Transfer Protocol")
    print(x)
    y = Singleton(SNMP="Single Netwrork Management Protocol")
    print(y)
    print(y.HTTP)