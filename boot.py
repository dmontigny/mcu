import gc
from blink import blinkme

from get_wifi import wifi_me

print('[boot]')


gc.collect()
print('Memory free:', gc.mem_free())

wifi_me()

gc.collect()
print('Memory free:', gc.mem_free())

blinkme()

gc.collect()
print('Memory free:', gc.mem_free())

import webblink