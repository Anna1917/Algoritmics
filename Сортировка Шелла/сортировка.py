import time

class ShellSort:
    def __init__(self, data):
        self.data = data

    def sort(self, sequence_type='shell'):
        n = len(self.data)
        if sequence_type == 'shell':
            gaps = self.shell_sequence(n)  # Последовательность Шелла
        elif sequence_type == 'hibbard':
            gaps = self.hibbard_sequence(n)  # Последовательность Хиббарда
        elif sequence_type == 'sedgewick':
            gaps = self.sedgewick_sequence(n)  # Последовательность Седжвика
        else:
            raise ValueError("Неизвестный тип последовательности")

        # Сортировка с использованием выбранной последовательности
        for gap in gaps:
            for i in range(gap, n):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j - gap] > temp:
                    self.data[j] = self.data[j - gap]
                    j -= gap
                self.data[j] = temp

    def shell_sequence(self, n):
        """Генерация последовательности Шелла"""
        gaps = []
        h = 1
        while h < n:
            gaps.append(h)
            h = 3 * h + 1
        return gaps[::-1]  # Возвращаем последовательность в обратном порядке

    def hibbard_sequence(self, n):
        """Генерация последовательности Хиббарда"""
        gaps = []
        k = 1
        while (2**k - 1) < n:
            gaps.append(2**k - 1)
            k += 1
        return gaps[::-1]  # Возвращаем последовательность в обратном порядке

    def sedgewick_sequence(self, n):
        """Генерация последовательности Седжвика"""
        gaps = []
        k = 0
        while True:
            gap = 9 * (4**k) - 9 * (2**k) + 1
            if gap >= n:
                break
            gaps.append(gap)
            gap = 4**(k + 2) - 3 * (2**(k + 2)) + 1
            if gap < n:
                gaps.append(gap)
            k += 1
        return sorted(gaps, reverse=True)  # Возвращаем последовательность в обратном порядке

def generate_random_array(size):
    """Генерация случайного массива заданного размера"""
    import random
    return [random.randint(0, 1000) for _ in range(size)]

def measure_sorting_time(sorter, sequence_type):
    """Измерение времени выполнения сортировки"""
    start_time = time.time()
    sorter.sort(sequence_type)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [100, 1000, 10000, 100000]  # Размеры массивов для тестирования
    sequence_types = ['shell', 'hibbard', 'sedgewick']  # Типы последовательностей
    results = []

    for size in sizes:
        data = generate_random_array(size)
        for seq_type in sequence_types:
            sorter = ShellSort(data.copy())
            time_taken = measure_sorting_time(sorter, seq_type)
            results.append({
                'Тип последовательности': seq_type,
                'Размер массива': size,
                'Время (с)': time_taken
            })

    for result in results:
        print(result)