#import kivy
#kivy.require('1.7.2') # replace with your current kivy version !


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
import birthday
import datetime
from dateutil.relativedelta import relativedelta

class HomeScreen(Screen):

    top_layout = ObjectProperty(None)
    btnDay = ObjectProperty(None)
    btnMonth = ObjectProperty(None)
    #btnYear = ObjectProperty(None)
    btnAsk = ObjectProperty(None)
    yearInput = ObjectProperty(None)

    result = ObjectProperty(None)
    birthday = birthday.Birthday()

    unicode_string = StringProperty("Unesite dan, mjesec i godinu rođenja:")

    def on_pause(self):
        return True

    def on_pause(self):
        pass

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        dropdown = DropDown()

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

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: self.setDay(self, x))

        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

  ########################### Month ########################################


        dropdownMonth = DropDown()
        #notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
        for monthNo in range(1,13):
            # when adding widgets, we need to specify the height manually (disabling
            # the size_hint_y) so the dropdown can calculate the area it needs.
            month = Button(text='%s' % monthNo, size_hint_y=None, height='50sp',background_color=(.5,.5,.5,1))

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            month.bind(on_release=lambda month: dropdownMonth.select(month.text))

            # then add the button inside the dropdown
            dropdownMonth.add_widget(month)

        # create a big main button

        print ('yay') 

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        self.btnMonth.bind(on_release=dropdownMonth.open)
        #dd_btn.bind(on_release=dropdown.open)
        print ('1') 

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdownMonth.bind(on_select=lambda instance, x: self.setMonth(self, x))
        print ('2') 

        #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))


       # self.top_layout.add_widget(mainbuttonMonth)

########################### Year ########################################


        # dropdownYear = DropDown()
        # #notes = ['Features', 'Suggestions', 'Abreviations', 'Miscellaneous']
        # for year in range(1950,2018):
        #     # when adding widgets, we need to specify the height manually (disabling
        #     # the size_hint_y) so the dropdown can calculate the area it needs.
        #     btnYear = Button(text='%r' % year, size_hint_y=None, height='50sp',background_color=(.5,.5,.5,1))

        #     # for each button, attach a callback that will call the select() method
        #     # on the dropdown. We'll pass the text of the button as the data of the
        #     # selection.
        #     btnYear.bind(on_release=lambda btnYear: dropdownYear.select(btnYear.text))

        #     # then add the button inside the dropdown
        #     dropdownYear.add_widget(btnYear)

        # # create a big main button

        # print ('yay') 

        # # show the dropdown menu when the main button is released
        # # note: all the bind() calls pass the instance of the caller (here, the
        # # mainbutton instance) as the first argument of the callback (here,
        # # dropdown.open.).
        # self.yearInput.bind(on_select=dropdownYear.open)
        # #dd_btn.bind(on_release=dropdown.open)

        # # one last thing, listen for the selection in the dropdown list and
        # # assign the data to the button text.
        # dropdownYear.bind(on_select=lambda instance, x: self.setYear(self, x))
        # #dropdownYear.bind(on_select=setYear(self, x))

        # #dropdown.bind(on_select=lambda instance, x: setattr(dd_btn, 'text', x))

        # # self.top_layout.add_widget(mainbuttonMonth)

        self.btnAsk.bind(on_release=self.calculateAge)


    # def setYear(dummy, self, x):
    #     self.btnYear.text = "Godina: " + x
    #     self.birthday.setYear(x)

    def setYear(dummy, self):
        self.birthday.setYear(self.yearInput.text)

    def setMonth(dummy, self, x):
        self.btnMonth.text = "Mjesec: " + x
        self.birthday.setMonth(x)

    def setDay(dummy, self, x):
        self.btnDay.text = "Dan: " + x
        self.birthday.setDay(x)


    def calculateAge(self, button):

        #self.result.text = self.birthday.getDay() + self.birthday.getMonth() + self.birthday.getYear()

        self.setYear(self)
        self.yearInput.text = ""
        self.btnDay.text = "Odaberite dan"
        self.btnMonth.text = "Odaberite mjesec"

        try:
            print(self.birthday.getYear())
            print(self.birthday.getMonth())
            print(self.birthday.getDay())
            rodjendan = datetime.date(int(self.birthday.getYear()), int(self.birthday.getMonth()), int(self.birthday.getDay()))
            star = relativedelta(datetime.date.today(), rodjendan)
            self.result.text = ("RoĐeni ste %d.%d.%d.\n\nVi ste danas stari točno %d godina, %d mjeseci i %d dana." % (rodjendan.day, rodjendan.month, rodjendan.year, star.years, star.months,star.days))
        except (ValueError, TypeError):
            self.result.text = "Upisali ste nevažeći datum. Pokušajte ponovno."



        print("from first")


class oldApp(App):

    def build(self):

        return HomeScreen()



if __name__ == '__main__':
    oldApp().run()
