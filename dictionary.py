game_user_profile={'age': 55, 'username': 'rohith__1634', 'weapons' : 'm24', 'is_active' : 'yes','clan':'yes'}

print(game_user_profile.keys())

game_user_profile.update({'is_banned' : True})

print(game_user_profile)

dummy=game_user_profile.copy()

dummy.update({'age':41,'username':'skdosh14'})
print(dummy)

#for i,j in game_user_profile.items():
#    print(f'{i} is {j}')

