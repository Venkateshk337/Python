n = int(input("Enter the number of men/women: "))
men_prefs = {}
women_prefs = {}

print("Enter men's preferences:")
for i in range(n):
    man = input(f"Enter name of man {i + 1}: ")
    prefs = input(f"Enter {man}'s preferences (space separated): ").split()
    men_prefs[man] = prefs

print("Enter women's preferences:")
for i in range(n):
    woman = input(f"Enter name of woman {i + 1}: ")
    prefs = input(f"Enter {woman}'s preferences (space separated): ").split()
    women_prefs[woman] = prefs


def stable_match(me_pres, wo_prefs):
    men_list = list(me_pres.keys())

    engagement = {}

    while men_list:
        men = men_list.pop(0)
        women = me_pres[men]
        eng = women.pop(0)
        fiance = engagement.get(eng)
        if not fiance:
            engagement[eng] = men
        elif wo_prefs[eng].index(men) < wo_prefs[eng].index(fiance):
            engagement[eng] = men
            men_list.append(fiance)
        else:
            men_list.append(men)
    return engagement


stableMatches = stable_match(men_prefs, women_prefs)
print("Stable Marriages:")
for woman, man in stableMatches.items():
    print(f"{man} engaged to {woman}")
