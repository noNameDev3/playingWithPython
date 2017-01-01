#import kivy
#kivy.require('1.7.2') # replace with your current kivy version !


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty

class CustomDropDown(DropDown):
    for i in range(5):
        print (i) 

class Birthday():

    date = 29

    def setDate(dummy, selectedDate):
        Birthday.date = selectedDate
    
    def getDate(dummy):
        return Birthday.date

class HomeScreen(Screen):

    top_layout = ObjectProperty(None)
    result = ObjectProperty(None)
    birthday = Birthday()

    unicode_string = StringProperty("""Unesite dan, mjesec i godinu rodenja: """)

    def on_pause(self):
        return True

    def calculateAge(self, button):




        self.result.text = self.birthday.getDate()


        print("from first")

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        self.drop_down = CustomDropDown()
        #notes_dropdown = ObjectProperty(None)


        dropdown = DropDown()
        #notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
        for note in range(1,32):
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btn = Button(text='%r' % note, size_hint_y=None, height='50sp', background_color=(.5,.5,.5,1))

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        #mainbutton = Button(text='1', size_hint=(0.5, 0.3), pos_hint= {'center_x': 0.5} )
        print ('yay') 

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.btnDay.bind(on_release=dropdown.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(self.btnDay, 'text', "Dan: " + x))

        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

        #self.top_layout.add_widget(button_day)

########################### Month ########################################


        dropdownMonth = DropDown()
        #notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
        for month in range(1,13):
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btnMonth = Button(text='%r' % month, size_hint_y=None, height='50sp',background_color=(.5,.5,.5,1))

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btnMonth.bind(on_release=lambda btn: dropdownMonth.select(btnMonth.text))

            # then add the button inside the dropdown
            dropdownMonth.add_widget(btnMonth)

        # create a big main button

        print ('yay') 

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.btnMonth.bind(on_release=dropdownMonth.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdownMonth.bind(on_select=lambda instance, x: setattr(self.btnMonth, 'text', "Mjesec: " + x))

        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

        self.btnAsk.bind(on_release=self.calculateAge)

       # self.top_layout.add_widget(mainbuttonMonth)

########################### Year ########################################


        dropdownYear = DropDown()
        #notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
        for year in range(1950,2018):
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            btnYear = Button(text='%r' % year, size_hint_y=None, height='50sp',background_color=(.5,.5,.5,1))

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btnYear.bind(on_release=lambda btn: dropdownYear.select(btnYear.text))

            # then add the button inside the dropdown
            dropdownYear.add_widget(btnYear)

        # create a big main button

        print ('yay') 

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.btnYear.bind(on_release=dropdownYear.open)
        #dd_btn.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdownYear.bind(on_select=lambda instance, x: self.setYear(self, x))
        #dropdownYear.bind(on_select=setYear(self, x))

        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

       # self.top_layout.add_widget(mainbuttonMonth)

    def setYear(dummy, self, x):
        self.btnYear.text = "Godina: " + x
        self.birthday.setDate(x)



class oldApp(App):

    def build(self):

        return HomeScreen()



if __name__ == '__main__':
    oldApp().run()
