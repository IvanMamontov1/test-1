from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def print(self, data: str) -> None:
        pass


class Monitor(Device):
    def print(self, data: str) -> None:
        print(f"Displaying on monitor: {data}")


class Printer(Device):
    def print(self, data: str) -> None:
        print(f"Printing to paper: {data}")


class Output(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def render(self, data: str) -> None:
        pass


class TextOutput(Output):
    def render(self, data: str) -> None:
        self.device.print(f"Text: {data}")


class ImageOutput(Output):
    def render(self, data: str) -> None:
        self.device.print(f"Image: [Binary data: {data}]")


if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    TextOutput(monitor).render("Hello, world!")
    TextOutput(printer).render("Hello, world!")
    ImageOutput(monitor).render("101010101")
