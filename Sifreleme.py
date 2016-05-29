import re
class Sifreleme:

#TAMAMLANDI

    def sifrele (kripcevir):
        kripto = {"A":"D",
                  "a":"b",
                  "B":"H",
                  "b":"l",
                  "C":"T",
                  "c":"j",
                  "D":"X",
                  "d":"c",
                  "E":"V",
                  "e":"z",
                  "F":"A",
                  "f":"v",
                  "G":"J",
                  "g":"y",
                  "H":"O",
                  "h":"p",
                  "I":"R",
                  "i":"a",
                  "J":"U",
                  "j":"f",
                  "K":"Z",
                  "k":"t",
                  "L":"M",
                  "l":"r",
                  "M":"B",
                  "m":"d",
                  "N":"F",
                  "n":"q",
                  "O":"W",
                  "o":"s",
                  "P":"C",
                  "p":"g",
                  "R":"I",
                  "r":"e",
                  "S":"Q",
                  "s":"w",
                  "T":"N",
                  "t":"x",
                  "U":"Y",
                  "u":"m",
                  "V":"P",
                  "v":"o",
                  "Q":"E",
                  "q":"h",
                  "W":"S",
                  "w":"n",
                  "X":"L",
                  "x":"k",
                  "Y":"K",
                  "y":"i",
                  "Z":"G",
                  "z":"u",
                  " ":" "}
        rc = re.compile('|'.join(map(re.escape, kripto)))

        def translate(match):
            return kripto[match.group(0)]

        return rc.sub(translate, kripcevir)

    def desifre(kripcoz):
        kriptoCoz = {"D":"A",
                  "b":"a",
                  "H":"B",
                  "l":"b",
                  "T":"C",
                  "j":"c",
                  "X":"D",
                  "c":"d",
                  "V":"E",
                  "z":"e",
                  "A":"F",
                  "v":"f",
                  "J":"G",
                  "y":"g",
                  "O":"H",
                  "p":"h",
                  "R":"I",
                  "a":"i",
                  "U":"J",
                  "f":"j",
                  "Z":"K",
                  "t":"k",
                  "M":"L",
                  "r":"l",
                  "B":"M",
                  "d":"m",
                  "F":"N",
                  "q":"n",
                  "W":"O",
                  "s":"o",
                  "C":"P",
                  "g":"p",
                  "I":"R",
                  "e":"r",
                  "Q":"S",
                  "w":"s",
                  "N":"T",
                  "x":"t",
                  "Y":"U",
                  "m":"u",
                  "P":"V",
                  "o":"v",
                  "E":"Q",
                  "h":"q",
                  "S":"W",
                  "n":"w",
                  "L":"X",
                  "k":"x",
                  "K":"Y",
                  "i":"y",
                  "G":"Z",
                  "u":"z",
                  " ":" "}
        #for karakter in kriptoCoz:
        #    kripcoz = kripcoz.replace(karakter,kriptoCoz[karakter])
        #return  kripcoz
        rc = re.compile('|'.join(map(re.escape, kriptoCoz)))

        def translate(match):
            return kriptoCoz[match.group(0)]

        return rc.sub(translate, kripcoz)

