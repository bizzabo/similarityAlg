import math
import pandas as pd




data3 ={
    'Lior Plis': {
		'Role': 1.0,
		'Age':0.25,
		'Experience': 3.34,
		'Industry': 2.32
	},
	'Jhonny Per': {
        'Role': 2.0,
        'Age': 0.36,
        'Experience': 2.1,
        'Industry': 3.0,
        'flow':1
    },
	'Itamr Ret': {
        'Role': 3.0,
        'Age': 0.45,
        'Experience': 3.2,
        'Industry': 1.32,
        'flow': 4

    },
	'Tamir Der': {
        'Role': 2.0,
        'Age': 0.30,
        'Experience': 3.88,
        'Industry': 2.55,
        'flow': 4

    },
	'Tamir2 Der2': {
        'Role': 2.0,
        'Age':0.50,
        'Experience': 3.88,
        'Industry': 2.55,
        'flow': 5
    },
	'Marvin Minsky': {
		'Role': 5.0,
		'Age': 0.23,
		'Experience': 4.32,
		'Industry': 2.76,
        'flow': 4
	},
    'John McCarthy': {
		'Role': 3.0,
		'Age': 0.58,
		'Experience': 3.23,
		'Industry': 3.03,
        'flow': 4
	},
    'Edsger Dijkstra': {
		'Role': 5.0,
		'Age': 0.52,
		'Experience': 3.04,
		'Industry': 4.97,
		'flow': 5

	},

	'Donald Knuth': {
		'Role': 1.0,
		'Age': 0.52,
		'Experience': 5.0,
		'Industry': 1.97,
		'flow': 4
	},
    'John Backus': {
		'Role': 5.0,
		'Age': 0.40,
		'Experience': 4.3,
		'Industry': 3.2,
		'flow': 3
	},

	'Robert Floyd': {
		'Role': 4.0,
		'Age': 0.56,
		'Experience': 4.04,
		'Industry': 3.97,
        'flow': 2
	},

	'Tony Hoare': {
		'Role': 4.0,
		'Age': 0.28,
		'Experience': 4.2,
		'Industry': 3.07,
        'flow': 3
	},
}




def euclidean_similarity(person1, person2):
    data = data3
    common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
    rankings = [(data[person1][itm], data[person2][itm]) for itm in common_ranked_items]
    distance = [pow(rank[0] - rank[1], 2) for rank in rankings]
    return 1 / (1 + sum(distance))

def pearson_similarity(person1, person2):
    data = data3
    common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
    n = len(common_ranked_items)
    s1 = sum([data[person1][item] for item in common_ranked_items])
    s2 = sum([data[person2][item] for item in common_ranked_items])

    ss1 = sum([pow(data[person1][item], 2) for item in common_ranked_items])
    ss2 = sum([pow(data[person2][item], 2) for item in common_ranked_items])

    ps = sum([data[person1][item] * data[person2][item] for item in common_ranked_items])

    num = n * ps - (s1 * s2)

    den = math.sqrt((n * ss1 - math.pow(s1, 2)) * (n * ss2 - math.pow(s2, 2)))

    return (num / den) if den != 0 else 0


def recommend(person,personObj, bound, similarity=pearson_similarity):
    data = data3
    data[person] = personObj
    scores = [(similarity(person, other), other) for other in data if other != person]
    scores.sort()
    scores.reverse()
    scores = scores[0:bound]

    print (scores)

    recomms = {}

    for sim, other in scores:
     ranked = data[other]

    for itm in ranked:
            if itm not in data[person]:
                weight = sim * ranked[itm]

                if itm in recomms:
                    s, weights = recomms[itm]
                    recomms[itm] = (s + sim, weights + [weight])
                else:
                    recomms[itm] = (sim, [weight])

    for r in recomms:
        sim, item = recomms[r]
        recomms[r] = sum(item) / sim

    return recomms


# print(recommend('Liora Plisa',{
#                 'Role': 4.36,
#         'Age': 4.0,
#         'Experience': 2.1,
#         'Industry': 3.0,},5,euclidean_similarity))
