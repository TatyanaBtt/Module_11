def introspection_info(obj):
    info = {}

    info['type'] = type(obj)

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    info['module'] = obj.__module__

    if hasattr(obj, '__dict__'):
        info['__dict__'] = obj.__dict__

    info['is_class'] = isinstance(obj, type)

    info['is_callable'] = callable(obj)

    return info


class MyClass:
    def __init__(self, attr1):
        self.attr1 = attr1

    def method1(self):
        pass

    def method2(self):
        pass


class MyClass1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method3(self):
        pass

    def method4(self):
        pass


my_obj = MyClass(42)
my_obj1 = MyClass1('Alex', 25)

info = introspection_info(my_obj)
for key, value in info.items():
    print(f"{key}: {value}")
info1 = introspection_info(my_obj1)
for key, value in info1.items():
    print(f"{key}: {value}")
