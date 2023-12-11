class DynamicArray:
    """
    Class DynamicArray implements a dynamic array to store integers.
    """

    def __init__(self, capacity=10):
        """
        Ініціалізація нового динамічного масиву

        Параметри:
        - capacity (int): Ініціалізує розмір масиву.
        """
        self._capacity = capacity  # Initial array size
        self._size = 0  # Current array size
        self._array = [None] * self._capacity  # Array initialization

    def __getitem__(self, index):
        """
        Повертає елемент за специфічним індексом.

        Параметри:
        - index (int): Індекс елемента для отримання.

        Повертає:
        - int: Елемент масиву за специфічним індексом.

        Спричиняє:
        - IndexError: Якщо індекс поза межами масиву.
        """
        if 0 <= index < self._size:
            return self._array[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        """
        Встановлює значення елемента за вказаним індексом.

        Параметри:
        - index (int): Індекс елемента, який потрібно змінити.
        - value (int): Нове значення для елемента.

        Спричиняє:
        - IndexError: Якщо індекс поза межами масиву.
        """
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of range")

    def insert(self, index, value):
        """
        Вставляє новий елемент у певну позицію в масиві.

        Параметри:
        - index (int): Позиція для вставки нового елемента.
        - value (int): Нове значення для елемента.

        Спричиняє:
        - IndexError: Якщо індекс поза межами масиву.
        """
        if self._size == self._capacity:
            self._resize()

        if 0 <= index <= self._size:
            for i in range(self._size, index, -1):
                self._array[i] = self._array[i - 1]
            self._array[index] = value
            self._size += 1
        else:
            raise IndexError("Index out of range")

    def delete(self, index):
        """
        Видаляє елемент із вказаним індексом із масиву.

        Параметри:
        - index (int): Індекс елемента для видалення.

        Спричиняє:
        - IndexError: Якщо індекс поза межами масиву.
        """
        if 0 <= index < self._size:
            for i in range(index, self._size - 1):
                self._array[i] = self._array[i + 1]
            self._array[self._size - 1] = None
            self._size -= 1
        else:
            raise IndexError("Index out of range")

    def _resize(self):
        """
        Збільшує розмір масиву, подвоюючи його.
        """
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def size(self):
        """
        Повертає поточний розмір масиву.

        Повертає:
        - int: Поточний розмір масиву.
        """
        return self._size

    def display(self):
        """
        Відображає поточні елементи в масиві.
        """
        print("Поточні елементи масиву:")
        for i in range(self._size):
            print(self._array[i], end=" ")
        print()  # Друкує пустий рядок для нового рядка

def display_elements():
    """
    Відображає поточні елементи масиву або повідомлення про відсутність елементів.
    """
    if arr.size() != 0:
        print()
        arr.display()
        print()
    else:
        print("\nЩе немає доданих елементів у масиві!\n")


def get_element():
    """
    Отримує елемент за вказаним індексом або виводить повідомлення про відсутність елементів.
    """
    if arr.size() != 0:
        print()
        index = int(input("Введіть індекс, щоб отримати елемент:  "))
        try:
            print("Елемент за індексом {}: {}".format(index, arr[index]))
        except IndexError as e:
            print(e)
        print()
    else:
        print("\nЩе немає доданих елементів у масиві!\n")


def set_element():
    """
    Встановлює значення для елемента за вказаним індексом або виводить повідомлення про відсутність елементів.
    """
    if arr.size() != 0:
        print()
        index = int(input("Введіть індекс для встановлення елемента: "))
        value = int(input("Введіть значення: "))
        try:
            arr[index] = value
        except IndexError as e:
            print(e)
        print()
    else:
        print("\nЩе немає доданих елементів у масиві!\n")


def insert_element():
    """
    Вставляє новий елемент за вказаним індексом.
    """
    print()
    index = int(input("Введіть індекс для вставки елемента: "))
    value = int(input("Введіть значення: "))
    try:
        arr.insert(index, value)
    except IndexError as e:
        print(e)
    print()


def delete_element():
    """
    Видаляє елемент за вказаним індексом або виводить повідомлення про відсутність елементів.
    """
    if arr.size() != 0:
        print()
        index = int(input("Введіть індекс для видалення елемента: "))
        try:
            arr.delete(index)
        except IndexError as e:
            print(e)
        print()
    else:
        print("\nЩе немає доданих елементів у масиві!\n")


def get_array_size():
    """
    Виводить поточний розмір масиву.
    """
    print("\nПоточний розмір масиву: ", arr.size(), "\n")

def exit_program():
    """
    Виводить повідомлення про вихід з програми.
    """
    print("\nВихід з програми...\n")

options = {
    "1": insert_element,
    "2": display_elements,
    "3": get_element,
    "4": set_element,
    "5": delete_element,
    "6": get_array_size,
    "7": exit_program
}

def display_menu():
    print("Меню динамічного масиву")
    print("1. Вставити елемент")
    print("2. Показати елементи масиву")
    print("3. Отримати елемент за індексом")
    print("4. Замінити елемент за індексом")
    print("5. Видалити елемент")
    print("6. Отримати поточний розмір масиву")
    print("7. Вийти")
    choice = input("Введіть ваш вибір: ")
    return choice


if __name__ == "__main__":
    arr = DynamicArray()

    while True:
        user_choice = display_menu()

        if user_choice in options:
            options[user_choice]()
        else:
            print("Неправильний вибір. Будь ласка, введіть правильний вибір.")
        if user_choice == "7":
            break
