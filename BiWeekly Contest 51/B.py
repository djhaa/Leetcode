class SeatManager:
    def __init__(self, n: int):
        self.data = list()
        for i in range(1, n+1):
            heappush(self.data, i)

    def reserve(self) -> int:
        return heappop(self.data)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.data, seatNumber)