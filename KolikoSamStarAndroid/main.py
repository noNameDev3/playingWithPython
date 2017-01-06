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

  ########################### Day ########################################

        for note in range(1,32):
            btn = Button(text='%r' % note, size_hint_y=None, height='50sp', background_color=(.5,.5,.5,1))

            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn)

        self.btnDay.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: self.setDay(self, x))

  ########################### Month ########################################

        dropdownMonth = DropDown()
        for monthNo in range(1,13):
            month = Button(text='%s' % monthNo, size_hint_y=None, height='50sp',background_color=(.5,.5,.5,1))

            month.bind(on_release=lambda month: dropdownMonth.select(month.text))

            dropdownMonth.add_widget(month)

        self.btnMonth.bind(on_release=dropdownMonth.open)
        dropdownMonth.bind(on_select=lambda instance, x: self.setMonth(self, x))
 
 ###########################################################################
        self.btnAsk.bind(on_release=self.calculateAge)


    def setYear(dummy, self):
        self.birthday.setYear(self.yearInput.text)

    def setMonth(dummy, self, x):
        self.btnMonth.text = "Mjesec: " + x
        self.birthday.setMonth(x)

    def setDay(dummy, self, x):
        self.btnDay.text = "Dan: " + x
        self.birthday.setDay(x)

    def croatianGrammar(dummy, croText, old):
        print("in cro")
        if abs(old.days) % 10 == 0:
            croText[2] = "dana"
        elif abs(old.days) % 10 == 1 and abs(old.days) % 100 != 11:
            croText[2] = "dan"
        elif abs(old.days) % 100 > 10 and abs(old.days) % 100 < 20:
            croText[2] = "dana"
        elif abs(old.days) % 10 > 1 and abs(old.days) % 10 < 5:
            croText[2] = "dana"
        else:
            croText[2] = "dana"

        if abs(old.months) % 10 == 0:
            croText[1] = "mjeseci"
        elif abs(old.months) % 10 == 1 and abs(old.months) % 100 != 11:
            croText[1] = "mjesec"
        elif abs(old.months) % 100 > 10 and abs(old.months) % 100 < 20:
            croText[1] = "mjeseci"
        elif abs(old.months) % 10 > 1 and abs(old.months) % 10 < 5:
            croText[1] = "mjeseca"
        else:
            croText[1] = "mjeseci"

        if abs(old.years) % 10 == 0:
            croText[0] = "godina"
        elif abs(old.years) % 10 == 1 and abs(old.years) % 100 != 11:
            croText[0] = "godinu"
        elif abs(old.years) % 100 > 10 and abs(old.years) % 100 < 20:
            croText[0] = "godina"
        elif abs(old.years) % 10 > 1 and abs(old.years) % 10 < 5:
            croText[0] = "godine"
        else:
            croText[0] = "godina"

    def calculateAge(self, button):

        self.setYear(self)
        self.yearInput.text = ""
        self.btnDay.text = "Odaberite dan"
        self.btnMonth.text = "Odaberite mjesec"

        croText = ["", "", ""]

        try:
            print(self.birthday.getYear())
            print(self.birthday.getMonth())
            print(self.birthday.getDay())
            rodjendan = datetime.date \
                (int(self.birthday.getYear()), int(self.birthday.getMonth()), int(self.birthday.getDay()))
            old = relativedelta(datetime.date.today(), rodjendan)

            self.croatianGrammar(croText, old)

            danas = datetime.date.today()
            if rodjendan < danas:
                self.result.text = ("Rođeni ste %d.%d.%d.\n\nVi ste danas stari %d %s, %d %s i %d %s." \
                     % (rodjendan.day, rodjendan.month, rodjendan.year, old.years,croText[0],  \
                      old.months, croText[1], old.days, croText[2]))
            elif rodjendan > danas:
                self.result.text = ("Dobro došao u %d. putniče iz budućnosti.\nRoditi ćeš se za %d %s, %d %s i %d %s." \
                    % (datetime.date.today().year, abs(old.years),croText[0], abs(old.months),  \
                    croText[1], abs(old.days), croText[2]))
            else:
                self.result.text = ("Ti si se rodio danas. Dobrodošao na svijet ;)")
        except (ValueError, TypeError):
            self.result.text = "Upisali ste nevažeći datum. Pokušajte ponovno."


class oldApp(App):

    def build(self):

        return HomeScreen()


if __name__ == '__main__':
    oldApp().run()
