def accounts_merge(accounts):
    store = {}
    res = []
    for each in accounts:
        if each[0] not in store:
            store[each[0]] = set(each[1:])
        else:
            for mail in each[1:]:
                if mail not in store[each[0]]:
                    store[each[0]].add(mail)
    for name, emails in store.items():
        res.append([name] + sorted(emails))
    return res



accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accounts_merge(accounts))