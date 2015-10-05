

class Position(object):
    def __init__(self):
        pass
        

class GameEntity(object):

    def __init__(self):
        self._momentum = ()

    def update(time_delta):
        pass
    
    
class Ship(GameEntity):
    pass
    
    
class Game(object):
    def __init__(self):
        self._entities = list()
    
    def main_loop(self):
        
        while True:
            time_delta = 0.01
            # Physics update
            self._update_physics(time_delta)
        
    def _update_physics(self, time_delta):
        for entity in self._entities:
            entity.update(time_delta)
        
if __name__ == '__main__':
    print "NavSim"
    game = Game()
    game.main_loop()