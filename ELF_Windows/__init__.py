from . import windows
from . import RepeateTime
class Main(windows.BadWindows , RepeateTime.RepeatedTimer):
    def __init__(self) -> None:
        super().__init__()
