def calculate_shipping_cost():
    # Get input for package weight and distance
    weight = float(input('Enter package weight: '))
    distance = float(input('Enter distance: '))

    # Calculate cost based on weight and distance
    if 0 <= weight < 2:
        cost = distance * 1.5
    elif 2 <= weight < 5:
        cost = distance * 2.5
    elif 5 <= weight < 10:
        cost = distance * 3.5
    elif weight >= 10:
        cost = distance * 5
    else:
        print('Invalid weight')
        return

    if distance > 500:
        cost += 50

    print(f'The shipping cost is: {cost}')


calculate_shipping_cost()