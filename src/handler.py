valid_cities = ['Las Vegas', 'Henderson', 'Boulder City']

def handle(event, context):
    errors = []
    messages = []
    if 'city' in event and len(event['city']) > 1 and event['city'].lower() not in [city.lower() for city in valid_cities]:
        errors.append('city')
        messages.append('We only deliver to {}, {}, and {} right now. Please check back to see when your city becomes available.'.format(*valid_cities))

    if 'zip' in event:
        if event['zip'][0:2] != '89' and len(event['zip']) == 5:
            errors.append('zip')
            if 'We only deliver' not in '::'.join(messages):
                messages.append('We only deliver to {}, {}, and {} right now. Please check back to see when your city becomes available.'.format(*valid_cities))

        if len(event['zip']) != 5:
            errors.append('zip')

    for key, value in event.iteritems():
        if len(value) == 0 and key not in errors:
            errors.append(key)

    return dict(errors=errors, messages=messages)
