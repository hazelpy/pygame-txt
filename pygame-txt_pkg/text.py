import pygame

try:
    pygame.ftfont.init()
except:
    pygame.font.init()

scr = pygame.display.set_mode((1080, 720))

class Text:
    allfonts = pygame.font.get_fonts()

    ### Initialization
    def __init__(self, debug: bool = False):
        ### Developer Debug
        self.debug = debug

        ### Text and Position
        self.text = [""]
        self.position = (0, 0)

        ### Style Settings
        self.bold = False
        self.italic = False

        ### Fonts
        self.font_size = 12
        self.font_name = "arial"
        self.font = pygame.font.SysFont(self.font_name, self.font_size, False, False)

    ### Simple Styling
    def styles(self, bold: bool = False, italics: bool = False):
        self.bold = bold
        self.italics = italics

        if self.debug: print("Set styles of text object")
        self.update()

    ### Simple Font Config
    def setfont(self, font_size: int = 12, font_name: str = "arial"):
        self.font_size = font_size
        self.font_name = font_name
        self.font = pygame.font.SysFont(self.font_name, self.font_size, self.bold, self.italic)

        if self.debug: print("Set font settings of text object")

    ### Updating Style Config
    def update(self):
        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)

        if self.debug: print("Updated style information of font")

    ### Generate Text Surface
    def render(self):
        final_text = ""

        for txt in self.text:
            final_text += txt

        return self.font.render(final_text, True, (0, 0, 0))

    ### Render Multiple Lines
    def renders(self):
        rendered_list = []

        for txt in self.text:
            rendered_list.append(self.font.render(txt, True, (0, 0, 0)))

        return rendered_list

    ### Set text by escaped newlines in strings or by list
    def set_text(self, text: list or str = [""]):
        if type(text) == str:
            self.text = [a for a in text.split("\n")]
        else:
            self.text = text

        if self.debug: print("Set text of text object to", self.text)

    ### Add a new line (Or if you're using blitext(), just concatenate text)
    def add_text(self, text: str):
        self.text.append(text)

    ### Blit multiple lines
    def blitexts(self, scr: pygame.Surface):
        rdr = self.renders()
        for surf in range(len(rdr)):
            scr.blit(rdr[surf], (self.position[0], self.position[1] + (surf * self.font_size)))

    ### Blit all text on one line
    def blitext(self, scr: pygame.Surface):
        rdr = self.render()
        scr.blit(rdr, self.position)
