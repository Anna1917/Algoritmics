import random

number = 0

class Array():


    def __init__(self, *lst):
        super().__init__()
        self._list = [*lst]

    def _len(self):
        return len(self._list)

    def _append(self, item):
        self._list.append(item)

    def _sort(self):
        self._list.sort()

    def _index(self, other):
        if other in self._list:
            return self._list.index(other)
        else:
            return -1

    def _find(self, value):
        for i in range(len(self._list)):
            if self._list[i] == value:
                return True
        return False

    def _delete(self, value):
        if a in self._list:
            for i in range(a, len(self._list) - 1):
                self._list[i] = self._list[i+1]
            self.list = self._list[:-1]
            print('Элемент', self._list[a],'успешно удален.')
        else:
            print('Такого элемента нет')

    def _get_min(self):
        a = self._list[0]
        for i in range(1, len(self._list)):
            if self._list[i] > a:
                a = self._list[i]
        return a

    def _get_max(self):
        a = self._list[0]
        for i in range(1, len(self._list)):
            if self._list[i] < a:
                a = self._list[i]
        return a

    def _display(self):
        print(f'{self._list}')

    def _contains(self, value):
        global number

        for i in range(len(self._list)):
            number = number + 1
            if self._list[i] == value:
                return True
        return False


array = Array()

for i in range(100):
    a = random.randint(-100, 100)
    array._append(a)

array._sort()
array._display()

x1 = random.randint(-100, 100)
x2 = random.randint(-100, 100)
print(x1)
if array._find(x1):
    print('Значение', x1, 'было найдено среди эллементов в массива.')
else:
    print('Значение', x1, 'не было найдено среди эллементов в массива.')

x1 = random.randint(-100, 100)
print(x1)
if array._contains(x1):
    print('Значение', x1, 'было найдено среди эллементов в массива. Оно на', number, 'месте.')
else:
    print('Значение', x1, 'не было найдено среди эллементов в массива.')

print('Минимальное значение:', array._get_min())
print('Максимальное значение:', array._get_max())

array._delete(x2)