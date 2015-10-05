

class Position(object):
    """
    Position in North - East - Down coordinates
    """
    def __init__(self, latitude, longitude, down=0):
        self.lat = latitude
        self.long = longitude
        self.down = down

class GameEntity(object):

    def __init__(self):
        pass

    def update(self, time_delta):
        raise Exception("Do not know how to simulate the physics")
    
    
class Vessel(GameEntity):
    def __init__(self):
        self.position = Position(0, 0, 0)

    def update(self, time_delta):
        pass
    
    
class Game(object):
    def __init__(self):
        self._entities = list()

        self._add_game_object()
    
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