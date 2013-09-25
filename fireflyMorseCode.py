import re
string = 'beeepbeeepbeeepbeeepbeeep beepbeepbeepbeeepbeeep beepbeepbeepbeeepbeeep beeepbeeepbeeepbeeepbeeep beepbeepbeepbeepbeeep beeepbeepbeepbeepbeep beeepbeeepbeeepbeeepbeep beeepbeeepbeeepbeeepbeep beeepbeeepbeeepbeepbeep beepbeepbeepbeeepbeeep beeepbeeepbeepbeepbeeepbeeep beeepbeeepbeeepbeeepbeep beeepbeeepbeepbeepbeep beeepbeeepbeeepbeepbeep beeepbeeepbeeepbeeepbeeep beepbeepbeepbeeepbeeep beepbeepbeepbeeepbeeep beeepbeeepbeeepbeeepbeeep beepbeepbeepbeepbeeep beeepbeepbeepbeepbeep beeepbeeepbeeepbeeepbeep beeepbeeepbeeepbeeepbeep beeepbeeepbeeepbeepbeep beepbeepbeeepbeeepbeeep'
words = string.split(' ')
decodedWords = []
for word in words:
    splitString = word.split('p')
    beeps = []
    for beep in splitString:
        Es = 0
        for letter in beep:
            if letter == 'e': Es += 1
        if Es == 2:
            beeps.append('.')
        elif Es == 3: 
            beeps.append('-')
    decodedWords.append(beeps)

decodedString = ''
for word in decodedWords:
    decodedString += ''.join(word)+' '
print decodedString
## Solution: ----- ...-- ...-- ----- ....- -.... ----. ----. ---.. ...-- --..-- ----. --... ---.. ----- ...-- ...-- ----- ....- -.... ----. ----. ---.. ..---
## Then translate from morse code to something legible with: http://morsecode.scphillips.com/jtranslator.html
##      which gives: 0330469983,9780330469982
##      which is the ISBN for Into The Wild by Jon Krakauer   