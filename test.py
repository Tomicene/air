db = {
    'Bode001': '12345',
    'Tomicene': 'a1234b',
    'NIIT' : 'pass123'
}
def up():
    for user in db.keys():
        db[user.upper()]=db.pop(user)
        
up()
print(db)
