from sys import exit
# from random import randint
# from textwrap import dedent

class Scene(object):

    def enter(self):
        print("None!")
        exit(1)
        
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
    
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    def enter(self):
        print('death')
        exit(1)
        
class CentralCorridor(Scene):

    def enter(self):
        print("choose")
        action = input("> ")
        if action == '3':
            print("choose 3")
            return 'death'
        elif action == '2':
            print("choose 2")
            return 'death'
        elif action == '1':
            print("right") 
            return 'laser_weapon_armory'
        else:
            print("ERROR")
            return 'central_corridor'
        
class LaserWeaponArmory(Scene):

    def enter(self):
        print("guess")
        guess = input("> ")
        if guess == '1':
            print('right')
            return 'the_bridge'
        else:
            print("wrong")
            return 'death'
        
class TheBridge(Scene):

    def enter(self):
        print('bridge')
        action = input("> ")
        if action == '1':
            print("right")
            return 'escape_pod'
        else:
            print('wrong')
            return 'death'
        
class EscapePod(Scene):
    
    def enter(self):
        print('escapepod')
        guess = input("> ")
        if guess == '1':
            print('right')
            return 'finished'
        else:
            print('wrong')
            return 'death'
        
class Finished(Scene):
    
    def enter(self):
        print("YOu win")
        return 'finished'

     
class Map(object):

    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),      
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

       
a_map = Map('central_corridor')

a_game = Engine(a_map) 

a_game.play()
