# by Dean R. on 2016-12-18
import datetime
from dateutil.relativedelta import relativedelta

ime = input('Kako se zoveš?\n') 
ime = ime.capitalize()
print('\nBok %s.' % ime)
prezime = input('\n%s, kako se prezivaš?\n' % ime)
prezime = prezime.capitalize()
while True:
  godina = input('\n%s %s, koje godine si rođen?\n' % (ime, prezime))
  mjesec = input('\nKoji mjesec si rođen?\n')
  dan = input('\nI za kraj, koji si dan u mjesecu rođen?\n')
  try:
    rodjendan = datetime.date(int(godina), int(mjesec), int(dan))
    break
  except (ValueError, TypeError):
    print('\nUpisao si nevažeći datum. Pokušaj ponovno.')
print('\n%s, rođen si %s.%s.%s.' % (ime, rodjendan.day, rodjendan.month, rodjendan.year))
star = relativedelta(datetime.date.today(), rodjendan)
print('\n%s %s, ti si danas star(a) točno %s godina, %s mjeseci i %s dana.\n' % (ime, prezime, star.years, star.months, star.days))
print('Želim ti ugodan ostatak dana :)\n')