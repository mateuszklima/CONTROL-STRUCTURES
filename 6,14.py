facebook = input('czy masz facebooka (T/N):').upper() =="T"
twitter = input('czy masz twittera (T/N):').upper() =="T"
instagram = input('czy masz instagrama (T/N):').upper() =="T"

accounts_count = facebook + twitter + instagram

if accounts_count >= 2:
    print('jestes dobrym inlfu!')
else:
    print('nie jestes dobrym infu!')