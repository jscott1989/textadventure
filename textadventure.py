import sys

FULL_HEAT = 5
HOT = 4
WARM = 2

class Game(object):
    switch1 = False
    switch2 = False
    switch3 = False

    heat1 = 0
    heat2 = 0
    heat3 = 0

    def get_option2(self, options):
        complete = False
        while not complete:
            sys.stdout.write("> ")
            command = raw_input()
            for key,value in options.iteritems():
                if command == key:
                    value()
                    complete = True
        
        if self.heat1 > 0:
            self.heat1 += 1
        if self.heat2 > 0:
            self.heat2 += 1
        if self.heat3 > 0:
            self.heat3 += 1

    # def get_option(self, options):
    #     complete = False
    #     while not complete:
    #         try:
    #             print "-----------------------"
    #             for i in enumerate(options):
    #                 print i[0] + 1, ":", i[1]
    #             option = raw_input("Input your option number: ").strip().lower()
    #             if option == "q":
    #                 sys.exit(0)
    #             user_input = int(option) - 1
    #             complete = True
    #         except SystemExit:
    #             sys.exit(0)
    #         except:
    #             pass

    #     if self.heat1 > 0:
    #         self.heat1 += 1
    #     if self.heat2 > 0:
    #         self.heat2 += 1
    #     if self.heat3 > 0:
    #         self.heat3 += 1
    #     return user_input

    def cellar(self):
        print "You are in the cellar. There are three switches on the wall."

        if self.switch1:
            print "The left switch is in the `on` position"
        else:
            print "the left switch his in the `off` position"

        if self.switch2:
            print "The middle switch is in the `on` position"
        else:
            print "the middle switch his in the `off` position"

        if self.switch3:
            print "The right switch is in the `on` position"
        else:
            print "the right switch his in the `off` position"

        self.get_option2({
            "walk upstairs": self.room,
            "touch left": self.press1,
            "touch middle": self.press2,
            "touch right": self.press3,
            "q": sys.exit,
            })

        # option = self.get_option([
        #         "Walk upstairs",
        #         "Press the left switch",
        #         "Press the middle switch",
        #         "Press the right switch",
        #     ])

        # if option == 1:
        #     self.switch1 = not self.switch1
        #     if self.switch1:
        #         self.heat1 = FULL_HEAT
        # elif option == 2:
        #     self.switch2 = not self.switch2
        #     if self.switch2:
        #         self.heat2 = FULL_HEAT
        # elif option == 3:
        #     self.switch3 = not self.switch3
        #     if self.switch3:
        #         self.heat3 = FULL_HEAT
        # elif option == 0:
        #     return self.room()
        self.cellar()

    def press1(self):
        self.switch1 = not self.switch1
        if self.switch1:
            self.heat1 = FULL_HEAT
    def press2(self):
        self.switch2 = not self.switch2
        if self.switch2:
            self.heat2 = FULL_HEAT
    def press3(self):
        self.switch3 = not self.switch3
        if self.switch3:
            self.heat3 = FULL_HEAT

    def room(self):
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

        if self.switch1:
            print "The left bulb is shining brightly"
        else:
            print "the left bulb is off"

        if self.switch2:
            print "The middle bulb is shining brightly"
        else:
            print "the middle bulb is off"

        if self.switch3:
            print "The right bulb is shining brightly"
        else:
            print "the right bulb is off"

        self.get_option2({
            "walk downstairs": self.die,
            "touch left": self.touch_1,
            "touch middle": self.touch_2,
            "touch right": self.touch_3,
            "exit": self.exit_door,
            "q": sys.exit,
        })

        # option = self.get_option([
        #         "Walk downstairs",
        #         "Touch left bulb",
        #         "Touch middle bulb",
        #         "Touch right bulb",
        #         "Exit door"
        #     ])

        # if option == 0:
        #     return self.die()
        # if option == 1:
        #     self.touch_1()
        # if option == 2:
        #     self.touch_2()
        # if option == 3:
        #     self.touch_3()
        # if option == 4:
        #     self.exit_door()
        self.room()

    def die(self):
        print "You fall to your death. GAME OVER"
        sys.exit(0)

    def touch_1(self):
        if self.heat1 > HOT:
            print "Oww! The bulb burns your hand"
        elif self.heat1 > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"

    def touch_2(self):
        if self.heat2 > HOT:
            print "Oww! The bulb burns your hand"
        elif self.heat2 > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"

    def touch_3(self):
        if self.heat3 > HOT:
            print "Oww! The bulb burns your hand"
        elif self.heat3 > WARM:
            print  "The bulb is warm to the touch"
        else:
            print "The bulb is cold"

    def exit_door(self):
        print "This is where you need to enter the answer...."

    def start(self):
        print "Welcome to our adventure."
        self.cellar()

game = Game()
game.start()