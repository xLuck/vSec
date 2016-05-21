
class Sifreleme:

#TAMAMLANDI

    def sifrele (kripcevir):
        kripto = {"A":"11",
                  "a":"24",
                  "B":"52",
                  "b":"53",
                  "C":"59",
                  "c":"54",
                  "D":"12",
                  "d":"89",
                  "E":"22",
                  "e":"69",
                  "F":"71",
                  "f":"35",
                  "G":"38",
                  "g":"93",
                  "H":"72",
                  "h":"61",
                  "I":"99",
                  "i":"77",
                  "J":"41",
                  "j":"32",
                  "K":"44",
                  "k":"63",
                  "L":"78",
                  "l":"96",
                  "M":"87",
                  "m":"95",
                  "N":"26",
                  "n":"17",
                  "O":"29",
                  "o":"47",
                  "P":"65",
                  "p":"67",
                  "R":"83",
                  "r":"79",
                  "S":"19",
                  "s":"37",
                  "T":"23",
                  "t":"62",
                  "U":"43",
                  "u":"39",
                  "V":"13",
                  "v":"68",
                  "Q":"57",
                  "q":"85",
                  "W":"49",
                  "w":"97",
                  "X":"51",
                  "x":"82",
                  "Y":"91",
                  "y":"73",
                  "Z":"56",
                  "z":"55",
                  " ":"33"}
        for karakter in kripto:
            kripcevir = kripcevir.replace(karakter,kripto[karakter])
        return kripcevir

    def desifre(kripcoz):
        kriptoCoz = {"11":"A",
                  "24":"a",
                  "52":"B",
                  "53":"b",
                  "59":"C",
                  "54":"c",
                  "12":"D",
                  "89":"d",
                  "22":"E",
                  "69":"e",
                  "71":"F",
                  "35":"f",
                  "38":"G",
                  "93":"g",
                  "72":"H",
                  "61":"h",
                  "99":"I",
                  "77":"i",
                  "41":"J",
                  "32":"j",
                  "44":"K",
                  "63":"k",
                  "78":"L",
                  "96":"l",
                  "87":"M",
                  "95":"m",
                  "26":"N",
                  "17":"n",
                  "29":"O",
                  "47":"o",
                  "65":"P",
                  "67":"p",
                  "83":"R",
                  "79":"r",
                  "19":"S",
                  "37":"s",
                  "23":"T",
                  "62":"t",
                  "43":"U",
                  "39":"u",
                  "13":"V",
                  "68":"v",
                  "57":"Q",
                  "85":"q",
                  "49":"W",
                  "97":"w",
                  "51":"X",
                  "82":"x",
                  "91":"Y",
                  "73":"y",
                  "56":"Z",
                  "55":"z",
                  "33":" "}
        for karakter in kriptoCoz:
            kripcoz = kripcoz.replace(karakter,kriptoCoz[karakter])
        return kripcoz
