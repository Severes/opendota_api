from pprint import pprint
from main.opendotaclass import OpenDota as OD
import config.config as cc

# print(OpenDota.teams.__doc__)
# print(OpenDota.uni_request.__doc__)

# a = OpenDota().teams(cc.dark_phoenixes)
# pprint(a)

# b = OpenDota().uni_request('explorer', {'sql': 'select * from teams where team_id = 683037'})
# pprint(b)

# c = OpenDota().uni_request('search', {'q': cc.lol_what_name})
# pprint(c)

# d = OpenDota().uni_request('leagues')
# pprint(d)

# e = OpenDota().players(cc.lol_what_id, 'recentMatches')
# pprint(e)

# f = OpenDota().constants()
# pprint(f)

# g = OpenDota().uni_request('schema')
# pprint(g)

# h = OpenDota().uni_request('explorer', {'sql': 'select * from leagues where leagueid = 2733'})
# pprint(h)

i = OD().explorer('select * from leagues where leagueid = 2733')
pprint(i)