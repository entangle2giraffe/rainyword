import time

class Player:

    def __init__(self, ID:int) -> None:
        """Initialize Player Class"""
        self._ID = ID
        self._point = 0

    # @property Decorators for protected members
    @property
    def ID(self):
        return self._ID

    @property
    def point(self):
        return self._point
    
    # @setter Decorators for setting a new point value
    @point.setter
    def point(self,point):
        self._point = point

    def add_point(self):
        self.point += 1

    def point_reset(self):
        self.point = 0

    def __str__(self) -> str:
        return f'Player(ID={self.ID}, Point={self.point})'

class Word():

    def __init__(self, ID, word:str) -> None:
        self._ID = ID
        self._time = time.time() 
        self.word = word

    @property
    def ID(self):
        return self._ID

    @property
    def time(self):
        return self._time

    def __str__(self) -> str:
        return f'Word({self.time} ID={self.ID}, {self.word})'

# Test cases
if __name__ == "__main__":
    import json 

    p = Player(1)
    p.add_point()
    print(p.__str__())
    p.point = 10 
    print(p.__str__())
    jsonstr = json.dumps(p.__dict__)
    print(jsonstr)
    p.point_reset()
    print(p.__str__())
    w = Word(1, "word here")
    print(w)
    w = Word(2, "word not here")
    print(w)
    jsonstr = json.dumps(w.__dict__)
    print(jsonstr)