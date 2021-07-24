import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 10

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.qx,self.qy = 60,self.game.DISPLAY_H / 2 - 0
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Q', 20, 60, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('W', 20, 100, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('E', 20, 140, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('R', 20, 180, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('T', 20, 220, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('Y', 20, 260, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('U', 20, 300, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('I', 20, 340, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('O', 20, 380, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('P', 20, 420, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('A', 20, 90, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('S', 20, 130, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('D', 20, 170, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('F', 20, 210, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('G', 20, 250, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('H', 20, 290, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('J', 20, 330, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('K', 20, 370, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('L', 20, 410, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('Z', 20, 120, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('X', 20, 160, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('C', 20, 200, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('V', 20, 240, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('B', 20, 280, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('N', 20, 320, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('M', 20, 360, self.game.DISPLAY_H / 2 + 80)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.qx + self.offset, self.qy)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
