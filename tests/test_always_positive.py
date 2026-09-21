from framework.decorators import test

@test("Teste sempre positivo")
def db_test():

    x = 1 + 1

    assert x == 2