from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass


class BubbleSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        a = data[:]
        n = len(a)
        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a


class BuiltinSort(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        return sorted(data)


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data: list[int]) -> list[int]:
        return self.strategy.sort(data)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    sorter = Sorter(BubbleSort())
    print("Bubble:", sorter.sort(data))

    sorter.set_strategy(BuiltinSort())
    print("Builtin:", sorter.sort(data))
