#!"c:\users\jun jiet ng\gitrepos\intermediate-python-projects\intermediate-python\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'contactbook','console_scripts','contactbook'
__requires__ = 'contactbook'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('contactbook', 'console_scripts', 'contactbook')()
    )
