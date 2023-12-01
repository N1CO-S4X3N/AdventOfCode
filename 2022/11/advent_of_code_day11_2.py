import math


worry_divider = 1


class Monkey:
    inspected_amount = 0

    def __init__(self, _monkey_id, _starting_items, _operation, _test_divisor, _test_true, _test_false):
        self.monkey_id = _monkey_id
        self.starting_items = _starting_items
        self.operation = _operation
        self.test_divisor = int(_test_divisor)
        self.test_true = int(_test_true)
        self.test_false = int(_test_false)
        self.divisor = math.gcd(*self.starting_items)

    def test(self, value):
        if value % self.test_divisor == 0:
            self.starting_items.pop(0)
            _monkey = all_monkeys[self.test_true]
            _monkey.starting_items.append(value)
        else:
            self.starting_items.pop(0)
            _monkey = all_monkeys[self.test_false]
            _monkey.starting_items.append(value)

    def do_operation(self, old_worry):
        old, operator, number = self.operation.split(' ')
        new = None
        if number == 'old':
            number = old_worry
        if operator == '+':
            new = old_worry + int(number)
        elif operator == '-':
            new = old_worry - int(number)
        elif operator == '*':
            new = old_worry * int(number)
        new = new % worry_divider
        return new

    def monkey_business(self):
        for item in self.starting_items.copy():
            self.inspected_amount += 1
            new_item = self.do_operation(item)
            self.test(new_item)


all_monkeys = []
with open(r'.\items2.txt', 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()
        if row.startswith('Monkey'):
            monkey_id = row.replace(':', '')[-1].strip()
        elif row.startswith('Starting'):
            starting_items = [int(item) for item in row.split(': ')[-1].split(', ')]
        elif row.startswith('Operation'):
            operation = row.split('new = ')[-1].strip()
        elif row.startswith('Test'):
            divisor = row.split(' ')[-1]
            worry_divider *= int(divisor)
        elif row.startswith('If true'):
            if_true = row[-1]
        elif row.startswith('If false'):
            if_false = row[-1]
        else:
            new_monkey = Monkey(monkey_id, starting_items, operation, divisor, if_true, if_false)
            all_monkeys.append(new_monkey)

for round in range(0, 10000):
    for monkey in all_monkeys:
        if not monkey.starting_items:
            continue
        monkey.monkey_business()
all_inspections = []
for monkey in all_monkeys:
    all_inspections.append(monkey.inspected_amount)
    print("Monkey", monkey.monkey_id, monkey.starting_items , ' inspected: ', monkey.inspected_amount, ' items')
v1, v2 = sorted(all_inspections)[-2:]
print('MONKEY BUSINESS: ', v1 * v2)
