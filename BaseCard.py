#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:00:45 2020

@author: alfonso
"""
style_font_title        = "\t\t\t.st1{\tfont-family:'Pixelmix';\n\t\t\t\tfont-size:60px;\n\t\t\t\tfill:rgb(0,0,0);\n\t\t\t}"
style_font_algorithm    = "\t\t\t.st2{\tfont-family:'Pixelmix';\n\t\t\t\tfont-size:20px;\n\t\t\t\tfill:rgb(0,0,0);\n\t\t\t}"
style_text              = '\t\t<style type="text/css">\n {}\n\n {} \n\t\t</style>'.format(style_font_title, style_font_algorithm)

style_card_container    = "\t\t\t#cardContainer{\n\t\t\t\tfill:rgb(192, 192, 192);\n\t\t\t\tstroke:black;\n\t\t\t\tstroke-width:30;\n\t\t\t}"
style_text_container    = "\t\t\t#textContainer{\n\t\t\t\tfill:rgb(0, 0, 0);\n\t\t\t\topacity:0.5;\n\t\t\t}"
style_containers        = '\t\t<style>\n {}\n\n {} \n\t\t</style>'.format(style_card_container, style_text_container)

definitions_block       = "\t<defs> \n {}\n{} \n\t</defs>".format(style_text, style_containers)

card_container          = '\t<rect x="15" y="15" rx="20" ry="20" width="630" height="870" id="cardContainer"/>'
title_container         = '\t<rect x="60" y="60" rx="30" ry="30" width="540" height="160" id="textContainer"/>'
algorithm_container     = '\t<rect x="60" y="280" rx="30" ry="30" width="540" height="530" id="textContainer"/>'

containers_block        = '{}\n {}\n {}\n'.format(card_container, title_container, algorithm_container)

base_card = '<svg width="659" height="899">\n {}\n{}\n'.format(definitions_block, containers_block)
base_card_end = '</svg>'

list_kind_algorithm     = ['if', 'else', 'else if', 'switch', 'None']
#list_kind_algorithm     = ['None']
list_kind_operations    = ['Monovalue operation', 'Multivalue operation', 'Logic operation']
list_arit_operations    = ['+', '-', '/', '%', '*']
list_arit_monators      = ['+=', '-=', '*=', '/=', '=']
list_logic_operations   = ['&lt;', '&gt;', '&lt;=', '&gt;=', '==', '!=']
list_condition_linkers  = ['&amp;&amp;', '||']
list_parenthesis         = ['()', 'Nope']
list_variables          = ['victory', 'position', 'None']

test_title              = "IF"
test_desc               = "if(pos%2 == 0){"

test_coord_title        = (290, 170)
test_coord_desc         = (80, 340)
test_desc_tab           = (40, 40)

init_high_text          = 340
max_lenght_text         = 36
max_high_text           = 795
increment_y_axis        = 20
increment_x_axis        = 30
