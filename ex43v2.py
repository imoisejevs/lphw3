import sys

#L1
# overall class that defines what all scenes should be able to do
class Scene(object):

    #interesting, no init method from which I gather we never instantiate this?

    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and implement enter().")
        sys.exit(1)



# engine class that pushes the game forward
class Engine(object):

    def __init__(self, scene_map):
        print("///loading the map...")
        self.scene_map = scene_map

    def play(self):
        print("///setting the first and last scenes, only ONCE...")
        current_scene = self.scene_map.opening_scene() #starts with CentralCorridor()
        last_scene = self.scene_map.next_scene('finished') #Finished()

        #recursion
        def recursive_action(current_scene):
            print("///loading the next scene...")
            next_scene_name = current_scene.enter() #this both enters the current scene and returns the next scene name
            print("ready to move?")
            move = input("> ")
            if move == "yes":
                current_scene = self.scene_map.next_scene(next_scene_name) #this fetches the next method after #CentralCorridor() etc
            else:
                current_scene = self.scene_map.next_scene("death") #this fetches death
            return recursive_action(current_scene)

        recursive_action(current_scene)

        # #his version
        # while current_scene != last_scene:
        #     print("///loading the next scene...")
        #     next_scene_name = current_scene.enter() #this both enters the current scene and returns the next scene name
        #     print("ready to move?")
        #     move = input("> ")
        #     if move == "yes":
        #         current_scene = self.scene_map.next_scene(next_scene_name) #this fetches the next method after #CentralCorridor() etc
        #     else:
        #         current_scene = self.scene_map.next_scene("death") #this fetches death

        current_scene.enter()

#L2
# all the different scenes - these should only contain actions within a scene
class Death(Scene):

    def enter(self):
        print('what a fucking loser - you died!!!!')
        sys.exit(0)

class Finished(Scene):

    def enter(self):
        print('you won!!!')
        sys.exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print("you arrive in the corridor, see a monster, and defeat the fucker! ONWARDS!")
        return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("you arrive in the armory, guess the pin, and obtain the weapon! ONWARDS!")
        return 'the_bridge'

class TheBridge(Scene):

    def enter(self):
        print("you arrive at the bridge, see another monster, and defeat the fucker! ONWARDS!")
        return "escape_pod"

class EscapePod(Scene):

    def enter(self):
        print("finally you arrive in the escape pod area, guess the pod, plant the bomb, and eject yourself before the explosion!")
        return 'finished'


#map class takes care of all the navigation
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val #returns the method

    def opening_scene(self):
        print("you arrive at the abandoned ship. lets figure shit out")
        return self.next_scene(self.start_scene)



#play
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

#learnings
# needed to write "this scene is not yet configured" in the top class
# didn't have to instantiate the class at all - just call the method directly
# the enter method should have been moved up into play, and the map should really just be a dictionary. this would save me from 25 IF statements implemented in the map
# I didn't use any "return"s! - arguably makes code harder to read
# another improvement I can make is to replace his while loop with recursion
