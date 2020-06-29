import re
import datetime
import os

#
# TODO: add version validation step
#

def status(s):
    """Prints things in bold."""
    print('\033[1m{0}\033[0m'.format(s))

def set_version(artifact='', master=False, release=False):
    status(f"Setting version for {artifact} artifact")

    current_version = os.popen(f"git describe --match {artifact}-release-* --tags").read()
    if not current_version:
        current_version = "0.0"
        status(f"No tag found for {artifact}, resetting to {current_version}")
    else:
        status(f"Current version for {artifact} is {current_version}")

    current_version_array = re.findall(r'\d+', current_version)
    current_version_array = [int(i) for i in current_version_array[0:2]]

    status(f"Version numbers for {artifact} are {current_version_array}")

    if release:
        new_version = str(current_version_array[0]+1) + ".0"
    elif master:
        new_version = str(current_version_array[0]) + "." + str(current_version_array[1]) + "-rc" + datetime.datetime.now().strftime("%y%m%d%H%M%S")
    else:
        new_version = str(current_version_array[0]) + "." + str(current_version_array[1]) + "-dev" + datetime.datetime.now().strftime("%y%m%d%H%M%S")
    # TODO: add local version x.y-devTIMESTAMP[local]

    status(f"New version is {new_version}")

    status("Changing version in the __version__.py")
    version_file = open('__version__.py','w')
    version_file.seek(0)
    version_file.write(f"__version__ = \'{new_version}\'")
    version_file.close()

set_version('lib', True, False)


#
# print("Incrementing minor version")
# print(f"Current version is {__version__}")
# version_numbers = re.findall(r'\d+', __version__)
# version_numbers = [int(i) for i in version_numbers]
#
# __version__ = str(version_numbers[0]) + "." + str(version_numbers[1]+1)
#
# print(f"Changed version to {__version__}")





