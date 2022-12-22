users = [ {
    'username': 'ananta',
    'password': 'rain',
    'role': 'admin'
},

{
    'username': 'shakib',
    'password': 'bubli',
    'role': 'contributor'
},]

for user in users:
    print(user.get('username'))