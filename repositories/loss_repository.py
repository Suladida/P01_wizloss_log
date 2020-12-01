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
    print(f"✅ Cast Updated: {loss.date} {loss.details} {loss.wizard.id} {loss.item.id} {loss.recovered}")

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