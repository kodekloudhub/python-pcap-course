events = [
        {'date': 11212021, 'name': 'Bengali wedding'},
        {'date': 11012021, 'name': 'Project meeting'},
        {'date': 11112021, 'name': 'Guitar class'},
]

sorted_events = sorted(events, key=lambda x: x['date'])
print(sorted_events)
