# Class to handle shipping cost calculation
class ShippingCostCalculator:
    # Base rates for different weight ranges
    BASE_RATES = {
        (0, 2): 1.5,
        (2, 5): 2.5,
        (5, 10): 3.5,
        (10, float('inf')): 5
    }

    # Constants for extra cost calculation
    EXTRA_COST_DISTANCE_THRESHOLD = 500
    EXTRA_COST = 50

    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_cost(self) -> float:
        for weight_range, rate in self.BASE_RATES.items():
            if weight_range[0] <= self.weight < weight_range[1]:
                cost = self.distance * rate
                break
        else:
            raise ValueError('Invalid weight')

        if self.distance > self.EXTRA_COST_DISTANCE_THRESHOLD:
            cost += self.EXTRA_COST

        return cost

    def _get_rate_for_weight(self, weight):
        for weight_range, rate in self.BASE_RATES.items():
            if weight_range[0] <= weight < weight_range[1]:
                return rate
        else:
            raise ValueError('Invalid weight')


# Function to calculate shipping cost
def calculate_shipping_cost():
    # Get input for package weight and distance
    weight = float(input('Enter package weight: '))
    distance = float(input('Enter distance: '))

    # Create an instance of ShippingCostCalculator
    scc = ShippingCostCalculator(weight, distance)
    cost = scc.calculate_cost()

    print(f'The shipping cost is: {cost}')


if __name__ == '__main__':
    calculate_shipping_cost()
