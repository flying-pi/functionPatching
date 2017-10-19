from function_store import adder
from peta_module import peta_function


def mock_peta(a, b):
    return a * b


store_fun = peta_function


class PatchForPeta():
    stored_calls = []

    def __call__(self, a, b):
        self.stored_calls.append(tuple([a, b]))
        return mock_peta(a, b)


patch = PatchForPeta()
adder.__globals__.update({'peta_function': patch})

result = adder(5)
print(result)
print('stored results :: ', patch.stored_calls)

adder.__globals__.update({'peta_function': peta_function})

result = adder(5)
print(result)
