
class Sifreleme:

#Sifreleme Sinifi nin sifreCozme fonk yapilacak

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
                  "I":"9",
                  "i":"77",
                  "J":"41",
                  "j":"32",
                  "K":"44",
                  "k":"63",
                  "L":"7",
                  "l":"96",
                  "M":"87",
                  "m":"95",
                  "N":"2",
                  "n":"17",
                  "O":"29",
                  "o":"47",
                  "P":"6",
                  "p":"67",
                  "R":"83",
                  "r":"79",
                  "S":"19",
                  "s":"37",
                  "T":"23",
                  "t":"62",
                  "U":"43",
                  "u":"3",
                  "V":"13",
                  "v":"24",
                  "Q":"57",
                  "q":"85",
                  "W":"49",
                  "w":"97",
                  "X":"51",
                  "x":"82",
                  "Y":"91",
                  "y":"73",
                  "Z":"5",
                  "z":"55",
                  "*":"33"}
        for karakter in kripto:
            kripcevir = kripcevir.replace(karakter,kripto[karakter])
        return kripcevir

    def desifre(kripcoz):
        kriptoCoz = {}
        for karakter in kriptoCoz:
            kripcoz = kripcoz.replace(karakter,kriptoCoz[karakter])
        return kripcevir
