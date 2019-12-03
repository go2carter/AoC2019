import argparse
from copy import deepcopy

OPCODES = {1, 2, 99}
OP_PTR_JUMP = {
    1: 4,
    2: 4,
    99: 0,
}


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


OPS = {
    1: add,
    2: mul,
    99: None,
}


def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('intcode_file')
    argparser.add_argument('--target_output', '-t', default=None, type=int)
    return vars(argparser.parse_args())


def execute_intcode(intcode, memory_restores=None):
    if memory_restores is not None:
        for ptr, val in memory_restores.items():
            intcode[ptr] = val
    k = 0
    while intcode[k] != 99:
        instr = intcode[k]
        if instr not in OPCODES:
            raise ValueError('Given instruction {} at position {} not valid.'.format(instr, k))
        if instr == 99:
            return intcode

        val0 = intcode[intcode[k+1]]
        val1 = intcode[intcode[k+2]]
        store = intcode[k+3]

        op = OPS.get(instr, None)
        if op is None:
            raise ValueError('Instruction {} at position {} led to invalid op.'.format(instr, k))
        output = op(val0, val1)
        intcode[store] = output

        k += OP_PTR_JUMP[instr]
    return intcode


def load_and_run_intcode(program_file, target_output=None):
    with open(program_file, 'r') as f:
        intcode = f.read()
        intcode = [int(k) for k in intcode.split(',')]

    if target_output is None:
        memory_restores = {
            1: 12,
            2: 2,
        }
        outcode = execute_intcode(intcode, memory_restores=memory_restores)
        print('Output code:')
        print(outcode)
        return outcode
    
    for noun in range(100):
        for verb in range(100):
            restores = {
                1: noun,
                2: verb
            }
            code_copy = deepcopy(intcode)
            outcode = execute_intcode(code_copy, restores)
            if outcode[0] == target_output:
                print('Output code:')
                print(outcode)
                print('noun: {}\tverb: {}'.format(noun, verb))
                return outcode, noun, verb



def main():
    args = parse_args()
    load_and_run_intcode(args['intcode_file'], args['target_output'])


if __name__ == '__main__':
    main()
