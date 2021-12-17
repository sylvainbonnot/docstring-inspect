
def func(param1=True, param2: str = 'default val'):
    """Description of func with docstring groups style (Googledoc).

    :param param1: descr of param1 that has True for default value
    :param param2: descr of param2 (Default value = 'default val')
    :type param2: str
    :returns: some value
    :raises keyError: raises key exception
    :raises TypeError: raises type exception

    .. code-block:: python
   
        def func(x):
            return 2*x

    """
    pass

def myfunc(param1=True, param2: str = 'default val'):
    """Description of func with docstring groups style (Googledoc).

    :param param1: descr of param1 that has True for default value
    :param param2: descr of param2 (Default value = 'default val')
    :type param2: str
    :returns: some value
    :raises keyError: raises key exception
    :raises TypeError: raises type exception

    .. code-block:: python
   
        def func(x):
            return 2*x

    """
    pass

class A:
    """ """
    def method(self, param1, param2=None) -> int:
        """

        :param param1:
        :param param2:  (Default value = None)
        :rtype: int

        """
        pass