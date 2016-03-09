
class Sifreleme:

#Karakterler Arttirilacak
    def sifrele (kripcevir):
        kripto = {"V":"11","v":"24","*":"33"}
        for karakter in kripto:
            kripcevir = kripcevir.replace(karakter,kripto[karakter])
        return kripcevir


