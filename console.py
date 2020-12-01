import pdb
from models.wizard import Wizard
from models.item import Item
from models.loss import Loss
import repositories.item_repository as item_repo
import repositories.wizard_repository as wiz_repo
import repositories.loss_repository as loss_repo

wizard1 = Wizard("Gandalferoo", "Frillywhiskers", 2000)
wizard2 = Wizard("Merlin", "Magicpants", 1000)
wizard3 = Wizard("Parry", "Hotter", 22)

hat1 = Item("Hat", "Grey", "Standard; rounded point", wizard1)
hat2 = Item("Hat", "Blue and Yellow", "Standard; sharp point", wizard2)
hat3 = Item("Hat", "Black", "Baseball cap with a lightning bolt", wizard3)
shoes1 = Item("Shoes", "Red and Black", "Jordan Air's", wizard1)
shoes2 = Item("Shoes", "Blue", "Curly Pointed Slippers", wizard2)
shoes3 = Item("Shoes", "Black", "90s Platform Trainers", wizard3)
wand1 = Item("Wand", "Light brown", "Knobbly", wizard1)
wand2 = Item("Wand", "Black", "Straight, smooth", wizard2)
wand3 = Item("Wand", "Brown", "Zig-zagged", wizard3)

# date, time, details, wizard_id, item_id, recovered = False
loss1 = Loss(2020-1-1, "Lost at event at Gimli's Nightclub", wizard1, hat1)
loss2 = Loss(2019- 3-4, "Lost in forest (name unknown)", wizard2, hat2)
loss3 = Loss(2018-6-7, "Woke up without it on the bus this morning", wizard3, wand3)
loss4 = Loss(2019-8-3, "No memory of loss", wizard1, shoes1)
# loss5 = Loss("", "", "", "", "", "")
# loss6 = Loss("", "", "", "", "", "")
# loss7 = Loss("", "", "", "", "", "")

pdb.set_trace()