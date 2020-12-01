import pdb
from models.wizard import Wizard
from models.item import Item
from models.loss import Loss
import repositories.wizard_repository as wiz_repo
import repositories.item_repository as item_repo
import repositories.loss_repository as loss_repo

loss_repo.delete_all()
item_repo.delete_all()
wiz_repo.delete_all()

wizard1 = Wizard("Gandalferoo", "Frillywhiskers", 2000)
wiz_repo.save(wizard1)
wizard2 = Wizard("Merlin", "Magicpants", 1000)
wiz_repo.save(wizard2)
wizard3 = Wizard("Parry", "Hotter", 22)
wiz_repo.save(wizard3)

hat1 = Item("Hat", "Grey", "Standard; rounded point", wizard1)
item_repo.save(hat1)
hat2 = Item("Hat", "Blue and Yellow", "Standard; sharp point", wizard2)
item_repo.save(hat2)
hat3 = Item("Hat", "Black", "Baseball cap with a lightning bolt", wizard3)
item_repo.save(hat3)
shoes1 = Item("Shoes", "Red and Black", "Jordan Air's", wizard1)
item_repo.save(shoes1)
shoes2 = Item("Shoes", "Blue", "Curly Pointed Slippers", wizard2)
item_repo.save(shoes1)
shoes3 = Item("Shoes", "Black", "90s Platform Trainers", wizard3)
item_repo.save(shoes1)
wand1 = Item("Wand", "Light brown", "Knobbly", wizard1)
item_repo.save(wand1)
wand2 = Item("Wand", "Black", "Straight, smooth", wizard2)
item_repo.save(wand2)
wand3 = Item("Wand", "Brown", "Zig-zagged", wizard3)
item_repo.save(wand3)

# day, month, year, details, wizard_id, item_id, recovered
loss1 = Loss("01","01","2020", "Lost at event at Gimli's Nightclub", wizard1, hat1)
loss_repo.save(loss1)
loss2 = Loss("04","03","2019", "Lost in forest (name unknown)", wizard2, hat2)
loss_repo.save(loss2)
loss3 = Loss("07","07","2019", "Woke up without it on the bus this morning", wizard3, wand3)
loss_repo.save(loss3)
loss4 = Loss("03", "07", "2019", "No memory of loss", wizard1, shoes1)
loss_repo.save(loss4)
# loss5 = Loss("", "", "", "", "", "")
# loss6 = Loss("", "", "", "", "", "")
# loss7 = Loss("", "", "", "", "", "")

wizards = wiz_repo.select_all()
items = item_repo.select_all()
losses = loss_repo.select_all()

pdb.set_trace()