from db.run_sql import run_sql
from models.item import Item
import repositories.item_repository as item_repo
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

# (type, colour, style, wizard_id) VALUES (%s, %s, %s, %s)
# wizard = wiz_repo.select(row['wizard_id'])
# item = Item(result['type'], result['colour'], result['style'], wizard, result['id'] )

# CREATE:
# save function goes here
def save(item):
    sql = "INSERT INTO items (type, colour, style, wizard_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [item.type, item.colour, item.style, item.wizard.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    item.id = id
    return item

# READ_ALL:
# select_all function goes here
def select_all():
    items = []

    sql = "SELECT * FROM items"
    results = run_sql(sql)

    for row in results:
        wizard = wiz_repo.select(row['wizard_id'])
        item = Item(row['type'], row['colour'], row['style'], wizard, row['id'] )
        items.append(item)
    return items

# READ:
# select function goes here
def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        wizard = wiz_repo.select(result['wizard_id'])
        item = Item(result['type'], result['colour'], result['style'], wizard, result['id'] )
    return item

# UPDATE:
# - update function goes here
def update(item):
    sql = "UPDATE items SET (type, colour, style, wizard_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [item.type, item.colour, item.style, item.wizard.id]
    run_sql(sql, values)
    print(f"✅ Item Updated: {item.type} {item.colour} {item.style} {item.wizard.id} {item.id}")

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)
