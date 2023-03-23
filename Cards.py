#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from dataclasses import dataclass, field

@dataclass(init=True, repr=True)
class Card:
    card_kind: str

    card_height: int
    card_width: int

    def base_card(self):
        base_string = '<svg width="{}" height="{}">\n {}\n {}\n</svg>'
        return base_string.format(self.card_width, self.card_height)

@dataclass(init=True, repr=True)
class TechDeck_Card(Card):
    text_to_write: str = field(default='', init=True)

    card_kind: str = field(default='TechDeck_Card', init=True)

    fsty_title: str = field(default='Pixelmix', init=True)
    fsiz_title: str = field(default=60, init=True)

    fsty_algorithm: str = field(default='Pixelmix', init=True)
    fsiz_algorithm: str = field(default=20, init=True)

    mxt_height: int = field(default=795, init=True)
    mxt_length: int = field(default=36, init=True)

    card_height: int = field(default=899, init=True)
    card_width: int = field(default=659, init=True)

    height_inc: int = field(default=20, init=True)
    width_inc: int = field(default=30, init=True)

    con_color_card: list = field(default=[192, 192, 192], init=True)
    con_color_text: list = field(default=[0, 0, 0, 0.5], init=True)

    def generate_style_text(self):
        stlf_title = "\t\t\t.st1{\tfont-family:'{}';\n\t\t\t\tfont-size:{}px;\n\t\t\t\tfill:rgb(0,0,0);\n\t\t\t}"
        stlf_title = stlf_title.format( self.fsty_title, 
                                        self.fsiz_title)  

        stlf_algorithm = "\t\t\t.st2{\tfont-family:'{}';\n\t\t\t\tfont-size:{}px;\n\t\t\t\tfill:rgb(0,0,0);\n\t\t\t}"
        stlf_algorithm = stlf_algorithm.format(self.fsty_algorithm, self.fsiz_algorithm) 

        return '\t\t<style type="text/css">\n {}\n\n {} \n\t\t</style>'.format(stlf_title, stlf_algorithm)

    def generate_style_cont(self):
        style_card_container    = "\t\t\t#cardContainer{\n\t\t\t\tfill:rgb({}, {}, {});\n\t\t\t\tstroke:black;\n\t\t\t\tstroke-width:30;\n\t\t\t}".format(self.con_color_card[0],
                self.con_color_card[1], self.con_color_card[2])

        style_text_container    = "\t\t\t#textContainer{\n\t\t\t\tfill:rgb({}, {}, {});\n\t\t\t\topacity:{};\n\t\t\t}".format(self.con_color_text[0],
                self.con_color_text[1], self.con_color_text[2], self.con_color_text[3])

        return '\t\t<style>\n {}\n\n {} \n\t\t</style>'.format(style_card_container, style_text_container)

    def generate_def_block(self):
        style_text = self.generate_style_text()
        style_cont = self.generate_style_cont()

        return "\t<defs> \n {}\n{} \n\t</defs>".format(style_text, style_cont)

    def generate_cont_block(self):
        card_container          = '\t<rect x="15" y="15" rx="20" ry="20" width="630" height="870" id="cardContainer"/>'
        title_container         = '\t<rect x="60" y="60" rx="30" ry="30" width="540" height="160" id="textContainer"/>'
        algorithm_container     = '\t<rect x="60" y="280" rx="30" ry="30" width="540" height="530" id="textContainer"/>'

        return '{}\n {}\n {}\n'.format(card_container, title_container, algorithm_container)

    def return_card_svg(self):
        base_card = self.base_card()

        definitions_block = self.generate_def_block()
        containers_block = self.generate_cont_block()
        
        return base_card.format('{} \n {}'.format(definitions_block, containers_block)).format(self.text_to_write)



@dataclass(init=True, repr=True)
class Against_Card(Card):
    text_to_write: str = field(default='', init=True)

    card_kind: str = field(default='Against_Card', init=True)

    font_color: list = field(default=[0,0,0], init=True)
    fsty_title: str = field(default='IBM Plex Mono', init=True)
    fsiz_title: str = field(default=30, init=True)

    font_style_text: str = field(default='IBM Plex Mono', init=True)
    font_size_text: str = field(default=20, init=True)

    mxt_height: int = field(default=795, init=True)
    mxt_length: int = field(default=36, init=True)
        
    card_size: int = field(default=481, init=True)

    height_inc: int = field(default=20, init=True)
    width_inc: int = field(default=30, init=True)
  
    con_color_text: list = field(default=[255, 255, 255, 0], init=True)

    logo_route: str = field(default='{}/logo.png'.format('./graphics/logo/monito_logo.PNG'), init=True)
    logo_height: int = field(default=50, init=True)
    logo_width: int = field(default=50, init=True)
    logo_x: int = field(default=290, init=True)
    logo_y:int = field(default=421, init=True)

    logo_text: str = field(default='Les Monkes', init=True)
    logo_text_x: int = field(default=350, init=True)
    logo_text_y: int = field(default=461, init=True)

    def __post_init__(self):
        object.__setattr__(self, 'card_height', self.card_size )
        object.__setattr__(self, 'card_width', self.card_size )

    def generate_style_text(self):
        style_font_title = "\t\t\t.st1{\tfont-family:'{}';\n\t\t\t\tfont-size:{}px;\n\t\t\t\tfill:rgb({},{},{});\n\t\t\t}".format(self.fsty_title, self.fsiz_title,
            self.font_color[0], self.font_color[1],self.font_color[2]) 
        style_font_text = "\t\t\t.st2{\tfont-family:'{}';\n\t\t\t\tfont-size:{}px;\n\t\t\t\tfill:rgb({},{},{});\n\t\t\t}".format(self.fsty_algorithm, self.font_size_text,
            self.font_color[0], self.font_color[1],self.font_color[2]) 

        return '\t\t<style type="text/css">\n {}\n\n {} \n\t\t</style>'.format(style_font_title, style_font_text)

    def generate_style_cont(self):
        style_text_container    = "\t\t\t#textContainer{\n\t\t\t\tfill:rgb({}, {}, {});\n\t\t\t\topacity:{};\n\t\t\t}".format(self.con_color_text[0],
                self.con_color_text[1], self.con_color_text[2], self.con_color_text[3])

        return '\t\t<style>\n {}\n\t\t</style>'.format(style_text_container)

    def generate_def_block(self):
        style_text = self.generate_style_text()
        style_cont = self.generate_style_cont()

        return "\t<defs> \n {}\n{} \n\t</defs>".format(style_text, style_cont)

    def generate_cont_block(self):
        return '\t<rect x="0" y="0" width="481" height="481" id="textContainer"/>\n'

    def generate_logo_block(self):
        return '\t<image xlink:href="{}" height="{}" width="{}" x="{}" y="{}"/>\n\t<text x="{}" y="{}" class="st2">{}</text>\n'.format(self.logo_route,
            self.logo_height, self.logo_width, self.logo_x, self.logo_y, self.logo_text, self.logo_text_x, self.logo_text_y)

    def return_card_svg(self):
        base_card = self.base_card()

        definitions_block = self.generate_def_block()
        containers_block = self.generate_cont_block()
        logo_container = self.generate_logo_block()

        return base_card.format('{}\n{}\n{}'.format(definitions_block, 
                                                    containers_block, 
                                                    logo_container)).format(self.text_to_write)


class CardElements(Enum):
    TechDeck = {'list_kind_algorithm': ['if', 'else', 'else if', 'switch', 'None'],
                'list_kind_operations': ['Monovalue operation', 'Multivalue operation', 'Logic operation'],
                'list_arit_operations': ['+', '-', '/', '%', '*'],
                'list_arit_monators': ['+=', '-=', '*=', '/=', '='],
                'list_logic_operations': ['&lt;', '&gt;', '&lt;=', '&gt;=', '==', '!='],
                'list_condition_linkers':['&amp;&amp;', '||'],
                'list_parenthesis': ['()', 'Nope'],
                'list_variables': ['victory', 'position', 'None']
    }

    Against = {'route_csv_file':'resources/against_cards.csv'
    }