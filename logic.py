import math




industryMap = {
    'MARKETING_AND_ADVERTISING': 1,
    'INTERNET': 2,
    'EDUCATION_MANAGEMENT': 3,
    'COMPUTER_SOFTWARE': 4,
    'BANKING': 5
}
roleMap = {
    'ContentManagerFlow': 0,
    'Designer': 1,
    'RegistrationManager': 2,
    'ContactManager': 3,
    'Admin': 4,
    'Marketer': 5,
    'Generic': 6
}


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

def replace_models_data(model_dict):
    index = 0
    result = model_dict
    for key in model_dict:
        result[key] = keyToValue(key, model_dict[key])
        index += 1

    return result


def keyToValue(key, value):
    if (key == 'Role'):
        return roleMap[value]
    if (key == 'Age'):
        return value / 100
    if (key == 'Experience'):
        return value / 100
    if (key == 'Industry'):
        return industryMap[value]

def recommend(person,dataObj, bound, similarity=pearson_similarity):
    personObj = replace_models_data(dataObj)
    data = data3
    data[person] = personObj
    scores = [(similarity(person, other), other) for other in data if other != person]
    scores.sort()
    scores.reverse()
    scores = scores[0:bound]

    #print (scores)

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

    t=flowMap[(str(int(recomms['flow'])))],recomms['flow']
    return t


x={
"Role": 'Marketer',
"Age":30,
"Experience": 5,
"Industry": 'MARKETING_AND_ADVERTISING'
}

flowMap = {
    # Content Manager flow
    '1':
        ['https://accounts.bizzabo.com/{accountId}/events/{eventId}/info/general',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/speakers/manage',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/agenda/manageTags',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/agenda/locations',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/agenda/editor',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/registration/sessionRegistration',
          'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/website/settings'],

    # Designer
    '2':
        ['https://accounts.bizzabo.com/preview/{accountId}/events/{eventId}',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/app',
         'https://accounts.bizzabo.com/{accountId}/mobileApp']
    ,

    # Contact/Registration Manager
    '3':
        ['https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/setup/create',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/registration/form',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/registration/confirmation',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/promos'],

    # Admin
    '4':
        ['https://accounts.bizzabo.com/{accountId}/team',
         'https://accounts.bizzabo.com/{accountId}/payment/processor',
         'https://accounts.bizzabo.com/{accountId}/customEmail',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/reports/registrations',
         'https://accounts.bizzabo.com/{accountId}/account/subscriptionUsage'],

    # Marketing Exec.
    '5':
        ['https://accounts.bizzabo.com/132427/events/{eventId}/contacts/contacts',
         'https://accounts.bizzabo.com/132427/events/{eventId}/promote/ticketBoost',
         'https://accounts.bizzabo.com/132427/events/{eventId}/contacts/emailAttendee',
         'https://accounts.bizzabo.com/132427/events/{eventId}/promote/socialShare',
         'https://accounts.bizzabo.com/132427/events/{eventId}/apps/website/trackingPixel']
    ,

    # Generic User
    '6':
        ['https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/setup/create',
         'https://accounts.bizzabo.com/preview/{accountId}/events/{eventId}',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/tickets/registration/form',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/agenda/editor',
         'https://accounts.bizzabo.com/{accountId}/events/{eventId}/apps/website/settings']


}

#list = recommend('name', x, 5)
#for itm in list:
#    print(itm)