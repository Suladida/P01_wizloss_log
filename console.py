import pdb
from models.wizard import Wizard
from models.item import Item
from models.loss import Loss

wizard1 = Wizard("Gandalferoo", "Frillywhiskers", 2000)
wizard2 = Wizard("Merlin", "Magicpants", 1000)
wizard3 = Wizard("Parry", "Hotter", 22)

hat1 = Item(wizard1, "Hat", "Grey", "Standard; rounded point")
hat2 = Item(wizard2, "Hat", "Blue and Yellow", "Standard; sharp point")
hat3 = Item(wizard3, "Hat", "Black", "Baseball cap with a lightning bolt")
shoes1 = Item(wizard1, "Shoes", "Red and Black", "Jordan Air's")
shoes2 = Item(wizard2, "Shoes", "Blue", "Curly Pointed Slippers")
shoes3 = Item(wizard3, "Shoes", "Black", "90s Platform Trainers")
wand1 = Item(wizard1, "Wand", "Light brown", "Knobbly")
wand2 = Item(wizard2, "Wand", "Black", "Straight, smooth")
wand3 = Item(wizard3, "Wand", "Brown", "Zig-zagged")


# loss1 = Loss("", "", "", "", "", "")
# loss2 = Loss("", "", "", "", "", "")
# loss3 = Loss("", "", "", "", "", "")
# loss4 = Loss("", "", "", "", "", "")
# loss5 = Loss("", "", "", "", "", "")
# loss6 = Loss("", "", "", "", "", "")
# loss7 = Loss("", "", "", "", "", "")

pdb.set_trace()