from kivymd.app import MDApp
from kivy import *
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.pickers import MDDatePicker,MDTimePicker
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.screen import Screen
from kivy.uix.tabbedpanel import TabbedPanel
import mysql.connector
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet

Builder.load_file('Project1.kv')

class Screen1(Screen): pass

class MyTabs(TabbedPanel):
    color = (1, .2, .3, 1)

    def hello_on(self):
        self.ids.mylbl.text = 'Evans rocks'
        self.ids.img.source = 'C:\\Users\\USER\\Pictures\\funky10.jpg'

    def hello_off(self):
        self.ids.img.source = 'C:\\Users\\USER\\PycharmProjects\\kivytake2\\family1.jpg'


    choices = []

    def tick(self, instance, value, toppings):
        if value == True:
            MyTabs.choices.append(toppings)
            self.ids.output.text = str(MyTabs.choices)
        else:
            MyTabs.choices.remove(toppings)
            self.ids.output.text = str(MyTabs.choices)

        print(instance)


class MyImage(Widget): pass



''' def selected(self, filename):
        try:
            self.ids.MyImage.source = filename[0]
            print(filename[0])
        except:
            self.ids.MyImage.source = 'Error in loading Image'

    choices = []

    def tick(self, instance, value, toppings):
        if value == True:
            MyCarousel.choices.append(toppings)
            self.ids.output.text = str(MyCarousel.choices)
        else:
            MyCarousel.choices.append(toppings)
            self.ids.output.text = str(MyCarousel.choices)

        print(value)
    pass '''

class MyImg(Widget):
   def selected(self,filename):
       try:
           self.ids.MyImage.source = filename[0]
           print(filename[0])
       except:
           self.ids.MyImage.source = 'Error in loading Image'

class MyCarousel(Widget):
    choices = []
    def tick(self,instance,value, toppings):
       if value == True:
           MyCarousel.choices.append(toppings)
           self.ids.output.text = str(MyCarousel.choices)
       else:
           MyCarousel.choices.remove(toppings)
           self.ids.output.text = str(MyCarousel.choices)

       print(value)

class RightItemsActions(BoxLayout):
    screen_mng = ObjectProperty()

class EvansApp(MDApp):
    title = 'Evans First Real App And Hoping to make it big'
    #theme_cls = ThemeManager()
    data = {
     'language-python': 'language-python',
     'youtube': 'youtube', 'andriod': 'andriod',
    }
    def show_example_custom_bottom_sheet(self):
        bottom_sheet = Factory.ContentCustomSheet()


        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Purple'

        return Screen1()

    def save(self,instance,value,date_range):
        print(instance,value,date_range)
        #self.root.ids.date.text = f'{value}'
        self.root.ids.date.text = f'{value}'

    def cancel(self,instance,value,date_range):
        self.root.ids.date.text = 'You cancelled th program'

    def show_date(self):
        todays_date = MDDatePicker(year=2003,month=4,day=1)
        todays_date.bind(on_save=self.save,on_cancel=self.cancel)
        todays_date.open()

    def savetime(self,instance,time):
        self.root.ids.date.text = f'{time}'

    def canceltime(self,instance,time):
        self.root.ids.date.text = 'You cancelled the time program'

    def show_time(self):
        todays_time=MDTimePicker()
        todays_time.bind(time=self.savetime,on_cancel=self.canceltime)
        todays_time.open()


EvansApp().run()