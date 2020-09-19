from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
import euhandler
import math

dbug = False

if dbug:
    from kivy.core.window import Window
    Window.size = (360,600)

KV = '''
#:import Clock kivy.clock.Clock

Screen:
    
    MDBottomNavigation:
    
        MDBottomNavigationItem:
            name: 'LandScreen'
            text: 'Land'
            icon: 'run'
    
            BoxLayout:
                orientation: 'vertical'
                padding: '10dp'
                spacing: 3
                
                BoxLayout: 
                    orientation: 'horizontal'
                    size_hint_max_y: '40dp'
                        
                        
                    MDDropDownItem:
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        id: terrainButton
                        text: 'Clear'
                        font_size: '14sp'
                        on_release: app.terrainmenu.open()
                    
                    FloatLayout:
                        MDLabel:
                            text: 'Fire'
                            pos_hint: {'x': .1, 'center_y': .5}
                            font_style: 'Caption'
                        
                        
                        MDIcon:
                            pos_hint: {'x': 0.25, 'center_y': .5}
                            icon: 'fire'
                        
                        MDSwitch:
                            pos_hint: {'x': .4, 'center_y': .5}
                            id: combatTypeSelector
                            on_active: app.combatselected(*args)
                        
                        MDIcon:
                            icon: 'sword-cross'
                            pos_hint: {'x': .75, 'center_y': .5}
                                
                        MDLabel:
                            pos_hint: {'x': .95, 'center_y': .5}
                            text: "Shock"
                            font_style: 'Caption'
                    
                    FloatLayout:
                        orientation: 'horizontal'
                        pos_hint: {'center_x': .5, 'center_y': .5}

                        MDLabel:
                            pos_hint: {'center_x': .9, 'center_y': .5}
                            text: "Assault?"
                            font_style: 'Body2'
                            
                        MDCheckbox:
                            id: assaultSelector
                            pos_hint: {'center_x': .95, 'center_y': .5}
                            size_hint: None, None
                            size: "48dp", "48dp"
                            on_active: app.assaultselected(*args)
                        
                Widget:
                    id: separator
                    size_hint_y: None
                    height: 6
                    canvas:
                        Color:
                            rgba: 0., 0., 1., 0.5
                        Rectangle:
                            pos: 10, separator.center_y
                            size: separator.width, 2
                
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_max_y: '40dp'

                    MDLabel:
                        text: 'Attackers:'
                        font_style: 'Body2'
                    MDDropDownItem:
                        pos_hint: {'center_x': 0, 'center_y': .5}
                        id: attackerTechButton
                        text: 'MED'
                        font_size: '14sp'
                        on_release: app.attackertechmenu.open()
                    BoxLayout:
                        orientation: 'horizontal'
                        MDLabel:
                            halign: 'right'
                            text: "Pursuing?"
                            font_style: 'Body2'
                        MDCheckbox:
                            id: attackerPursuing
                            pos_hint: {'center_x': .95, 'center_y': .5}
                            size_hint: None, None
                            size: "48dp", "48dp" 
                            on_active: app.attackerpursuingselected(*args) 
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 2
                    size_hint: (1,0.3)
                    MDTextField:
                        id: txt_field_mrl_att
                        hint_text: 'Morale'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'att', 'morale')
                    MDRaisedButton:
                        id: 'mrl+att'
                        pos_hint: {"center_y": .5}
                        size_hint: (0.3,1)
                        text: "+"
                        on_press: app.increment(self,'mrl','att')        
                    MDRaisedButton:
                        id: 'mrl-att'
                        pos_hint: {"center_y": .5}
                        size_hint: (0.3,1)
                        text: "-"
                        on_press: app.increment(self,'mrl','att')
                    MDLabel:
                        halign: 'right'
                        text: "ModRoll="
                        font_style: 'Body1'
                    MDLabel:
                        id: att_roll_label
                        halign: 'left'
                        text: "3"
                        font_style: 'Body1'
                        
                MDSlider:
                    size_hint: (1,0.4)
                    hint: False
                    id: attacker_roll_slider
                    min: 3
                    max: 14
                    value: 3
                    on_value: app.roll_slider_change('att',self.value)
                
                
                    
                BoxLayout: 
                    orientation: 'horizontal'
                    size_hint: (1,1.1)
                    spacing: 5
                    
                    MDTextField:
                        id: txt_field_inf_att
                        hint_text: 'Inf'
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'att', 'inf')
                    
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        
                        MDRaisedButton:
                            size_hint: (1,0.25)
                            id: 'inf+att'
                            text: "+"
                            on_press: app.increment(self,'inf','att')
                    
                
                        MDRaisedButton:
                            id: 'inf-att'
                            size_hint: (1,0.25)
                            text: "-"
                            on_press: app.increment(self,'inf','att')
                            
                        MDRaisedButton:
                            id: 'inf+10att'
                            size_hint: (1,0.25)
                            text: "+10"
                            on_press: app.increment(self,'inf','att')
                        
                        MDRaisedButton:
                            id: 'inf-10att'
                            text: "-10"
                            size_hint: (1,0.25)
                            on_press: app.increment(self,'inf','att')
                    
                    MDTextField:
                        id: txt_field_cav_att
                        hint_text: "Cav"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'att', 'cav')
                        
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'cav+att'
                            size_hint: (1,0.25)
                            text: "+"
                            on_press: app.increment(self,'cav','att')
                        
                    
                        MDRaisedButton:
                            id: 'cav-att'
                            size_hint: (1,0.25)
                            text: "-"
                            on_press: app.increment(self,'cav','att')
                            
                        MDRaisedButton:
                            id: 'cav+10att'
                            size_hint: (1,0.25)
                            text: "+10"
                            on_press: app.increment(self,'cav','att')
                        
                        MDRaisedButton:
                            id: 'cav-10att'
                            size_hint: (1,0.25)
                            text: "-10"
                            on_press: app.increment(self,'cav','att')
                    
                    MDTextField:
                        id: txt_field_art_att
                        hint_text: "Art"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'att', 'art')
                        
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'art+att'
                            size_hint: (1,0.25)
                            text: "+"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','att')
                        
                    
                        MDRaisedButton:
                            id: 'art-att'
                            size_hint: (1,0.25)
                            text: "-"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','att')
                            
                        MDRaisedButton:
                            id: 'cav+10att'
                            size_hint: (1,0.25)
                            text: "+10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','att')
                        
                        MDRaisedButton:
                            id: 'cav-10att'
                            size_hint: (1,0.25)
                            text: "-10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','att')
                    
                    MDTextField:
                        id: txt_field_pac_att
                        hint_text: "Pasha"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'att', 'pac')
                        
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'pac+att'
                            size_hint: (1,0.25)
                            text: "+"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'pac','att')
                        
                    
                        MDRaisedButton:
                            id: 'pac-att'
                            size_hint: (1,0.25)
                            text: "-"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'pac','att')
                            
                        MDRaisedButton:
                            id: 'pac+10att'
                            size_hint: (1,0.25)
                            text: "+10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'pac','att')
                        
                        MDRaisedButton:
                            id: 'pac-10att'
                            size_hint: (1,0.25)
                            text: "-10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'pac','att')
                    
                    
                
                MDLabel:
                    text: 'Attackers results:' 
                    font_style: 'Caption'
                    size_hint: 1, 0.2
                MDLabel:
                    id: att_results
                    text: 'XXX.X pow  table X:  [XX%, -X] : cause XX loss'
                    font_style: 'Body1'
                    size_hint: 1, 0.2
                
                
                
                Widget:
                    id: separator
                    size_hint_y: None
                    height: 6
                    canvas:
                        Color:
                            rgba: 0., 0., 1., 0.5
                        Rectangle:
                            pos: 10, separator.center_y
                            size: separator.width, 2
                        
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint: (1,0.7)
                    MDLabel:
                        pos_hint: {'center_x': 0, 'center_y': .5}
                        text: 'Defenders:'
                        font_style: 'Body2'
                        size_hint: 0.4, None
                    MDTextField:
                        pos_hint: {'center_x': 0, 'center_y': .5}
                        size_hint: 0.2, None
                        id: txt_field_pac_def
                        hint_text: "Pasha"
                        text: '0'
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'pac')
                    MDTextField:
                        pos_hint: {'center_x': 0, 'center_y': .5}
                        size_hint: 0.2, None
                        id: txt_field_lvl_def
                        hint_text: "Ftr LVL"
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self,  'def', 'frt_lvl')
                    MDDropDownItem:
                        size_hint: 0.2, None
                        pos_hint: {'center_x': 0, 'center_y': .5}
                        id: defenderTechButton
                        text: 'MED'
                        font_size: '14sp'
                        on_release: app.defendertechmenu.open()
                    BoxLayout:
                        size_hint: 0.6, None
                        pos_hint: {'center_x': 0.5, 'center_y': .5}
                        orientation: 'horizontal'
                        MDLabel:
                            halign: 'right'
                            text: "Pursuing?"
                            font_style: 'Body2'
                        MDCheckbox:
                            id: defenderPursuing
                            pos_hint: {'center_x': .95, 'center_y': .5}
                            size_hint: None, None
                            size: "48dp", "48dp"
                            on_active: app.defenderpursuingselected(*args)  
                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 2
                    size_hint: (1,0.3)
                    MDTextField:
                        id: txt_field_mrl_def
                        hint_text: 'Morale'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'morale')
                    MDRaisedButton:
                        id: 'mrl+def'
                        pos_hint: {"center_y": .5}
                        size_hint: (0.3,1)
                        text: "+"
                        on_press: app.increment(self,'mrl','def')        
                    MDRaisedButton:
                        id: 'mrl-def'
                        pos_hint: {"center_y": .5}
                        size_hint: (0.3,1)
                        text: "-"
                        on_press: app.increment(self,'mrl','def')
                    MDLabel:
                        halign: 'right'
                        text: "ModRoll="
                        font_style: 'Body1'
                    MDLabel:
                        id: def_roll_label
                        halign: 'left'
                        text: "3"
                        font_style: 'Body1'
                        
                MDSlider:
                    size_hint: (1,0.4)
                    id: defender_roll_slider
                    hint: False
                    min: 3
                    max: 14
                    value: 3
                    on_value: app.roll_slider_change('def',self.value)
                    
                BoxLayout: 
                    orientation: 'horizontal'
                    size_hint: (1,1.1)
                    spacing: 2
                    
                    MDTextField:
                        id: txt_field_inf_def
                        hint_text: 'Inf'
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'inf')
                    
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        
                        MDRaisedButton:
                            size_hint: (1,0.25)
                            id: 'inf+def'
                            text: "+"
                            on_press: app.increment(self,'inf','def')
                    
                
                        MDRaisedButton:
                            id: 'inf-def'
                            size_hint: (1,0.25)
                            text: "-"
                            on_press: app.increment(self,'inf','def')
                            
                        MDRaisedButton:
                            id: 'inf+10def'
                            size_hint: (1,0.25)
                            text: "+10"
                            on_press: app.increment(self,'inf','def')
                        
                        MDRaisedButton:
                            id: 'inf-10def'
                            text: "-10"
                            size_hint: (1,0.25)
                            on_press: app.increment(self,'inf','def')
                    
                    MDTextField:
                        id: txt_field_cav_def
                        hint_text: "Cav"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'cav')
                        
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'cav+def'
                            size_hint: (1,0.25)
                            text: "+"
                            on_press: app.increment(self,'cav','def')
                        
                    
                        MDRaisedButton:
                            id: 'cav-def'
                            size_hint: (1,0.25)
                            text: "-"
                            on_press: app.increment(self,'cav','def')
                            
                        MDRaisedButton:
                            id: 'cav+10def'
                            size_hint: (1,0.25)
                            text: "+10"
                            on_press: app.increment(self,'cav','def')
                        
                        MDRaisedButton:
                            id: 'cav-10def'
                            size_hint: (1,0.25)
                            text: "-10"
                            on_press: app.increment(self,'cav','def')
                    
                    MDTextField:
                        id: txt_field_art_def
                        hint_text: "Art"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'art')
                    
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'art+def'
                            size_hint: (1,0.25)
                            text: "+"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','def')
                        
                    
                        MDRaisedButton:
                            id: 'art-def'
                            size_hint: (1,0.25)
                            text: "-"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','def')
                            
                        MDRaisedButton:
                            id: 'cav+10def'
                            size_hint: (1,0.25)
                            text: "+10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','def')
                        
                        MDRaisedButton:
                            id: 'cav-10def'
                            size_hint: (1,0.25)
                            text: "-10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'art','def')
                    
                    MDTextField:
                        id: txt_field_fcv_def
                        hint_text: "FortCV"
                        font_size: '20sp'
                        text: '0'
                        pos_hint: {"center_y": .5}
                        input_filter: 'int'
                        input_type: 'number'
                        on_focus: Clock.schedule_once(lambda dt: self.select_all()) if self.focus else None
                        on_text: app.textfield_change(self, 'def', 'frt_cv')
                        
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: 2
                        MDRaisedButton:
                            id: 'fcv+def'
                            size_hint: (1,0.25)
                            text: "+"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'fcv','def')
                        
                    
                        MDRaisedButton:
                            id: 'fcv-def'
                            size_hint: (1,0.25)
                            text: "-"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'fcv','def')
                            
                        MDRaisedButton:
                            id: 'fcv+10def'
                            size_hint: (1,0.25)
                            text: "+10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'fcv','def')
                        
                        MDRaisedButton:
                            id: 'cav-10fcv'
                            size_hint: (1,0.25)
                            text: "-10"
                            pos_hint: {"center_y": .7}
                            on_press: app.increment(self,'fcv','def')
                    
                    
                MDLabel:
                    text: 'Defenders results:'
                    font_style: 'Caption'
                    size_hint: 1, 0.2
                MDLabel:
                    id: def_results
                    text: 'XXX.X pow  table X:  [XX%, -X] : cause XX loss'
                    font_style: 'Body1'
                    size_hint: 1, 0.2                      
                            
                
                    
                
                    
                
                
                
        
        MDBottomNavigationItem:
            name: 'NavalScreen'
            text: 'Naval'
            icon: 'ship-wheel'       
'''


class EuApp(MDApp):
    terrainmenu = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.eu = euhandler.euhandler()
        self.screen = Builder.load_string(KV)
        self.terrainmenu = MDDropdownMenu(
            caller = self.screen.ids.terrainButton,
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
            caller=self.screen.ids.attackerTechButton,
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
            caller=self.screen.ids.defenderTechButton,
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

    def terrainmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.terrainButton.set_item(instance_menu_item.text)
        terrconv = {'Clear': 'clear', 'Mount.': 'mountain', 'Forest': 'forest', 'Marsh': 'marsh'}
        self.eu.terrain = terrconv[instance_menu_item.text]
        self.update()
        self.terrainmenu.dismiss()

    def attackertechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.attackerTechButton.set_item(instance_menu_item.text)
        self.eu.attacker['ltech'] = instance_menu_item.text
        self.update()
        self.attackertechmenu.dismiss()

    def defendertechmenu_item_selected(self, instance_menu, instance_menu_item):
        self.screen.ids.defenderTechButton.set_item(instance_menu_item.text)
        self.eu.defender['ltech'] = instance_menu_item.text
        self.update()
        self.defendertechmenu.dismiss()

    def roll_slider_change(self,att_or_def,value):
        rounded = math.ceil(value)
        if att_or_def == 'att':
            self.screen.ids.att_roll_label.text = str(rounded)
            self.eu.attacker['roll'] = rounded
        elif att_or_def == 'def':
            self.screen.ids.def_roll_label.text = str(rounded)
            self.eu.defender['roll'] = rounded
        self.update()

    def assaultselected(self, instance, value):
        if value:
            self.eu.assault = value
            self.screen.ids.defenderPursuing.active = False
            self.screen.ids.attackerPursuing.active = False
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
            self.screen.ids.combatTypeSelector.active = True
            self.screen.ids.attackerPursuing.active = False
            self.screen.ids.assaultSelector.active = False
            if dbug:
                print('Defender pursuing is ', value)
        else:
            self.eu.defender_pursuing = value
            if dbug:
                print('Defender pursuing is ', value)
        self.update()

    def attackerpursuingselected(self, instance, value):
        if value:
            self.eu.attacker_pursuing = value
            self.screen.ids.combatTypeSelector.active = True
            self.screen.ids.defenderPursuing.active = False
            self.screen.ids.assaultSelector.active = False
            if dbug:
                print('Attacker pursuing is ', value)
        else:
            self.eu.attacker_pursuing = value
            if dbug:
                print('Attacker pursuing is ', value)
        self.update()

    def combatselected(self, instance, value):
        if value:
            self.eu.type_of_combat = 'shock'
            if dbug:
                print('shock phase')
        else:
            self.eu.type_of_combat = 'fire'
            self.screen.ids.defenderPursuing.active = False
            self.screen.ids.attackerPursuing.active = False
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

    def increment(self, buttonInstance, unit, att_or_def):
        #Define the id of the text field that needs to be changed
        textId = 'txt_field_'+unit+'_'+att_or_def
        #Get the current value of the field
        if not self.screen.ids[textId].text.isdigit():
            value = 0
        else:
            value = int(self.screen.ids[textId].text)
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
        self.screen.ids[textId].text = str(value)


    def update(self):
        self.eu.updateall()
        base_string = '{0} pow  table {1}:  [{2}%, -{3}] : cause {4} loss'
        att_string = base_string.format(
            self.eu.results['attstr'], self.eu.results['tblatt'],
            self.eu.results['attresult'], self.eu.results['ainflictmorale'],
            self.eu.results['ainflict']
        )
        self.screen.ids['att_results'].text = att_string

        def_string = base_string.format(
            self.eu.results['defstr'], self.eu.results['tbldef'],
            self.eu.results['defresult'], self.eu.results['dinflictmorale'],
            self.eu.results['dinflict']
        )
        self.screen.ids['def_results'].text = def_string
        if dbug:
            self.eu.fancyprint()


    def get_id(self, instance):
        for id, widget in instance.parent.ids.items():
            if widget.__self__ == instance:
                return id

    def build(self):
        return self.screen



if __name__ == "__main__":
    EuApp().run()
