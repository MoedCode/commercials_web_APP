class tsto:
    def __init__(self, *args, **kwargs):
        # Initialize attributes from positional arguments
        if args:
            if len(args) > 3:
                raise ValueError("Too many positional arguments (max 3)")
            for i, arg in enumerate(args):
                self.validate_and_set(['one', 'tow', 'three'][i], arg)

        # Initialize attributes from keyword arguments
        if kwargs:
            for key, value in kwargs.items():
                self.validate_and_set(key, value)

    def validate_and_set(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"Value of '{attr_name}' must be an integer")
        setattr(self, attr_name, value)

x0 = tsto(1, 2, 3)
print(x0.__dict__)

x1 = tsto(one=4, tow=5, three=6)
print(x1.__dict__)

x2 = tsto(7, 8, three=9)
print(x2.__dict__)
