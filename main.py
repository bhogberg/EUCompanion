from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
import euhandler
import math

dbug = True

if dbug:
    from kivy.core.window import Window
    Window.size = (360,600)

KV = '''
#:import Clock kivy.clock.Clock
#:include landscreen.kv
#:include navalscreen.kv

Screen:
    
    MDBottomNavigation:
    
        MDBottomNavigationItem:
            name: 'LandScreen'
            text: 'Land'
            icon: 'run'
            
            LandScreen:
                size_hint: (None,None)
                size: (self.parent.width, self.parent.height)
                id: lndscr
     
 
        
        MDBottomNavigationItem:
            name: 'NavalScreen'
            text: 'Naval'
            icon: 'ship-wheel'
            
            NavalScreen:
                size_hint: (None,None)
                size: (self.parent.width, self.parent.height)
                id: navscr
            
                    
'''


class EuApp(MDApp):
    terrainmenu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.eu = euhandler.euhandler()
        self.screen = Builder.load_string(KV)
        self.terrainmenu = MDDropdownMenu(
            caller = self.screen.ids.lndscr.ids.terrainButton,
            items = [{"viewclass" : "MDMenuItem", "text" : "Clear"},
                     {"viewclass" : "MDMenuItem", "text" : "Mount."},
                     {"viewclass" : "MDMenuItem", "text" : "Forest"},
                     {"viewclass" : "MDMenuItem", "text" : "Marsh"}
                     ],
            width_mult=4,
            opening_time = 0
        )
        self.terrainmenu.bind(on_release=self.terrainmenu_item_selected)

        self.attackertechmenu = MDDropdownMenu(
            caller=self.screen.ids.lndscr.ids.attackerTechButton,
            position="bottom",
            items=[{"viewclass": "MDMenuItem", "text": "MED"},
                   {"viewclass": "MDMenuItem", "text": "REN"},
                   {"viewclass": "MDMenuItem", "text": "ARQ"},
                   {"viewclass": "MDMenuItem", "text": "MOU"},
                   {"viewclass": "MDMenuItem", "text": "BAR"},
                   {"viewclass": "MDMenuItem", "text": "MAN"},
                   {"viewclass": "MDMenuItem", "text": "DEN"}
                   ],
            width_mult=3,
            opening_time=0
        )
        self.attackertechmenu.bind(on_release=self.attackertechmenu_item_selected)

        self.defendertechmenu = MDDropdownMenu(
            caller=self.screen.ids.lndscr.ids.defenderTechButton,
            items=[{"viewclass": "MDMenuItem", "text": "MED"},
                   {"viewclass": "MDMenuItem", "text": "REN"},
                   {"viewclass": "MDMenuItem", "text": "ARQ"},
                   {"viewclass": "MDMenuItem", "text": "MOU"},
                   {"viewclass": "MDMenuItem", "text": "BAR"},
                   {"viewclass": "MDMenuItem", "text": "MAN"},
                   {"viewclass": "MDMenuItem", "text": "DEN"}
                   ],
            width_mult=3,
            opening_time=0
        )
        self.defendertechmenu.bind(on_release=self.defendertechmenu_item_selected)

        self.attackernavaltechmenu = MDDropdownMenu(
            caller=self.screen.ids.navscr.ids.attackerNavalTechButton,
            items=[{"viewclass": "MDMenuItem", "text": "GA"},
                   {"viewclass": "MDMenuItem", "text": "CAR"},
                   {"viewclass": "MDMenuItem", "text": "GLN"},
                   {"viewclass": "MDMenuItem", "text": "LS"},
                   {"viewclass": "MDMenuItem", "text": "BA"},
                   {"viewclass": "MDMenuItem", "text": "VE"},
                   {"viewclass": "MDMenuItem", "text": "T-D"}
                   ],
            width_mult=3,
            opening_time=0
        )
        self.attackernavaltechmenu.bind(on_release=self.attackernavaltechmenu_item_selected)

        self.defendernavaltechmenu = MDDropdownMenu(
            caller=self.screen.ids.navscr.ids.defenderNavalTechButton,
            items=[{"viewclass": "MDMenuItem", "text": "GA"},
                   {"viewclass": "MDMenuItem", "text": "CAR"},
                   {"viewclass": "MDMenuItem", "text": "GLN"},
                   {"viewclass": "MDMenuItem", "text": "LS"},
                   {"viewclass": "MDMenuItem", "text": "BA"},
                   {"viewclass": "MDMenuItem", "text": "VE"},
                   {"viewclass": "MDMenuItem", "text": "T-D"}
                   ],
            width_mult=3,
            opening_time=0
        )
        self.defendernavaltechmenu.bind(on_release=self.defendernavaltechmenu_item_selected)


    def terrainmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.lndscr.ids.terrainButton.set_item(instance_menu_item.text)
        terrconv = {'Clear': 'clear', 'Mount.': 'mountain', 'Forest': 'forest', 'Marsh': 'marsh'}
        self.eu.terrain = terrconv[instance_menu_item.text]
        self.update()
        self.terrainmenu.dismiss()

    def attackernavaltechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.navscr.ids.attackerNavalTechButton.set_item(instance_menu_item.text)
        self.eu.attacker['ntech'] = instance_menu_item.text
        self.update()
        self.attackernavaltechmenu.dismiss()

    def defendernavaltechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.navscr.ids.defenderNavalTechButton.set_item(instance_menu_item.text)
        self.eu.defender['ntech'] = instance_menu_item.text
        self.update()
        self.defendernavaltechmenu.dismiss()


    def attackertechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.lndscr.ids.attackerTechButton.set_item(instance_menu_item.text)
        self.eu.attacker['ltech'] = instance_menu_item.text
        self.update()
        self.attackertechmenu.dismiss()

    def defendertechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.lndscr.ids.defenderTechButton.set_item(instance_menu_item.text)
        self.eu.defender['ltech'] = instance_menu_item.text
        self.update()
        self.defendertechmenu.dismiss()

    def roll_slider_change(self, att_or_def,value):
        rounded = math.ceil(value)
        if att_or_def == 'att':
            self.screen.ids.lndscr.ids.att_roll_label.text = str(rounded)
            self.screen.ids.navscr.ids.att_roll_label.text = str(rounded)
            self.eu.attacker['roll'] = rounded
        elif att_or_def == 'def':
            self.screen.ids.lndscr.ids.def_roll_label.text = str(rounded)
            self.screen.ids.navscr.ids.def_roll_label.text = str(rounded)
            self.eu.defender['roll'] = rounded
        self.update()

    def assaultselected(self, instance, value):
        if value:
            self.eu.assault = value
            self.screen.ids.lndscr.ids.defenderPursuing.active = False
            self.screen.ids.lndscr.ids.attackerPursuing.active = False
            if dbug:
                print('Assault is ', value)
        else:
            self.eu.assault = value
            if dbug:
                print('Assault is ', value)
        self.update()

    def defenderpursuingselected(self, instance, value):
        if value:
            self.eu.defender_pursuing = value
            self.screen.ids.lndscr.ids.combatTypeSelector.active = True
            self.screen.ids.lndscr.ids.attackerPursuing.active = False
            self.screen.ids.navscr.ids.combatTypeSelector.active = True
            self.screen.ids.navscr.ids.attackerPursuing.active = False
            self.screen.ids.lndscr.ids.assaultSelector.active = False
            if dbug:
                print('Defender pursuing is ', value)
        else:
            self.eu.defender_pursuing = value
            if dbug:
                print('Defender pursuing is ', value)
        self.update()

    def breachselected(self, instance, value):
        if value:
            self.eu.breach = True
        else:
            self.eu.breach = False
        self.update()

    def attackerpursuingselected(self, instance, value):
        if value:
            self.eu.attacker_pursuing = value
            self.screen.ids.lndscr.ids.combatTypeSelector.active = True
            self.screen.ids.lndscr.ids.defenderPursuing.active = False
            self.screen.ids.navscr.ids.combatTypeSelector.active = True
            self.screen.ids.navscr.ids.defenderPursuing.active = False
            self.screen.ids.lndscr.ids.assaultSelector.active = False
            if dbug:
                print('Attacker pursuing is ', value)
        else:
            self.eu.attacker_pursuing = value
            if dbug:
                print('Attacker pursuing is ', value)
        self.update()

    def combatselected(self, instance, value):
        self.screen.ids.lndscr.ids.combatTypeSelector.active = value
        self.screen.ids.navscr.ids.combatTypeSelector.active = value
        if value:
            self.eu.type_of_combat = 'shock'
            if dbug:
                print('shock phase')
        else:
            self.eu.type_of_combat = 'fire'
            self.screen.ids.lndscr.ids.defenderPursuing.active = False
            self.screen.ids.lndscr.ids.attackerPursuing.active = False
            self.screen.ids.navscr.ids.defenderPursuing.active = False
            self.screen.ids.navscr.ids.attackerPursuing.active = False
            if dbug:
                print('fire phase')
        self.update()

    def textfield_change(self, textfield, att_or_def, unit):
        if textfield.text.isdigit():
            if int(textfield.text)<0:
                textfield.text = '0'
            if dbug:
                print(att_or_def, ' ', textfield.text,' ', textfield.hint_text)
            if att_or_def == 'att':
                self.eu.attacker[unit] = int(textfield.text)
            else:
                self.eu.defender[unit] = int(textfield.text)
        else:
            #Field is not a positive digit set values to 0
            if att_or_def == 'att':
                self.eu.attacker[unit] = 0
            else:
                self.eu.defender[unit] = 0
        self.update()

    def increment(self, buttonInstance, screen, unit, att_or_def):
        #Define the id of the text field that needs to be changed
        textId = 'txt_field_'+unit+'_'+att_or_def
        #Get the current value of the field
        if not self.screen.ids[screen].ids[textId].text.isdigit():
            value = 0
        else:
            value = int(self.screen.ids[screen].ids[textId].text)
        #Read the text of the button to decide how to change
        if buttonInstance.text == '+':
            value += 1
        elif buttonInstance.text == '-':
            value += -1
        elif buttonInstance.text == '+10':
            value += 10
        elif buttonInstance.text == '-10':
            value += -10
        if value < 0:
            value = 0
        self.screen.ids[screen].ids[textId].text = str(value)


    def update(self):
        self.eu.updateall()
        base_string = '{0} pow  table {1}:  [{2}%, -{3}] : cause {4} loss'
        att_string = base_string.format(
            self.eu.results['attstr'], self.eu.results['tblatt'],
            self.eu.results['attresult'], self.eu.results['ainflictmorale'],
            self.eu.results['ainflict']
        )
        self.screen.ids.lndscr.ids['att_results'].text = att_string

        def_string = base_string.format(
            self.eu.results['defstr'], self.eu.results['tbldef'],
            self.eu.results['defresult'], self.eu.results['dinflictmorale'],
            self.eu.results['dinflict']
        )
        self.screen.ids.lndscr.ids['def_results'].text = def_string
        if dbug:
            self.eu.fancyprint()

        att_navstring = base_string.format(
            self.eu.results['attstr_n'], self.eu.results['tblatt_n'],
            self.eu.results['attresult_n'], self.eu.results['ainflictmorale_n'],
            self.eu.results['ainflict_n']
        )
        self.screen.ids.navscr.ids['att_results'].text = att_navstring

        def_navstring = base_string.format(
            self.eu.results['defstr_n'], self.eu.results['tbldef_n'],
            self.eu.results['defresult_n'], self.eu.results['dinflictmorale_n'],
            self.eu.results['dinflict_n']
        )
        self.screen.ids.navscr.ids['def_results'].text = def_navstring

        self.screen.ids.navscr.ids.att_wind_gauge_modifier_text.text = self.eu.results['attwindgauge']
        self.screen.ids.navscr.ids.def_wind_gauge_modifier_text.text = self.eu.results['defwindgauge']


    def get_id(self, instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def build(self):
        return self.screen



if __name__ == "__main__":
    EuApp().run()
