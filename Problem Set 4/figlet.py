from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit('Invalid usage')

if len(sys.argv) == 3 :
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in fonts:
        sys.exit('Invalid usage')

text = input('Input: ').strip()

if len(sys.argv) == 3:
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))


if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
    print(figlet.renderText(text))

