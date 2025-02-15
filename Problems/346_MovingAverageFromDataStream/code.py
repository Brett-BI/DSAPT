from typing import List


class MovingAverage:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.stream: List[int] = []

    def next(self, val: int) -> float:
        self.stream.append(val)
        streamValSum: int = 0
        sIndex: int = 0

        for s in self.stream[-self.size]:
            sIndex += 1
            streamValSum += s
        
        return streamValSum / min(self.size, sIndex)