from __version__ import __version__
import re
import datetime

# TODO: add version validation step

print("Incrementing minor version")
print(f"Current version is {__version__}")
version_numbers = re.findall(r'\d+', __version__)
version_numbers = [int(i) for i in version_numbers]

__version__ = str(version_numbers[0]) + "." + str(version_numbers[1]+1)

print(f"Changed version to {__version__}")

version_file = open('__version__.py','r+')
version_file.seek(0)
version_file.write("__version__ = \'"+__version__+"\'")
version_file.close()



