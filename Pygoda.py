from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
#import time
#import locale

# locale.setlocale(locale.LC_TIME, 'uk_UA')

# seconds = time.time()
# local = time.ctime(seconds)

# write_file = open('my_file.txt', 'w')
# write_file.write(str(local))
# write_file.close()

# file = 'my_file.txt'
# file_date_mod = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%A, %d %b, %H:%M:%S")

# f = open('last_date.txt', 'w')
# for i in file_date_mod:
#    f.write(i)
# f.close()

config_dict = get_default_config()
config_dict['language'] = 'ua'
owm = OWM('6ba59007b4e78a432035fbeaf72b427e')
mgr = owm.weather_manager()
observation = mgr.weather_at_place("Volodymyr-Volynskyi, UA")
w = observation.weather
status = w.detailed_status
temp = w.temperature('celsius')["temp"]
#bot.send_message(game.chat.id,str(file_date_mod))
pogod = f'У Володимирі: {str(temp)}℃ {status}'
