class NPITerminals():

    def __init__(self):
        self.terminals = {
            'D': ['the'],
            'SD': ['the', 'some'],
            'IC': ['that'],
            'C': ['that'],
            'MOST': ['most', 'many'],
            'NO': ['no', 'few'],
            'MS': [
                'authors', 'pilots', 'surgeons', 'farmers', 'managers',
                'customers', 'officers', 'teachers', 'senators', 'consultants'
            ],
            'ES': [
                'guards', 'chefs', 'architects', 'skaters', 'dancers',
                'ministers', 'drivers', 'assistants', 'executives', 'parents'
            ],
            'IS': [
                'movies', 'books', 'games', 'songs', 'pictures', 'paintings',
                'novels', 'poems', 'shows'
            ],
            'EV': ['like', 'admire', 'hate', 'love'],
            'PASTAUX': ['have'],
            'FUTAUX': ['will'],
            'NPI': ['ever'],
            'IPMV': [
                'been seen', 'been appreciated', 'been ignored', 'gotten old'
            ],
            'IFMV': ['be seen', 'be appreciated', 'be ignored', 'get old'],
            'APMV': ['been popular', 'been famous', 'had children'],
            'AFMV': ['be popular', 'be famous', 'have children'],
            'MV': [],
            'LMV': []
        }


class AgreementTerminals():

    def __init__(self):
        self.terminals = {
            'D': ['the'],
            'IC': ['that'],
            'C': ['that'],
            'MS': [
                'author', 'pilot', 'surgeon', 'farmer', 'manager', 'customer',
                'officer', 'teacher', 'senator', 'consultant'
            ],
            'ES': [
                'guard', 'chef', 'architect', 'skater', 'dancer', 'minister',
                'taxi driver', 'assistant', 'executive', 'parent'
            ],
            'IS': [
                'movie', 'book', 'game', 'song', 'picture', 'painting', 'novel',
                'poem', 'show'
            ],
            'MV': [
                'laughs', 'swims', 'smiles', 'is tall', 'is old', 'is young',
                'is short'
            ],
            'EV': ['likes', 'admires', 'hates', 'loves'],
            'IV': [
                'is good', 'is bad', 'is new', 'is popular', 'is unpopular',
                'brings joy to people', 'interests people'
            ],
            'P': [
                'next to', 'behind', 'in front of', 'near', 'to the side of',
                'across from'
            ],
            'IP': ['from', 'by'],
            'BS': ['mechanic', 'banker'],
            'BV': ['said', 'thought', 'knew'],
            'AND': ['and'],
            'ANPHR': ['himself', 'herself'],
            'LMV': [
                'knows many different foreign languages',
                'likes to watch television shows', 'is twenty three years old',
                'enjoys playing tennis with colleagues',
                'writes in a journal every day'
            ],
            'RMV': [
                'hurt', 'injured', 'congratulated', 'embarrassed', 'disguised',
                'hated', 'doubted'
            ]
        }


class AgreementTerminals():

    def __init__(self):
        self.terminals = {
            'D': ['the'],
            'IC': ['that'],
            'C': ['that'],
            'MS': [
                'author', 'pilot', 'surgeon', 'farmer', 'manager', 'customer',
                'officer', 'teacher', 'senator', 'consultant'
            ],
            'ES': [
                'guard', 'chef', 'architect', 'skater', 'dancer', 'minister',
                'taxi driver', 'assistant', 'executive', 'parent'
            ],
            'IS': [
                'movie', 'book', 'game', 'song', 'picture', 'painting', 'novel',
                'poem', 'show'
            ],
            'MV': ['is tall', 'is old', 'is young', 'is short'],
            'EV': ['likes', 'admires', 'hates', 'loves'],
            'IV': [
                'is good', 'is bad', 'is new', 'is popular', 'is unpopular',
                'brings joy to people', 'interests people'
            ],
            'P': [
                'next to', 'behind', 'in front of', 'near', 'to the side of',
                'across from'
            ],
            'IP': ['from', 'by'],
            'BS': ['mechanic', 'banker'],
            'BV': ['said', 'thought', 'knew'],
            'AND': ['and'],
            'ANPHR': ['himself', 'herself'],
            'LMV': [
                'knows many different foreign languages',
                'likes to watch television shows', 'is twenty three years old',
                'enjoys playing tennis with colleagues',
                'writes in a journal every day'
            ],
            'RMV': [
                'hurt', 'injured', 'congratulated', 'embarrassed', 'disguised',
                'hated', 'doubted'
            ]
        }


# class AgreementTerminals():

#     def __init__(self):
#         self.terminals = {
#             'D': ['the'],
#             'IC': ['that'],
#             'C': ['that'],
#             'MS': [
#                 'author', 'pilot', 'surgeon', 'farmer', 'manager', 'customer',
#                 'officer', 'teacher', 'senator', 'consultant'
#             ],
#             'ES': [
#                 'guard', 'chef', 'architect', 'skater', 'dancer', 'minister',
#                 'taxi driver', 'assistant', 'executive', 'parent'
#             ],
#             'IS': [
#                 'movie', 'book', 'game', 'song', 'picture', 'painting', 'novel',
#                 'poem', 'show'
#             ],
#             'MV': [
#                 'laughs', 'smiles', 'agrees', 'arrives', 'dies', 'disappears',
#                 'exists', 'jumps', 'knocks', 'learns', 'leans', 'asks', 'grows',
#                 'falls', 'lies', 'lives', 'looks', 'moves', 'reads', 'responds',
#                 'runs', 'screams', 'shakes', 'shouts', 'sighs', 'sits',
#                 'sleeps', 'smells', 'stands', 'stays', 'walks', 'waves',
#                 'works', 'yells'
#             ],
# 'EV': [
#     'likes', 'hates', 'loves', 'owes', 'leaves', 'offers', 'pays',
#     'promises', 'refuses', 'tells', 'writes', 'hurts', 'kills',
#     'praises', 'hugs', 'holds', 'feeds', 'draws', 'hears', 'begs',
#     'tricks'
# ],
#             'IV': [
#                 'is good', 'is bad', 'is new', 'is popular', 'is unpopular',
#                 'interests me', 'interests him', 'looks good', 'looks bad',
#                 'looks popular'
#             ],
#             'P': [
#                 'next to', 'behind', 'in front of', 'near', 'to the side of',
#                 'across from'
#             ],
#             'IP': ['from', 'by'],
#             'BS': ['mechanic', 'banker'],
#             'BV': ['said', 'thought', 'knew'],
#             'AND': ['and'],
#             'ANPHR': ['himself', 'herself'],
#             'LMV': [
#                 'knows many different foreign languages',
#                 'likes to watch television shows', 'is twenty three years old',
#                 'enjoys playing tennis with colleagues',
#                 'writes in a journal every day'
#             ],
#             'RMV': [
#                 'hurt', 'injured', 'congratulated', 'embarrassed', 'disguised',
#                 'hated', 'doubted'
#             ]
#         }
