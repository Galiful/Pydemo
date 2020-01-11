data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
update = ','.join(["{key} = % s".format(key=key) for key in data])
print(update)