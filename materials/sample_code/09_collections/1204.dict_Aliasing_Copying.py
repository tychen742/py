opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)   # is checks objects and == checks value

alias['right'] = 'left'
print(opposites['right'])

acopy = opposites.copy()
acopy['right'] = 'wrong'
print(acopy['right'])
print(opposites['right'])