import webbrowser, sys

address='escorpion 3701-B la calma'
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
URL = f'https://www.google.com/maps/place/{address}'


webbrowser.open(URL)
