# Task:
# 1) Создайте ABC класс с абстрактным методом проверки целого числа на
# простоту. Т.е., если параметром этого метода является целое число и оно
# простое, то метод должен вернуть True, а в противном случае False.
# 2) Создайте класс его наследующий.
# 3) Создайте класс, который не наследует пользовательский ABC класс, но
# обладает нужным методом. Зарегистрируйте его в качестве виртуального
# подкласса.
# 4) Проверьте работоспособность проекта.

import abc


class AbcClass(abc.ABC):

    @abc.abstractmethod
    def prime_number(self, number):
        pass


class Validator(AbcClass):

    def prime_number(self, number):
        for i in range(2, number):
            if not number % i:
                return False
        return True


class VirtualCls:

    def prime_number(self, number):
        for i in range(2, number):
            if not number % i:
                return False
        return True


a = Validator()
b = VirtualCls()

print(isinstance(b, AbcClass))
AbcClass.register(VirtualCls)
print(isinstance(b, AbcClass))
