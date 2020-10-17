import urllib.request
import json
urlT = 'http://www.protezionecivilepop.tk/allerte?citta=060038&rischio=temporali&allerta=verde&giorno=domani&formato=json'
urlI = 'http://www.protezionecivilepop.tk/allerte?citta=060038&rischio=idraulico&allerta=verde&giorno=domani&formato=json'
urlG = 'http://www.protezionecivilepop.tk/allerte?citta=060038&rischio=idrogeologico&allerta=verde&giorno=domani&formato=json'

reqT = urllib.request.Request(urlT)
reqI = urllib.request.Request(urlI)
reqG = urllib.request.Request(urlG)

##parsing response
r = urllib.request.urlopen(reqI).read()
previsioneT = json.loads(r.decode('utf-8'))
r = urllib.request.urlopen(reqT).read()
previsioneI = json.loads(r.decode('utf-8'))
r = urllib.request.urlopen(reqG).read()
previsioneG = json.loads(r.decode('utf-8'))

##parsing json
print("Livello allerta comune di Frosinone:")
print("Rischio Temporali:", previsioneT['previsione']['alert'])
print("Rischio Idraulico:", previsioneI['previsione']['alert'])
print("Rischio Idrogeologico:", previsioneG['previsione']['alert'])
print("----")