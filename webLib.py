import webbrowser, sys, pyperclip

"""
Small script for opening from Run with a .bat file
The script take address as an argument or you just have to copy to clipboard
and hit enter google maps will show the address.

for .bat file create a new file and put this line in that file

@py.exe PATH_TO_THE_SCRIPT/SCRIPT_NAME.py %*

Now save with .bat extension

then put the path of .bat file in Enviroment variable

Run by SUPER_KEY + R and enter .bat file name with arguments or copy to clipboard

"""

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
