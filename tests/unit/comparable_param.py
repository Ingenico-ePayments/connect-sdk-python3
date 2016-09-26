from ingenico.connect.sdk.request_param import RequestParam


class ComparableParam(RequestParam):
    """Request param object that can be compared to request param objects for attribute equality"""

    def __init__(self, name, value):
        super(ComparableParam, self).__init__(name, value)

    def __eq__(self, other):
        for attribute in vars(self):
            if not hasattr(other, attribute):
                return False
            else:
                s_attr = getattr(self, attribute)
                o_attr = getattr(other, attribute)
                if s_attr != o_attr:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        _hash = ""
        for attribute in vars(self):
            _hash += getattr(self, attribute)
        return _hash
