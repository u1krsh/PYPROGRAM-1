class REctangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    @property   
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def length(self):
        return f"{self._length:.1f}cm"
rect = REctangle(10, 20)

