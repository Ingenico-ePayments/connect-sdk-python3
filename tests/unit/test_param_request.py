import unittest

from ingenico.connect.sdk.param_request import ParamRequest
from tests.unit.comparable_param import ComparableParam


class AbstractParamRequestTest(unittest.TestCase):
    """Contains tests that test if the AbstractParamRequest class accepts the proper parameter types and refuses others
    """

    def test_add_parameter_string(self):
        """Tests that an AbstractParamRequest accepts a string as value"""
        name = "foo"
        value = "false"
        listvar = []
        reflist = [ComparableParam(name, value)]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_int(self):
        """Tests that an AbstractParamRequest accepts an int as value"""
        name = "foo"
        value = 1234567890
        listvar = []
        reflist = [ComparableParam(name, value.__str__())]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_longer_int(self):
        """Tests that an AbstractParamRequest accepts a longer int as value"""
        name = "foo"
        value = 1234567890987654321
        listvar = []
        reflist = [ComparableParam(name, value.__str__())]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_bool(self):
        """Tests that an AbstractParamRequest accepts a boolean as value"""
        name = "bar"
        value = False
        listvar = []
        reflist = [ComparableParam(name, value.__str__())]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_string_list(self):
        """Tests that an AbstractParamRequest accepts a list with a single string as value"""
        name = "foolist"
        value = ["foo"]
        listvar = []
        reflist = [ComparableParam(name, value[0].__str__())]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_int_list(self):
        """Tests that an AbstractParamRequest accepts a list of a single int as value"""
        name = "foolist"
        value = [1337]
        listvar = []
        reflist = [ComparableParam(name, str(value[0]))]
        ParamRequest()._add_parameter(listvar, name, value)
        self.assertCountEqual(reflist, listvar)

    def test_add_parameter_bool_list(self):
        """Tests that an AbstractParamRequest accepts a list of two booleans as value"""
        name = "barfoo"
        value = [False, True]
        listvar = []
        reflist = [ComparableParam(name, value[0].__str__()),
                   ComparableParam(name, value[1].__str__())]
        ParamRequest()._add_parameter(listvar, name, value)
        try:
            self.assertListEqual(reflist, listvar)
        except AttributeError:
            print(type(listvar[1]))
            print(type(reflist[1]))
            self.fail()

    def test_add_parameter_float(self):
        """Tests that an AbstractParamRequest refuses a float as value and responds with an appropriate error"""
        name = "bar"
        value = 1.9999999999
        listvar = []
        self.assertRaises(ValueError, ParamRequest()._add_parameter, listvar,
                          name, value)

    def test_add_string_list_list(self):
        """Tests that an AbstractParamRequest refuses a float as value and responds with an appropriate error"""
        name = "bar"
        value = [["foo"]]
        listvar = []
        self.assertRaises(ValueError, ParamRequest()._add_parameter, listvar,
                          name, value)


if __name__ == '__main__':
    unittest.main()
