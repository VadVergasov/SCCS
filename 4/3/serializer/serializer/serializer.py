"""
Implementing serializer class
"""
import inspect

class Serializer:
    """
    Serializer class
    """
    def serialize(self, obj: object):
        """
        Serialization function
        """
        if inspect.isclass(obj):
            pass
        else:
            pass
