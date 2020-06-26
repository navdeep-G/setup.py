from __version__ import __version__
import re
import datetime

__version__ = __version__ + "-dev" + datetime.datetime.now().strftime("%y%m%d%H%M%S")

version_file = open('__version__.py','r+')
version_file.seek(0)
version_file.write("__version__ = \'"+__version__+"\'")
version_file.close()



