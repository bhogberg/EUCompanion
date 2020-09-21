# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:41:21 2020

@author: bjohog
"""
import eutables
import math

class euhandler():
    def __init__(self):
        self.tables = eutables.eutables()
        # Below are lists of:
        # [inf,cav,art,fortress cv,fortress lvl,transports, galleys, warships, morale]
        self.attacker = dict([('inf',0),('cav',0),('art',0),('pac',0),
                        ('trs',0),('gal',0),('war',0),
                        ('morale',0),('ltech','MED'),('ntech','GA'),('roll',0)])
        self.defender = dict([('inf',0),('cav',0),('art',0),('pac',0),
                        ('trs',0),('gal',0),('war',0),
                        ('morale',0),('ltech','MED'),('ntech','GA'),('frt_cv',0),('frt_lvl',0),
                        ('roll',0)])
        self.assault = False
        self.attacker_pursuing = False
        self.defender_pursuing = False
        self.type_of_combat = 'fire'
        self.terrain = 'clear'
        self.breach = 'False'
        self.results = dict([
                ('tblatt','na'),('tbldef','na'),
                ('attstr',0),('defstr',0),
                ('attresult',0),('defresult',0),
                ('ainflict',0),('dinflict',0),
                ('ainflictmorale',0),('dinflictmorale',0),
                ('tblatt_n', 'na'), ('tbldef_n', 'na'),
                ('attstr_n', 0), ('defstr_n', 0),
                ('attresult_n', 0), ('defresult_n', 0),
                ('ainflict_n', 0), ('dinflict_n', 0),
                ('ainflictmorale_n', 0), ('dinflictmorale_n', 0),
                ('attwindgauge', 'na'), ('defwindgauge', 'na')
                ])
    
        
    def deffortstr(self):
        power = 0
        if self.type_of_combat == 'fire':
            if self.defender['ltech']=='MED':
                power = 0
            elif self.defender['ltech']=='REN':
                power = self.defender['frt_lvl']
            elif self.defender['ltech']=='ARQ':
                power = self.defender['frt_cv']/2.0
            else:
                power = self.defender['frt_cv']
        else:
            #assumes 'shock'
            power = self.defender['frt_cv']
        if self.breach:
            power = round(power/4.0)
        return power
        
    def updateall(self):
        ph = self.type_of_combat
        #
        #       First land combats:
        #
        ln = 'land'
        if self.terrain == 'mountain':
            artmodatt = 0.5
            artmoddef = 1.0
            cavmod = 0.5
        elif self.terrain == 'forest' or self.terrain == 'marsh':
            artmodatt = 0.5
            artmoddef = 0.5
            cavmod = 0.5
        else:
            artmodatt = 1.0
            artmoddef = 1.0
            cavmod = 1.0
        if self.assault:
            #No str modifications due to terrain in assault
            artmodatt = 1.0
            artmoddef = 1.0
            cavmod = 0
        at = self.attacker['ltech']
        self.results['attstr'] = (self.attacker['inf'] * self.tables.getstr('inf',at,ph) +
                                  cavmod * self.attacker['cav'] * self.tables.getstr('cav',at,ph) +
                                  artmodatt * self.attacker['art'] * self.tables.getstr('art',at,ph) +
                                  cavmod * self.attacker['pac'] * self.tables.getstr('pac',at,ph))

        dt = self.defender['ltech']
        self.results['defstr'] = (self.defender['inf']*self.tables.getstr('inf',dt,ph) +
                                  cavmod*self.defender['cav']*self.tables.getstr('cav',dt,ph) +
                                  artmoddef*self.defender['art']*self.tables.getstr('art',dt,ph) +
                                  cavmod*self.defender['pac']*self.tables.getstr('pac',dt,ph))
        if self.assault:
            self.results['defstr'] += self.deffortstr()

        self.results['tblatt'] = self.tables.gettables(ln,ph,at,dt)
        self.results['tbldef'] = self.tables.gettables(ln,ph,dt,at)
        if self.assault:
            self.results['tblatt'] = self.tables.gettables(ln,ph,at,dt,False,True,True)
            self.results['tbldef'] = self.tables.gettables(ln,ph,dt,at,False,True,False)
        if self.attacker_pursuing:
            self.results['tblatt'] = self.tables.gettables(ln,ph,at,dt,True)
        if self.defender_pursuing:
            self.results['tbldef'] = self.tables.gettables(ln,ph,dt,at,True)
        [self.results['attresult'], self.results['ainflictmorale']]=self.tables.getresult(self.results['tblatt'],self.attacker['roll'])
        [self.results['defresult'], self.results['dinflictmorale']]=self.tables.getresult(self.results['tbldef'],self.defender['roll'])
        self.results['ainflict'] = math.ceil(0.01*self.results['attresult']*self.results['attstr'])
        self.results['dinflict'] = math.ceil(0.01*self.results['defresult']*self.results['defstr'])
        #
        #      Then naval combats:
        #
        at = self.attacker['ntech']
        dt = self.defender['ntech']
        self.results['attstr_n'] = (self.attacker['trs'] * self.tables.getstr_nav('trs', ph) +
                                  self.attacker['gal'] * self.tables.getstr_nav('gal', ph) +
                                  self.attacker['war'] * self.tables.getstr_nav('war', ph))
        self.results['defstr_n'] = (self.defender['trs'] * self.tables.getstr_nav('trs', ph) +
                                   self.defender['gal'] * self.tables.getstr_nav('gal', ph) +
                                   self.defender['war'] * self.tables.getstr_nav('war', ph))
        nv = 'naval'
        self.results['tblatt_n'] = self.tables.gettables(nv, ph, at, dt)
        self.results['tbldef_n'] = self.tables.gettables(nv, ph, dt, at)
        if self.attacker_pursuing:
            self.results['tblatt_n'] = self.tables.gettables(nv, ph, at, dt, True)
        if self.defender_pursuing:
            self.results['tbldef_n'] = self.tables.gettables(nv, ph, dt, at, True)
        [self.results['attresult_n'], self.results['ainflictmorale_n']] = self.tables.getresult(self.results['tblatt_n'],
                                                                                            self.attacker['roll'])
        [self.results['defresult_n'], self.results['dinflictmorale_n']] = self.tables.getresult(self.results['tbldef_n'],
                                                                                            self.defender['roll'])
        self.results['ainflict_n'] = math.ceil(0.01 * self.results['attresult_n'] * self.results['attstr_n'])
        self.results['dinflict_n'] = math.ceil(0.01 * self.results['defresult_n'] * self.results['defstr_n'])
        self.results['attwindgauge'] = self.tables.getwindgauge(at,dt)
        self.results['defwindgauge'] = self.tables.getwindgauge(dt,at)

    def fancyprint(self):
        if self.assault:
            print('This is an assault, {0} phase'.format(self.type_of_combat))
        elif self.attacker_pursuing or self.defender_pursuing:
            if self.attacker_pursuing:
                print('The attacker is pursuing')
            else:
                print('The defender is pursuing')
        else:
            print('This is a normal {0} combat, {1} phase, in {2}'.format('land',self.type_of_combat,self.terrain))
        print('Attacker {0} inf, {1} cav, {2} art and {3} pasha'.format(self.attacker['inf'], self.attacker['cav'],
                                                                        self.attacker['art'], self.attacker['pac']))
        print('Attacker ({6}) total strenght {0}, rolls a {1} on the {2} table for {3}%,-{4} morale, inflicting {5} losses'.format(
                self.results['attstr'],self.attacker['roll'],self.results['tblatt'],
                self.results['attresult'],self.results['ainflictmorale'],self.results['ainflict'],self.attacker['ltech']))
        print('Defender ({6}) total strenght {0}, rolls a {1} on the {2} table for {3}%,-{4} morale, inflicting {5} losses'.format(
                self.results['defstr'],self.defender['roll'],self.results['tbldef'],
                self.results['defresult'],self.results['dinflictmorale'],self.results['dinflict'],self.defender['ltech']))

