#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:58:49 2020

@author: alfonso
"""

import BaseCard as bc
import routes
import utils
import random
import os

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def create_deck(deck_name, n_cards, base_card, test_title, test_desc,
                base_card_end, list_kind_algorithm, list_logic_operations,
                list_variables, list_condition_linkers, list_arit_monators,
                list_kind_operations, list_arit_operations, list_parenthesis,
                test_coord_title, test_coord_desc):
    
    os.system('mkdir {}/{}'.format(routes.deck_folder, deck_name))
    
    for i in range(n_cards):
        file_card = open("{}/{}/card_{}.svg".format(routes.deck_folder, deck_name, i), "w")
        file_card.write(base_card)
        
        title, description = generate_card(list_kind_algorithm, list_logic_operations, 
                                           list_variables, list_condition_linkers, 
                                           list_arit_monators, list_kind_operations, 
                                           list_arit_operations, list_parenthesis)
        
        title_coord = calculate_coord(title, test_title, test_coord_title)
        desc_coord = test_coord_desc
        
        description_lines = description.split("\n")
        
        file_card.write('\t<text x="{}" y="{}" class="st1"> {} </text>\n'.format(title_coord[0], title_coord[1],
                                                                            title))
        file_card.write('\t<text x="{}" y="{}" class="st2"> {} \n'.format(desc_coord[0], desc_coord[1],
                                                                       description_lines[0]))
        offset_x = 0
        offset_y = 20

        if len(description_lines) > 2:
    
            for line in description_lines[1:]:
            
                if ('{' in list(description_lines[description_lines.index(line) - 1])) or (len(description_lines[description_lines.index(line) - 1].split("SEMICOLON")) > 1):
                    offset_x += 30
                elif ('}' in list(line)):
                    offset_x -= 30
            
                
                file_card.write('\t\t<tspan x="{}" y="{}" class="st2"> {} </tspan>\n'.format(desc_coord[0]+offset_x, 
                                                                               desc_coord[1]+offset_y,
                                                                               line.replace('SEMICOLON', ':')))
                if ('break;' in line.split(" ")):
                    offset_x -= 30
                
                offset_y += 20

        
        file_card.write("\t</text>\n")
        
        file_card.write(base_card_end)
        file_card.close()
        

def calculate_coord(string_to_insert, test_string, test_coord):
    caracteres_test = len(test_string)
    caracteres      = len(string_to_insert)
    
    diff_letters    = caracteres - caracteres_test
    
    coord_x = test_coord[0] - diff_letters * 20
    
    return (coord_x, test_coord[1])

    
def generate_card(list_kind_algorithm, list_logic_operations, list_variables, list_condition_linkers, list_arit_monators, list_kind_operations, list_arit_operations, list_parenthesis):
    algorithm           = random.choice(list_kind_algorithm)
   
    string_title        = ""
    string_description  = ""
    
    if algorithm == 'if':
        string_title += (algorithm)
        string_description += generate_if_struct(list_logic_operations,
                                                 list_variables, list_condition_linkers, list_arit_monators,
                                                 list_kind_operations, list_arit_operations, list_parenthesis)
        
    
    elif algorithm == 'else if':
        string_title += ("if - " + algorithm)
        
        string_description += generate_if_else_if_struct(list_logic_operations,
                                                         list_variables, list_condition_linkers, list_arit_monators,
                                                         list_kind_operations, list_arit_operations, list_parenthesis)
        
    elif algorithm == 'else':
        string_title += ("if - " + algorithm)
        string_description += generate_if_else_struct(list_logic_operations,
                                                      list_variables, list_condition_linkers, list_arit_monators,
                                                      list_kind_operations, list_arit_operations, list_parenthesis)
    elif algorithm == 'switch':
        string_title += (algorithm)
        string_description += generate_switch_case_struct(list_logic_operations,
                                                          list_variables, list_condition_linkers, list_arit_monators,
                                                          list_kind_operations, list_arit_operations, list_parenthesis)
        
    
    elif algorithm == 'None':
        string_title += ("Operation")
        string_description += "{}".format(generate_operations(list_arit_monators, 
                                                              list_variables, 
                                                              list_kind_operations, 
                                                              list_arit_operations, 
                                                              list_parenthesis,
                                                              list_logic_operations,
                                                              list_condition_linkers))

    return string_title, string_description

def generate_if_struct(list_logic_operations,
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

def generate_if_else_if_struct(list_logic_operations,
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

def generate_if_else_struct(list_logic_operations,
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

def generate_switch_case_struct(list_logic_operations,
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

def generate_case_estructure(case, kind_of_case, list_logic_operations,
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
      
def generate_condition(list_logic_operations, list_variables, list_condition_linkers):
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

def generate_operations(list_arit_monators, list_variables, list_kind_operations, 
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

def generate_compound_operation(list_arit_operations, list_variables, list_parenthesis):
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

#### CARD MANAGEMENT ####

def filter_deck(deck_folder, deck_name, init_high_text, max_high, max_length, increment_y_axis):
    cards = utils.ls("{}/{}/".format(deck_folder, deck_name))
    cards_to_remove = []
    
    for card in cards:
        card_file = open("{}/{}/{}".format(deck_folder, deck_name, card), "r")
        line = card_file.readline()
        
        total_height = init_high_text
        
        while line:
            splitted_line = line.split(" ")
            
            if 'class="st2">' in splitted_line:
                aux = line.split('>')[1].split('<')
                aux = aux[0].replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&").replace("\n", "")
                total_height += increment_y_axis
                
                if len(aux) > max_length and card not in cards_to_remove:                    
                    cards_to_remove.append(card)
                    break
                    
                elif total_height > max_high and card not in cards_to_remove:
                    cards_to_remove.append(card)
                    break
                
            line = card_file.readline()
        
        card_file.close()
        
    return cards_to_remove               

def remove_list_of_cards(list_of_cards, deck_folder, deck_name):
    
    for card in list_of_cards:
        os.system('rm {}/{}/{}'.format(deck_folder, deck_name, card))
        utils.printProgressBar(list_of_cards.index(card), len(list_of_cards))

def generate_card_to_print(output_route, input_route, card_width, card_height, list_of_cards, end_svg_file):
    number_of_cards = len(list_of_cards)
    number_of_folds = int(number_of_cards / 9) + 1
    index = 0
    
    for fold in range(number_of_folds):
        file_to_print = open("{}/fold_to_print_{}.svg".format(output_route, fold), "w")
        string_cards = ""
        
        card_offset_x   = 30
        card_offset_y  = 50
        
        cards_to_add = list_of_cards[index:index+9]
        
        for card in cards_to_add:
            card_route = "{}/{}".format(input_route, card)
            
            if cards_to_add.index(card) % 3 == 0 and cards_to_add.index(card) != 0:
                card_offset_y += card_height + 50
                card_offset_x = 30

                
            string_cards += '<image x="{}" y="{}" width="{}" height="{}" xlink:href="{}" />\n'.format(card_offset_x, card_offset_y,
                                                                                                      card_width, card_height, 
                                                                                                      card_route)
            card_offset_x += card_width + 30

            
            
        file_to_print.write('<svg width="2100" height="2970">\n {}\n{}\n'.format(string_cards, end_svg_file))
        
        index += 9
        file_to_print.close()
        
def converse_to_pdf(route_input_folds, route_output_folds):
    
    list_of_folds = utils.ls(route_input_folds)
    
    for fold in list_of_folds:
        os.system("rsvg-convert -f pdf -o {}/{}.pdf {}/{}".format(route_output_folds, fold[:len(fold)-4], route_input_folds, fold))

if __name__ == '__main__':
    # create_deck("Variables_Operaciones", 1000, bc.base_card, 
    #             bc.test_title, bc.test_desc,
    #             bc.base_card_end, bc.list_kind_algorithm, bc.list_logic_operations,
    #             bc.list_variables, bc.list_condition_linkers, bc.list_arit_monators,
    #             bc.list_kind_operations, bc.list_arit_operations, bc.list_parenthesis,
    #             bc.test_coord_title, bc.test_coord_desc)
    
    # list_of_cards = filter_deck(routes.deck_folder, "Variables_Operaciones", bc.init_high_text, 
    #                             bc.max_high_text, bc.max_lenght_text, bc.increment_y_axis)
    
    # remove_list_of_cards(list_of_cards, routes.deck_folder, "Variables_Operaciones")
    # generate_card_to_print("Decks/to_print", "Variables_Operaciones", bc.card_size[0],
    #                        bc.card_size[1], utils.ls("Decks/Variables_Operaciones/"), bc.base_card_end)
    
    converse_to_pdf("Decks/to_print", "Decks/to_print_pdf")
    
    
    
    
    
    
    