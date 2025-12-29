from dataclasses import dataclass
from typing import Optional


@dataclass
class Request:
    amount: int


class Handler:
    def __init__(self):
        self._next: Optional["Handler"] = None

    def set_next(self, nxt: "Handler") -> "Handler":
        self._next = nxt
        return nxt

    def handle(self, request: Request) -> str:
        if self._next:
            return self._next.handle(request)
        return "No handler could process the request"


class SmallAmountHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.amount <= 100:
            return f"SmallAmountHandler handled: {request.amount}"
        return super().handle(request)


class MediumAmountHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.amount <= 1000:
            return f"MediumAmountHandler handled: {request.amount}"
        return super().handle(request)


class LargeAmountHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.amount > 1000:
            return f"LargeAmountHandler handled: {request.amount}"
        return super().handle(request)


if __name__ == "__main__":
    h1 = SmallAmountHandler()
    h2 = MediumAmountHandler()
    h3 = LargeAmountHandler()
    h1.set_next(h2).set_next(h3)

    for amt in [50, 700, 5000]:
        print(h1.handle(Request(amt)))
