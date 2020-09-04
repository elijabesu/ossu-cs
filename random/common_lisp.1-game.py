import sys

class Game:
    health = 0
    level = 0

    def get_health(self):
        return self.health

    def set_health(self, value):
        if not isinstance(value, int):
            sys.exit("Variable health must be a number.")
        self.health = value

    def get_level(self):
        return self.level

    def set_level(self, value):
        if not isinstance(value, int):
            sys.exit("Variable level must be a number.")
        self.level = value

    def next_step(self, option):
        if (not isinstance(option, int)) and (option != 1 or option != 2):
            sys.exit("Option can only be 1 or 2.")
        level = self.get_level
        health = self.get_health
        opt1 = options[1]
        opt2 = options[2]
        opt_obe = options[3]
        minus = options[4]
        co_dal = options[5]
        vyber = options[6]
        if level == 0:
            self.set_health(health - 1)
            if option == 1:
                

game = Game()

def start():
    global game
    game.set_health(3)
    game.set_level(0)
    print(options[0].format(game.get_health(), options[2], options[3]))

def choose(option):
    global game
    game.next_step(option)

options = [
    """Stojite v arene s jednim dalsim protivnikem, ktery ma stejne moznosti jako vy. Mate {0} zivoty. {1}

1. Rozbehnete se na pravou stranu pro nuz.
2. Rozbehnete se proti nemu.

{2}""", # 0
#(list
#"~A ~A Mate ~D zivoty. ~A\n\n1. Zvednete se a popadnete nuz.\n2. Rozbehnete se a zkusite
#ziskat nejaky naskok.\n\n~A\n" ; 1
#"Protivnik se priblizil dostatecne a nozem vas rizl do ramene vasi dominantni ruky. ~A
#Mate ~D zivot. ~A\n\n1. Zvednete nuz v druhe ruce a bodnete ho. \n2. Vzdalite se a chytnete
#si ranu, abyste neztratili moc krve.\n\n~A\n" ; 11
#"Rychle ztracite krev. Zacne se vam tocit hlava a vy se zhroutite k zemi. Nevstavate
#dostatecne dlouho, abyste byly prohlaseni porazenymi...\n\nKONEC HRY"; 112 ----- KONEC HRY
#)
#(list
#"~A ~A Mate ~D zivoty. ~A\n\n1. Zvednete se a priblizite se k nemu, nasledne jej
#kopnete.\n2. Rozbehnete se a zkusite ziskat nejaky naskok.\n\n~A\n" ; 2
#
#"Kopli jste ho do citliveho mista, protivnik se zhroutil k zemi v bolestnych krecich.
#Nevstava dostatecne dlouho, abyste byli prohlaseni vitezem. Gratuluji!\n\nKONEC HRY" ; 21
#----- KONEC HRY
#)
#(list
#"Zakopnete o kamen, ktery vam lezel v ceste. Protivnik mezi tim ziskal nuz a rychle se
#blizi k vam." ; zacatek 1 a 2
#"Vas protivnik je velmi pomaly a vy jste ziskali dostatecny naskok. Mate ~D zivoty.
#~A\n\n1. Popadnete nuz a pobezite k nemu, nasledne protivnika bodnete.\n2. Pokracujete v behu
#dokud se neunavi.\n\n~A\n" ; 12 a 22
#"Bodli jste ho do citliveho mista, protivnik se zhroutil k zemi v bolestnych krecich.
#Nevstava dostatecne dlouho, abyste byli prohlaseni vitezem. Gratuluji!\n\nKONEC HRY"; 121 a
#221 a 111 ----- KONEC HRY
#"Po nejake chvili se protivnik unavi a zastavi. Mate ~D zivoty. ~A\n\n1. Priblizite se k
#nemu a kopnete ho.\n2. Cekate dokud zcela nepolozi svuj nuz.\n\n~A\n"; 122 a 222
#"Kdyz jste se priblizili, zvedl se a nasledne vas rizl. ~A Mate ~D zivoty. ~A\n\n1.
#Zacnete znovu utikat.\n2. Rychle ho kopnete znovu." ; 1221 a 2221
#"Po dalsi chvili polozi svuj nuz a lehne si ve vycerpani. Nevstava dostatecne dlouho,
#abyste byli prohlaseni vitezem. Gratuluji!\n\nKONEC HRY" ; 1222 a 2222 ----- KONEC HRY
#"Protivnik zacne za vami utikat, ale po kratke chvili se unavi dostatecne na to, aby si
#lehl. Nevstava dostatecne dlouho, abyste byli prohlaseni vitezem. Gratuluji!\n\nKONEC HRY";
#12211 A 2221 ----- KONEC HRY
#)
"Ztratili jste 1 zivot.",
"Co udelate?",
"Vyberte moznost X pouzitim (choose X)."]

start()
choose(1)