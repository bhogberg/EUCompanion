# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:19:18 2020

@author: bjohog
"""


class eutables():
    def __init__(self):
        self.combattable = dict([
            ('A',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [5, 0],
              [10, 0],
              [20, 1],
              [25, 1],
              [30, 1],
              [40, 2],
              [50, 3],
              [60, 3],
              [70, 3],
              [80, 4],
              [90, 4]
              ]),
            ('B',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [5, 0],
              [10, 0],
              [15, 0],
              [20, 1],
              [25, 1],
              [30, 2],
              [40, 3],
              [50, 3],
              [60, 3],
              [70, 3],
              [80, 4]
              ]),
            ('C',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0],
              [5, 0],
              [10, 0],
              [15, 1],
              [20, 1],
              [25, 2],
              [30, 3],
              [40, 3],
              [50, 3],
              [60, 3],
              [70, 4]
              ]),
            ('D',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0],
              [5, 0],
              [10, 0],
              [15, 0],
              [20, 0],
              [20, 1],
              [25, 1],
              [30, 2],
              [40, 2],
              [50, 3],
              [60, 3]
              ]),
            ('E',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0],
              [5, 0],
              [10, 0],
              [10, 0],
              [15, 0],
              [20, 0],
              [25, 0],
              [30, 1],
              [30, 2],
              [40, 2],
              [50, 3]
              ]),
            ('F',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [5, 0],
              [10, 1],
              [20, 2],
              [25, 3],
              [30, 3],
              [40, 3],
              [50, 4],
              [60, 4],
              [70, 4],
              [80, 4],
              [90, 4]
              ]),
            ('G',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [5, 0],
              [10, 0],
              [15, 1],
              [20, 2],
              [25, 2],
              [30, 3],
              [40, 3],
              [50, 4],
              [60, 4],
              [70, 4],
              [80, 4]
              ]),
            ('H',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [5, 0],
              [5, 0],
              [10, 1],
              [15, 1],
              [20, 2],
              [25, 2],
              [30, 3],
              [40, 3],
              [50, 4],
              [60, 4],
              [70, 4]
              ]),
            ('I',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0],
              [5, 0],
              [10, 0],
              [15, 0],
              [20, 1],
              [20, 1],
              [25, 2],
              [30, 2],
              [40, 3],
              [50, 3],
              [60, 4]
              ]),
            ('J',
             [[0, 0], [0, 0], [0, 0], [0, 0],
              [0, 0],
              [5, 0],
              [10, 0],
              [10, 0],
              [20, 0],
              [20, 0],
              [25, 1],
              [30, 1],
              [40, 2],
              [50, 2],
              [50, 3]
              ])])
        self.landtech = dict([
            ('MED', 0),
            ('REN', 1),
            ('ARQ', 2),
            ('MOU', 3),
            ('BAR', 4),
            ('MAN', 5),
            ('DEN', 6)
        ])

        self.landfire = [['na', 'na', 'na', 'na', 'na', 'na', 'na'],
                         ['C', 'C', 'C', 'D', 'E', 'E', 'E'],
                         ['B', 'B', 'C', 'D', 'E', 'E', 'E'],
                         ['A', 'B', 'B', 'C', 'D', 'E', 'E'],
                         ['A', 'B', 'B', 'B', 'B', 'D', 'D'],
                         ['A', 'A', 'A', 'B', 'B', 'B', 'C'],
                         ['A', 'A', 'A', 'A', 'A', 'B', 'B']]

        self.landshock = [['H', 'H', 'H', 'H', 'I', 'J', 'J'],
                          ['G', 'G', 'G', 'H', 'I', 'J', 'J'],
                          ['F', 'F', 'F', 'G', 'H', 'I', 'J'],
                          ['F', 'F', 'F', 'F', 'H', 'I', 'J'],
                          ['F', 'F', 'F', 'F', 'F', 'G', 'H'],
                          ['F', 'F', 'F', 'F', 'F', 'F', 'G'],
                          ['F', 'F', 'F', 'F', 'F', 'F', 'F']]

        self.attacker_assault_fire = [
            ['na', 'na', 'na', 'na', 'na', 'na', 'na'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D'],
            ['B', 'C', 'D', 'D', 'D', 'D', 'D']]
        self.defender_assault_fire = [
            ['na', 'na', 'na', 'na', 'na', 'na', 'na'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A', 'A', 'A']]
        self.attacker_assault_shock = [
            ['B', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C'],
            ['A', 'B', 'C', 'C', 'C', 'C', 'C']]

        self.firestr = dict([
            ('inf', [0, 0, 0.5, 1, 1, 1, 1]),
            ('cav', [0, 0, 0, 0, 0, 0, 0.5]),
            ('art', [0, 2, 2, 2, 2, 2, 2]),
            ('pac', [0, 0, 0, 0, 0, 0, 0])
        ])

        self.shockstr = dict([
            ('inf', [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),
            ('cav', [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]),
            ('art', [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]),
            ('pac', [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        ])

    def getresult(self, table_column, roll):
        if roll < 0:
            mroll = 0
        elif roll > 14:
            mroll = 14
        else:
            mroll = roll
        if table_column == 'na':
            return [0, 0]
        else:
            return self.combattable[table_column][mroll]

    def getstr(self, type_of_unit, tech, phase):
        if phase == 'fire':
            return self.firestr[type_of_unit][self.landtech[tech]]
        else:
            return self.shockstr[type_of_unit][self.landtech[tech]]

    def gettables(self, land_or_naval, type_of_combat, player_tech, opposing_tech, pursuit=False, assault=False,
                  attacker=False):
        if land_or_naval == 'land':
            if type_of_combat == 'fire':
                if assault:
                    if attacker:
                        return self.attacker_assault_fire[self.landtech[player_tech]][self.landtech[opposing_tech]]
                    else:
                        return self.defender_assault_fire[self.landtech[player_tech]][self.landtech[opposing_tech]]
                else:
                    return self.landfire[self.landtech[player_tech]][self.landtech[opposing_tech]]
            elif type_of_combat == 'shock':
                if assault:
                    if attacker:
                        return self.attacker_assault_shock[self.landtech[player_tech]][self.landtech[opposing_tech]]
                    else:
                        return 'A'
                elif pursuit:
                    return 'E'
                else:
                    return self.landshock[self.landtech[player_tech]][self.landtech[opposing_tech]]
