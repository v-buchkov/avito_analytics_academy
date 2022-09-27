"""
Buchkov Viacheslav, DS Track, Python - HW2
"""
from keyword import iskeyword


class InnerClass:
    """
    This class creates objects for inner attributes creation from the dictionary
    """
    def __init__(self, dict_self):
        self.dict_self = dict_self

    # Representation change allows to return the dict of attrs, when the parent attr is called
    def __repr__(self):
        return str(dict(self.dict_self))


class DictToAttrs:
    """
    This class reads the dictionary and creates the attributes from key-value pairs
    ! Class is not specific to this HW and can be fully reused in further applications
    """
    def __init__(self, input_dict: dict):
        # Set initial attributes (decompose first-level dict)
        self.set_attributes(self, input_dict, '_')
        # Decompose inner dicts
        self.decompose_inner()

    # Method for setting attributes to an object from a dict
    @staticmethod
    def set_attributes(obj: object, python_dict: dict, privatness: str = '') -> None:
        for key, value in python_dict.items():
            setattr(obj, privatness + key, value)

    # Method that operates with inner dicts, decomposing all into sub-attrs to the main attr - key to this dict
    def decompose_inner(self) -> None:
        # List of attribute names
        attr_names = list(vars(self))
        for attr_name in attr_names:
            # Value for the given attribute
            attr_obj = getattr(self, attr_name)
            # If the attr name corresponds to a dict, should decompose
            if type(attr_obj) == dict:
                # Set attr as an InnerClass to add sub-attrs
                setattr(self, attr_name, InnerClass(attr_obj))
                # Set sub-attrs to attr
                self.set_attributes(getattr(self, attr_name), attr_obj)


class ColorizeMixin:
    """
    ColorizeMixin allows to change the color of the text
    """
    repr_color_code = 33

    def __repr__(self):
        self.repr_starter = f'\033[1;{self.repr_color_code};40m '


class Advert(ColorizeMixin, DictToAttrs):
    """
    Main Class to work with advertisements

    Required inputs are set as list (in this HW as one value only)
    """
    REQUIRED_INPUTS = ['title']

    def __init__(self, json_dict):
        super().__init__(json_dict)
        self.rename_super_attrs()
        self.check_required_inputs()

    def rename_super_attrs(self):
        """
        Parent attrs are set in the form of '_{attr}' to avoid interference with child properties
        This function changes the attribute keys to '{attr}' format with regard to the created properties
        """
        for key, value in dict(vars(self)).items():
            new_key = key.lstrip('_')
            # If the 'new_key' value is not in the list of attrs and properties already
            if new_key not in dir(self):
                if iskeyword(new_key):
                    setattr(self, new_key + '_', value)
                else:
                    setattr(self, new_key, value)

    def check_required_inputs(self):
        """
        Check, if all required inputs are present (from REQUIRED_INPUTS list)
        """
        requirements = [req_input in list(vars(self)) for req_input in self.REQUIRED_INPUTS]
        assert all(requirements), f'Please, check required inputs: {", ".join(self.REQUIRED_INPUTS)}'

    @property
    def price(self, default_value: float = 0):
        # Get value and set to default value, if not in the dictionary
        advert_price = vars(self).get('_price', default_value)
        if advert_price < 0:
            raise ValueError('Price must be non-negative!')
        return advert_price

    def __repr__(self):
        """
        Child repr will always rewrite the Parent repr
        Therefore, here we call Parent repr that will redefine self.repr_starter
        If ColorizeMixin will not be in the Parent classes, it will still return correct format (with standard color)
        """
        self.repr_starter = ''
        # Parent repr reclaims the
        super().__repr__()
        return self.repr_starter + f'{self.title} | {self.price} RUB'
