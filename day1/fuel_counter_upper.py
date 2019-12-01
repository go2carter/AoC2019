import argparse


def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('model_file')
    argparser.add_argument('--include-fuel', action='store_true',
                           help='Include added fuel in fuel calculations.')
    return vars(argparser.parse_args())


def fuel_for_module(mass, include_fuel=False):
    # 8 is cutoff for nonzero fuel requirement
    if mass <= 8:
        return 0
    mass //= 3
    fuel = mass - 2
    if include_fuel:
        added_fuel = fuel_for_module(fuel, include_fuel)
        fuel += added_fuel
    return fuel


def compute_total_fuel(model_file, include_fuel=False):
    total_fuel = 0
    with open(model_file, 'r') as f:
        for module in f:
            mass = int(module)
            module_fuel = fuel_for_module(mass, include_fuel)
            total_fuel += module_fuel
    print('Total fuel needed for Santa: {}'.format(total_fuel))
    return total_fuel


def main():
    args = parse_args()
    compute_total_fuel(args['model_file'], args['include_fuel'])


if __name__ == '__main__':
    main()
