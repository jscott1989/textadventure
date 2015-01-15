import sys
import random

HOT = 6
WARM = 2

class Game(object):
    switch1 = False
    switch2 = False
    switch3 = False

    heat1 = 0
    heat2 = 0
    heat3 = 0

    switch1_name = "middle"
    switch2_name = "left"
    switch3_name = "right"


    def get_option(self, options):
        complete = False
        while not complete:
            try:
                for i in enumerate(options):
                    print i[0] + 1, ":", i[1]
                option = raw_input("Input your option number: ").strip().lower()
                if option == "q":
                    sys.exit(0)
                user_input = int(option) - 1
                complete = True
            except SystemExit:
                sys.exit(0)
            except:
                pass

        if self.heat1 > 0 and not self.switch1:
            self.heat1 -= 1
        elif self.switch1:
            self.heat1 += 1
        if self.heat2 > 0 and not self.switch2:
            self.heat2 -= 1
        elif self.switch2:
            self.heat2 += 1
        if self.heat3 > 0 and not self.switch3:
            self.heat3 -= 1
        elif self.switch3:
            self.heat3 += 1
        return user_input

    def cellar(self):
        print "--------------------------------------"
        print "You are in the cellar. There are three switches on the wall."

        if self.switch1:
            print "The left switch is in the `on` position"
        else:
            print "the left switch is in the `off` position"

        if self.switch2:
            print "The middle switch is in the `on` position"
        else:
            print "the middle switch is in the `off` position"

        if self.switch3:
            print "The right switch is in the `on` position"
        else:
            print "the right switch is in the `off` position"

        print "--------------------------------------"

        option = self.get_option([
                "Walk upstairs",
                "Press the left switch",
                "Press the middle switch",
                "Press the right switch",
                "Wait",
            ])

        if option == 1:
            self.switch1 = not self.switch1
        elif option == 2:
            self.switch2 = not self.switch2
        elif option == 3:
            self.switch3 = not self.switch3
        elif option == 4:
            print "--------------------------------------"
            print "You wait for a bit..."
            print "--------------------------------------"
        elif option == 0:
            return self.room()
        self.cellar()

    def get_bulb_state(self, s):
        if self.switch1_name == s:
            return self.switch1
        elif self.switch2_name == s:
            return self.switch2
        else:
            return self.switch3

    def get_bulb_heat(self, s):
        if self.switch1_name == s:
            return self.heat1
        elif self.switch2_name == s:
            return self.heat2
        else:
            return self.heat3    

    def room(self):
        print "--------------------------------------"
        print "As you walk up the stairs, they collapse behind you."
        num_lights = self.switch1 + self.switch2 + self.switch3

        if num_lights == 0:
            print "You are in a dark room."
        elif num_lights == 1:
            print "You are in a dimly lit room."
        elif num_lights == 2:
            print "You are in a room."
        else:
            print "You are in a brightly lit room."

        if self.get_bulb_state("left"):
            print "The left bulb is shining brightly"
        else:
            print "the left bulb is off"

        if self.get_bulb_state("middle"):
            print "The middle bulb is shining brightly"
        else:
            print "the middle bulb is off"

        if self.get_bulb_state("right"):
            print "The right bulb is shining brightly"
        else:
            print "the right bulb is off"

        print "--------------------------------------"

        option = self.get_option([
                "Walk downstairs",
                "Touch left bulb",
                "Touch middle bulb",
                "Touch right bulb",
                "Wait",
                "Exit door"
            ])

        if option == 0:
            return self.die()
        if option == 1:
            self.touch_1()
        if option == 2:
            self.touch_2()
        if option == 3:
            self.touch_3()
        elif option == 4:
            print "--------------------------------------"
            print "You wait for a bit..."
            print "--------------------------------------"
        if option == 5:
            self.exit_door()
        self.room()

    def die(self):
        print "You fall to your death. GAME OVER"
        sys.exit(0)

    def touch_1(self):
        print "--------------------------------------"
        heat = self.get_bulb_heat("left")
        if heat > HOT:
            print "Oww! The bulb burns your hand"
        elif heat > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"
        print "--------------------------------------"

    def touch_2(self):
        print "--------------------------------------"
        heat = self.get_bulb_heat("middle")
        if heat > HOT:
            print "Oww! The bulb burns your hand"
        elif heat > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"
        print "--------------------------------------"

    def touch_3(self):
        print "--------------------------------------"
        heat = self.get_bulb_heat("right")
        if heat > HOT:
            print "Oww! The bulb burns your hand"
        elif heat > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"
        print "--------------------------------------"

    def exit_door(self):
        print "You walk out the door into the brightly lit living room."
        print "'You've been in there a long time' calls your wife"
        print "'Did you figure out what order the light switches are in yet?'"
        print "'Yes' you respond"
        print "The left switch is for the...."

        bulb_name_map = {
            0: "left",
            1: "middle",
            2: "right"
        }

        a1 = self.get_option(["The left bulb", "The middle bulb", "The right bulb"])
        answer1_name = bulb_name_map[a1]

        print "The middle switch is for the...."

        a2 = self.get_option(["The left bulb", "The middle bulb", "The right bulb"])
        answer2_name = bulb_name_map[a2]

        print "The right switch is for the...."

        a3 = self.get_option(["The left bulb", "The middle bulb", "The right bulb"])
        answer3_name = bulb_name_map[a3]

        if answer1_name == self.switch1_name and answer2_name == self.switch2_name and answer3_name == self.switch3_name:
            print "You were correct. Your wife is very happy. YOU WIN"
        else:
            print "That was wrong. Your wife took your advice, and ended up falling down the stairs in the dark. I think that means you lose"
        sys.exit(0)

    def start(self):
        options = ["left", "middle", "right"]
        random.shuffle(options)

        self.switch1_name = options.pop()
        self.switch2_name = options.pop()
        self.switch3_name = options.pop()

        print "Welcome to our adventure."
        self.cellar()

game = Game()
game.start()