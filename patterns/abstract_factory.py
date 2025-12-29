from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print("Windows Button")


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows Checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()


if __name__ == "__main__":
    app = Application(WindowsFactory())
    app.paint()
