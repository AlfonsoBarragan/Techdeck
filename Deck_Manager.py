#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import copy
import random
import routes
import Galfgets

from Cards import TechDeck_Card, CardElements, Against_Card
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

from abc import ABC, abstractmethod


class DeckFactory(ABC):

    def generate_deck(self) -> dict:
        """ Returns the list of cards that compound the deck """

    def generate_card(self) -> Card:
        """ Returns a single card generate for the deck """

class TechDeckFactory(DeckFactory):
    def generate_deck(self) -> dict:
        """ Returns the list of cards that compound the deck """
                # UPDATE WITH GALFGETS IN FUTURE 
        #1001
        random_str = lambda n_chars: ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n_chars))

        deck_name = random_str(8)
        deck = {deck_name:{}}
        for i in range(100):
            
            new_card = self.generate_card().return_card_svg()

            deck[deck_name][f'card_{i}'] = copy.deepcopy(new_card)

    def generate_card(self) -> Card:
        """ Returns a single card generate for the deck """
        card_dict = CardElements.TechDeck.value

        algorithm           = random.choice(card_dict['list_kind_algorithm'])
    
        string_title        = ""
        string_description  = ""
        
        if algorithm == 'if':
            string_title += (algorithm)
            string_description += _generate_if_struct(card_dict['list_logic_operations'],
                                                    card_dict['list_variables'], 
                                                    card_dict['list_condition_linkers'], 
                                                    card_dict['list_arit_monators'],
                                                    card_dict['list_kind_operations'], 
                                                    card_dict['list_arit_operations'], 
                                                    card_dict['list_parenthesis'])
            
        
        elif algorithm == 'else if':
            string_title += ("if - " + algorithm)
            
            string_description += _generate_if_else_if_struct(card_dict['list_logic_operations'],
                                                            card_dict['list_variables'], 
                                                            card_dict['list_condition_linkers'], 
                                                            card_dict['list_arit_monators'],
                                                            card_dict['list_kind_operations'], 
                                                            card_dict['list_arit_operations'], 
                                                            card_dict['list_parenthesis'])
            
        elif algorithm == 'else':
            string_title += ("if - " + algorithm)
            string_description += _generate_if_else_struct(card_dict['list_logic_operations'],
                                                        card_dict['list_variables'],
                                                        card_dict['list_condition_linkers'], 
                                                        card_dict['list_arit_monators'],
                                                        card_dict['list_kind_operations'], 
                                                        card_dict['list_arit_operations'], 
                                                        card_dict['list_parenthesis'])
        elif algorithm == 'switch':
            string_title += (algorithm)
            string_description += _generate_switch_case_struct(card_dict['list_logic_operations'],
                                                            card_dict['list_variables'], 
                                                            card_dict['list_condition_linkers'], 
                                                            card_dict['list_arit_monators'],
                                                            card_dict['list_kind_operations'], 
                                                            card_dict['list_arit_operations'], 
                                                            card_dict['list_parenthesis'])
            
        
        elif algorithm == 'None':
            string_title += ("Operation")
            string_description += "{}".format(_generate_operations(card_dict['list_arit_monators'], 
                                                                card_dict['list_variables'], 
                                                                card_dict['list_kind_operations'], 
                                                                card_dict['list_arit_operations'], 
                                                                card_dict['list_parenthesis'],
                                                                card_dict['list_logic_operations'],
                                                                card_dict['list_condition_linkers']))

        title_coord = _calculate_coord(title)
        desc_coord = test_coord_desc
        
        description_lines = description.split("\n")

        text_to_write = ''
        
        text_to_write += '\t<text x="{}" y="{}" class="st1"> {} </text>\n'.format(title_coord[0], title_coord[1],
                                                                            title)
        text_to_write += '\t<text x="{}" y="{}" class="st2"> {} \n'.format(desc_coord[0], desc_coord[1],
                                                                        description_lines[0])
        offset_x = init_offset_x
        offset_y = init_offset_y

        if len(description_lines) > 2:

            for line in description_lines[1:]:
            
                if ('{' in list(description_lines[description_lines.index(line) - 1])) or (len(description_lines[description_lines.index(line) - 1].split("SEMICOLON")) > 1):
                    offset_x += base_card.width_increment
                elif ('}' in list(line)):
                    offset_x -= base_card.width_increment
            
                
                text_to_write += '\t\t<tspan x="{}" y="{}" class="st2"> {} </tspan>\n'.format(desc_coord[0]+offset_x, 
                                                                                desc_coord[1]+offset_y,
                                                                                line.replace('SEMICOLON', ':'))
                if ('break;' in line.split(" ")):
                    offset_x -= base_card.width_increment
                
                offset_y += base_card.height_increment

        text_to_write += "\t</text>\n"

        base_card.text_to_write = text_to_write

        return base_card

    def _generate_if_struct(list_logic_operations,
                        list_variables, list_condition_linkers, list_arit_monators,
                        list_kind_operations, list_arit_operations, list_parenthesis):
        
        string_description = "if({}){{\n{}}}\n".format(generate_condition(list_logic_operations, 
                                                                        list_variables, 
                                                                        list_condition_linkers),
                                                    generate_operations(list_arit_monators, 
                                                                        list_variables, 
                                                                        list_kind_operations, 
                                                                        list_arit_operations, 
                                                                        list_parenthesis,
                                                                        list_logic_operations,
                                                                        list_condition_linkers))

        return string_description

    def _generate_if_else_if_struct(list_logic_operations,
                                list_variables, list_condition_linkers, list_arit_monators,
                                list_kind_operations, list_arit_operations, list_parenthesis):
        
        
        if random.randint(1,3) < 3:
                string_description = "if({}){{\n{}}} else if({}){{\n{}\n}}\n".format(generate_condition(list_logic_operations, 
                                                                                                    list_variables, 
                                                                                                    list_condition_linkers),
                                                                                generate_operations(list_arit_monators, 
                                                                                                    list_variables, 
                                                                                                    list_kind_operations, 
                                                                                                    list_arit_operations, 
                                                                                                    list_parenthesis,
                                                                                                    list_logic_operations,
                                                                                                    list_condition_linkers),
                                                                                generate_condition(list_logic_operations, 
                                                                                                    list_variables, 
                                                                                                    list_condition_linkers),
                                                                                generate_operations(list_arit_monators, 
                                                                                                    list_variables, 
                                                                                                    list_kind_operations, 
                                                                                                    list_arit_operations, 
                                                                                                    list_parenthesis,
                                                                                                    list_logic_operations,
                                                                                                    list_condition_linkers))
        else:
            string_description = "if({}){{\n{}}} else if({}){{\n{}\n}} else {{\n{}\n}}\n".format(generate_condition(list_logic_operations, 
                                                                                                                        list_variables, 
                                                                                                                        list_condition_linkers),
                                                                                                generate_operations(list_arit_monators, 
                                                                                                                        list_variables, 
                                                                                                                        list_kind_operations, 
                                                                                                                        list_arit_operations, 
                                                                                                                        list_parenthesis,
                                                                                                                        list_logic_operations,
                                                                                                                        list_condition_linkers),
                                                                                                generate_condition(list_logic_operations, 
                                                                                                                        list_variables, 
                                                                                                                        list_condition_linkers),
                                                                                                generate_operations(list_arit_monators, 
                                                                                                                        list_variables,
                                                                                                                        list_kind_operations, 
                                                                                                                        list_arit_operations, 
                                                                                                                        list_parenthesis,
                                                                                                                        list_logic_operations,
                                                                                                                        list_condition_linkers),
                                                                                                generate_operations(list_arit_monators, 
                                                                                                                        list_variables, 
                                                                                                                        list_kind_operations, 
                                                                                                                        list_arit_operations, 
                                                                                                                        list_parenthesis,
                                                                                                                        list_logic_operations,
                                                                                                                        list_condition_linkers))
    

        return string_description

    def _generate_if_else_struct(list_logic_operations,
                                list_variables, list_condition_linkers, list_arit_monators,
                                list_kind_operations, list_arit_operations, list_parenthesis):
        
        string_description = "if({}){{\n{}}} else {{\n{}\n}}\n".format(generate_condition(list_logic_operations, 
                                                                                        list_variables, 
                                                                                        list_condition_linkers),
                                                                    generate_operations(list_arit_monators, 
                                                                                        list_variables, 
                                                                                        list_kind_operations, 
                                                                                        list_arit_operations, 
                                                                                        list_parenthesis,
                                                                                        list_logic_operations,
                                                                                        list_condition_linkers),
                                                                    generate_operations(list_arit_monators, 
                                                                                        list_variables, 
                                                                                        list_kind_operations, 
                                                                                        list_arit_operations, 
                                                                                        list_parenthesis,
                                                                                        list_logic_operations,
                                                                                        list_condition_linkers))

        return string_description

    def _generate_switch_case_struct(list_logic_operations,
                                    list_variables, list_condition_linkers, list_arit_monators,
                                    list_kind_operations, list_arit_operations, list_parenthesis):
        
        cases = random.randint(1,3)
        string_switch = ""
        string_cases  = ""
        case          = ""
        
        variable = random.choice(list_variables)
        
        while variable == "None":
            variable = random.choice(list_variables)
        
        if random.randint(1,4) == 4:
            list_of_cases = random.sample(range(0, cases), random.randint(0, cases))
        else:
            list_of_cases = range(0, cases)
            

        for case in list_of_cases:
            string_cases += generate_case_estructure(case, 'case', list_logic_operations,
                                                    list_variables, list_condition_linkers, list_arit_monators,
                                                    list_kind_operations, list_arit_operations, list_parenthesis)
            

        string_cases += generate_case_estructure(case, 'default', list_logic_operations,
                                                list_variables, list_condition_linkers, list_arit_monators,
                                                list_kind_operations, list_arit_operations, list_parenthesis)
            

            
        string_switch += "switch ({}){{\n{}\n}}\n".format(variable, string_cases)
        
        return string_switch

    def _generate_case_estructure(case, kind_of_case, list_logic_operations,
                                list_variables, list_condition_linkers, list_arit_monators,
                                list_kind_operations, list_arit_operations, list_parenthesis):
        
        if random.randint(1,3) == 3:
            kind_conditional = random.randint(1,3)
            if kind_conditional == 1:
                what_are_in_case = generate_if_struct(list_logic_operations,
                                                    list_variables, list_condition_linkers, list_arit_monators,
                                                    list_kind_operations, list_arit_operations, list_parenthesis)

            elif kind_conditional == 2:
                what_are_in_case = generate_if_else_struct(list_logic_operations,
                                                        list_variables, list_condition_linkers, list_arit_monators,
                                                        list_kind_operations, list_arit_operations, list_parenthesis)        
            elif kind_conditional == 3:
                what_are_in_case = generate_if_else_if_struct(list_logic_operations,
                                                            list_variables, list_condition_linkers, list_arit_monators,
                                                            list_kind_operations, list_arit_operations, list_parenthesis)
        else:
            what_are_in_case = generate_operations(list_arit_monators, list_variables, list_kind_operations, 
                                                list_arit_operations, list_parenthesis, list_logic_operations,
                                                list_condition_linkers)
            
        if kind_of_case == 'case':
            string_cases = "case {}SEMICOLON\n{}break;\n".format(case, what_are_in_case)
        else:
            string_cases = "defaultSEMICOLON\n{}break;\n".format(what_are_in_case)
            
        return string_cases
        
    def _generate_condition(list_logic_operations, list_variables, list_condition_linkers):
        conditions = random.randint(1,2)
        string_condition = ""
        
        
        
        for i in range(conditions):
            operator = random.choice(list_logic_operations)
            variable = random.choice(list_variables)
            
            if variable == 'victory':
                condition_number = random.randint(0,4)
            elif variable == 'position':
                condition_number = random.randint(0,5)
            else:
                condition_number = random.randint(0,3)
                
                while variable == 'None':
                    variable = random.choice(list_variables)
            
            if conditions - i > 1:
                linker = random.choice(list_condition_linkers) + "\n"
                
                if conditions - i == conditions:
                    string_condition += "({} {} {}) {}".format(variable, operator, condition_number, linker)
        
                else:
                    string_condition += "({} {} {}) {}".format(variable, operator, condition_number, linker)
                    
            
            else:
                linker = ""
            
                if conditions - i == conditions:
                    string_condition += "({} {} {})".format(variable, operator, condition_number)
        
                else:
                    string_condition += "({} {} {})".format(variable, operator, condition_number)
                    
            
            
        return string_condition

    def _generate_operations(list_arit_monators, list_variables, list_kind_operations, 
                            list_arit_operations, list_parenthesis, list_logic_operations,
                            list_condition_linkers):
        operations = random.randint(1,5)
        string_operation = ""
        
        for i in range(operations):
            kind = random.choice(list_kind_operations)
            
            if kind == 'Monovalue operation':
                operator = random.choice(list_arit_monators)
                variable = random.choice(list_variables)
                number   = random.randint(0,6)
                
                while variable == 'None':
                    variable = random.choice(list_variables)
                
                if number == 6:
                    number = "victory"
                    
                elif number == 0:
                    number = "position"

                string_operation += "{} {} {};\n".format(variable, operator, number)            
            
            elif kind == 'Multivalue operation':

                operator            = random.choice(list_arit_operations)
                variable_to_assign  = random.choice(list_variables)
                variable_to_use     = random.choice(list_variables)
                number              = random.randint(1,7)
                
                while variable_to_assign == 'None':
                    variable_to_assign = random.choice(list_variables)
                
                if variable_to_use == 'None':
                    variable_to_use = 0
                
                if number == 6:
                    number = random.choice(list_variables)
                    
                    while number == 'None':
                        number = random.choice(list_variables)
                        
                elif number == 7:
                    number = generate_compound_operation(list_arit_operations, list_variables, list_parenthesis)
                    
                string_operation += "{} = {} {} {};\n".format(variable_to_assign, variable_to_use, operator, number)            

            elif kind == 'Logic operation':
                variable_to_assign  = random.choice(list_variables)
                
                while variable_to_assign == 'None':
                    variable_to_assign = random.choice(list_variables)
                
                
                condition = generate_condition(list_logic_operations, list_variables, list_condition_linkers)
                string_operation += "{} = {};\n".format(variable_to_assign, condition)            

        return string_operation

    def _generate_compound_operation(list_arit_operations, list_variables, list_parenthesis):
        operations                  = random.randint(1,3)
        string_compound_operation   = ""
        
        for i in range(operations):
            operator            = random.choice(list_arit_operations)
            linker              = random.choice(list_arit_operations)
            with_parenthesis    = random.choice(list_parenthesis)
            variable            = random.choice(list_variables)
            number              = random.randint(1,6)
            number_aux          = random.randint(1,5)
            
            if number == 6:
                number = random.choice(list_variables)
                
                while number == 'None':
                    number = random.choice(list_variables)
                    
            
            if operations - i > 1:
                if with_parenthesis != 'None':
                    if variable != 'None':
                        string_compound_operation += "({} {} {}) {} ".format(variable, operator, number, linker)
                    else:
                        string_compound_operation += "({} {} {}) {} ".format(number_aux, operator, number, linker)
                else:
                    if variable != 'None':
                        string_compound_operation += "{} {} {} {} ".format(variable, operator, number, linker)
                    else:
                        string_compound_operation += "{} {} {} {} ".format(number_aux, operator, number, linker)
            else:
                if with_parenthesis != 'None':
                    if variable != 'None':
                        string_compound_operation += "({} {} {})".format(variable, operator, number)
                    else:
                        string_compound_operation += "({} {} {})".format(number_aux, operator, number)
                else:
                    if variable != 'None':
                        string_compound_operation += "{} {} {}".format(variable, operator, number)
                    else:
                        string_compound_operation += "{} {} {}".format(number_aux, operator, number, linker)
        
        return string_compound_operation

    def _calculate_coord(string_to_insert):

        test_string = "IF"
        test_coord = (290, 170)


        caracteres_test = len(test_string)
        caracteres      = len(string_to_insert)
        
        diff_letters    = caracteres - caracteres_test
        
        coord_x = test_coord[0] - diff_letters * 20
        
        return (coord_x, test_coord[1])



class AgainstDeckFactory(DeckFactory):
    def generate_deck(self) -> dict:
        """ Returns the list of cards that compound the deck """
        # os.system('mkdir {}/{}'.format(routes.deck_folder, deck_name))

        white_cards, black_cards = _read_cards_csv(CardElements.Against.value['route_csv_file'])

        deck = {'white_cards': {},
                'black_cards': {}
            }
        white_card_base = self.generate_card()

        black_card_base = self.generate_card()
        black_card_base.font_color = [255,255,255]
        black_card_base.container_color_text = [0,0,0]

        deck['white_cards'] = svg_converse_group_of_cards(white_cards, white_card_base)
        deck['black_cards'] = svg_converse_group_of_cards(black_cards, black_card_base)

        return deck

    def svg_converse_group_of_cards(cards_collection, base_card):
        card_dict = {}
        for card_ind, card_text in enumerate(cards_collection):
            # file_card = open("{}/{}/card_{}.svg".format(routes.deck_folder, deck_name, cards.index(i)), "w")
            
            lenght_text = len(card_text)
            words_aux = card_text.split(' ')
            
            if (lenght_text >= 12):
                
                words       = card_text.split(' ')
                characters  = 0
                for word in words:
                    if (word == '<'):
                        words[words.index(word)] = 'lt&'
                        
                    characters += len(word)
                    characters += 1
                    if characters >= 12:
                        words_aux[words_aux.index(word)] = "{}\n".format(word)
                        characters = 0
                        
            description = _recreate_phrase(words_aux)
            description_lines = description.split('\n')

            text_to_write = ''
            
            text_to_write +='\t<text x="{}" y="{}" class="st1"> {} \n'.format(desc_coord[0], desc_coord[1],
                                                                            description_lines[0])
            offset_x = init_offset_x
            offset_y = init_offset_y

            if len(description_lines) > 2:
        
                for line in description_lines[1:]:
                
                    text_to_write += '\t\t<tspan x="{}" y="{}" class="st1"> {} </tspan>\n'.format(desc_coord[0]+offset_x, 
                                                                                desc_coord[1]+offset_y,
                                                                                line.replace('SEMICOLON', ':'))
                    offset_y += base_card.height_increment

            text_to_write += ("\t</text>\n")

            svg_card = base_card.return_card_svg()

            card_dict[f'card_{card_ind}'] = copy.deepcopy(svg_card)

        return card_dict

    def generate_card(self) -> Card:
        """ Returns a single card generate for the deck """
        return Against_Card()

    # Against humanity custom deck generation
    def _recreate_phrase(list_words):
        string_phrase = ""
        for word in list_words:
            string_phrase += word
            string_phrase += ' '
        
        return string_phrase

    def _read_cards_csv(route_csv):

        aux = Galfgets.galfgets.read_dataset(route_csv)
        black = list(aux['Cartas negras'].dropna())
        white = list(aux['Cartas blancas '].dropna())
        

        return black, white

