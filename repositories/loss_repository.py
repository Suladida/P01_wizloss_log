from db.run_sql import run_sql

from models.loss import Loss
from models.item import Item
from models.wizard import Wizard
import repositories.loss_repository as loss_repo
import repositories.item_repository as item_repo
import repositories.wizard_repository as wiz_repo

# CREATE:
# save function goes here
def save(loss):
    sql = "INSERT INTO losses (day, month, year, details, wizard_id, item_id, recovered) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [loss.day, loss.month, loss.year, loss.details, loss.wizard.id, loss.item.id, loss.recovered]
    results = run_sql(sql, values)
    id = results[0]['id']
    loss.id = id
    return loss

# READ_ALL:
# select_all function goes here
def select_all():
    losses = []

    sql = "SELECT * FROM losses"
    results = run_sql(sql)

    for row in results:
        wizard = wiz_repo.select(row['wizard_id'])
        item = item_repo.select(row['item_id'])
        loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
        losses.append(loss)
    return losses

# READ:
# select function goes here
def select(id):
    loss = None
    sql = "SELECT * FROM losses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        wizard = wiz_repo.select(result['wizard_id'])
        item = item_repo.select(result['spell_id'])
        loss = Loss(result['day'], result['month'], result['year'], result['details'], wizard, item, result['recovered'], result['id'] )
    return loss

# UPDATE:
# - update function goes here
def update(loss):
    sql = "UPDATE casts SET (day, month, year, details, wizard_id, item_id, recovered) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [loss.day, loss.month, loss.year, loss.details, loss.wizard.id, loss.item.id, loss.recovered]
    run_sql(sql, values)
    print(f"✅ Cast Updated: {loss.day} {loss.month} {loss.year} {loss.details} {loss.wizard.id} {loss.item.id} {loss.recovered}")

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM losses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM losses"
    run_sql(sql)

# READ_ALL:
# select_all function goes here
def active_losses():
    losses = []

    sql = "SELECT * FROM losses where recovered = False"
    results = run_sql(sql)

    for row in results:
        wizard = wiz_repo.select(row['wizard_id'])
        item = item_repo.select(row['item_id'])
        loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
        losses.append(loss)
        print(f"🧙‍♂️ Success! {item.id} {item.type} {item.colour} {item.style}") 
    return losses

# checks if a wizard owns an item

def check_wizard_owns_item(wizard, item):
    # loss = None
    sql = "SELECT * FROM losses WHERE wizard_id = %s AND item_id = %s"
    values = [wizard.id, item.id]
    result = run_sql(sql, values)[0]

    if result is not None:
        print(f"🧙‍♂️ WIZARD {wizard.first_name} {wizard.last_name} OWNS ITEM {item.colour} {item.type} {item.style}") 
        return True


# # # checks wizard current losses
# def current_losses(wizard):
#     losses = []
#     sql = "SELECT FROM losses WHERE wizard_id = %s AND recovered = %s"
#     values = [wizard.id, False]
#     results = run_sql(sql, values)

#     for row in results:
#         # # wizard = wiz_repo.select(row['wizard_id'])
#         # wizard = loss.wizard.id
#         # item = item.id
#         item = item_repo.select(row['item_id'])
#         loss = Loss(row['day'], row['month'], row['year'], row['details'], row['wizard'], row['item'], row['recovered'], row['id'] )
#         # loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
#         losses.append(loss)
#         print(f"🧙‍♂️ Success! {item.id} {item.type} {item.colour} {item.style}") 
#     return losses


# def current_losses(wizard):
#     losses = []
#     sql = "SELECT FROM losses WHERE wizard_id = %s AND recovered = False"
#     values = [wizard.id]
#     results = run_sql(sql, values)

#     for row in results:
#         # wizard = wiz_repo.select(row['id'])
#         # wizard = loss.wizard.id
#         # item = item.id
#         # item = item_repo.select(row['item_id'])
#         loss = Loss(row['day'], row['month'], row['year'], row['details'], row['wizard'], row['item'], row['recovered'], row['id'] )
#         # loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
#         losses.append(loss)
#         print(f"🧙‍♂️ Success! {item.id} {item.type} {item.colour} {item.style}") 
#     return losses

def current_losses(wizard):
    losses = []

    sql = "SELECT * FROM losses where wizard_id = %s AND recovered = False"
    values = [wizard.id]
    results = run_sql(sql, values)

    for row in results:
        wizard = wiz_repo.select(row['wizard_id'])
        item = item_repo.select(row['item_id'])
        loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
        losses.append(loss)
        print(f"🧙‍♂️ Oh Dear! {wizard.first_name} {wizard.last_name} HAS LOST {item.colour}{item.type}{item.style}") 
    return losses

def wizard_loss_history(wizard):
    history = []

    sql = "SELECT * FROM losses where wizard_id = %s AND recovered = True"
    values = [wizard.id]
    results = run_sql(sql, values)

    for row in results:
        wizard = wiz_repo.select(row['wizard_id'])
        item = item_repo.select(row['item_id'])
        loss = Loss(row['day'], row['month'], row['year'], row['details'], wizard, item, row['recovered'], row['id'] )
        history.append(loss)
        print(f"🧙‍♂️ WIZARD: {wizard.first_name} {wizard.last_name} LOST ITEM: {item.colour}{item.type}{item.style} DATE: {loss.day}{loss.month}{loss.year}") 
    return history


    




# # checks if item is lost

# def check_item_status(item):
# For loss in losses:
# if loss.item = item.id
# AND loss.recovered = False:
# return False
# Else: 
# return True

# # marks item as recovered 

# def mark_recovered(item):
# result = check_item_status(item)
# return result

# # checks if a wizard owns an item and it's not lost (i.e. current inventory)

# def wizard_inventory(wizard, item):
# inventory = []
# ### checks if wizard owns item
# owned = check_wizard_owns_item(wizard, item)
# ### checks if item is NOT lost
# status = check_item_status(item)
# For item in inventory:
# If owned = true and status = true: 
# inventory.append(item)
# return inventory
