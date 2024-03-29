import pytest

from intcode_executor import execute_intcode, load_and_run_intcode


class TestIntcodeExecution:
    def test_intcode_execution(self):
        assert execute_intcode([1,0,0,0,99]) == [2,0,0,0,99]
        assert execute_intcode([2,3,0,3,99]) == [2,3,0,6,99]
        assert execute_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
        assert execute_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

        assert execute_intcode([
            1,9,10,3,2,3,11,0,99,30,40,50
        ]) == [
            3500,9,10,70,2,3,11,0,99,30,40,50
        ]

    def test_input(self):
        assert load_and_run_intcode('input.txt') == [6730673, 12, 2, 2, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 36, 1, 19, 6, 38, 2, 6, 23, 76, 2, 27, 9, 228, 1, 5, 31, 229, 1, 35, 10, 233, 2, 39, 9, 699, 1, 5, 43, 700, 2, 47, 10, 2800, 1, 51, 6, 2802, 1, 5, 55, 2803, 2, 6, 59, 5606, 2, 63, 6, 11212, 1, 5, 67, 11213, 1, 71, 9, 11216, 2, 75, 10, 44864, 1, 79, 5, 44865, 1, 10, 83, 44869, 1, 5, 87, 44870, 2, 13, 91, 224350, 1, 95, 10, 224354, 2, 99, 13, 1121770, 1, 103, 5, 1121771, 1, 107, 13, 1121776, 2, 111, 9, 3365328, 1, 6, 115, 3365330, 2, 119, 6, 6730660, 1, 123, 6, 6730662, 1, 127, 9, 6730665, 1, 6, 131, 6730667, 1, 135, 2, 6730669, 1, 139, 10, 0, 99, 2, 0, 14, 0]

        find_target_output = load_and_run_intcode('input.txt', 19690720)
        assert find_target_output[0] == [19690720, 37, 49, 2, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 111, 1, 19, 6, 113, 2, 6, 23, 226, 2, 27, 9, 678, 1, 5, 31, 679, 1, 35, 10, 683, 2, 39, 9, 2049, 1, 5, 43, 2050, 2, 47, 10, 8200, 1, 51, 6, 8202, 1, 5, 55, 8203, 2, 6, 59, 16406, 2, 63, 6, 32812, 1, 5, 67, 32813, 1, 71, 9, 32816, 2, 75, 10, 131264, 1, 79, 5, 131265, 1, 10, 83, 131269, 1, 5, 87, 131270, 2, 13, 91, 656350, 1, 95, 10, 656354, 2, 99, 13, 3281770, 1, 103, 5, 3281771, 1, 107, 13, 3281776, 2, 111, 9, 9845328, 1, 6, 115, 9845330, 2, 119, 6, 19690660, 1, 123, 6, 19690662, 1, 127, 9, 19690665, 1, 6, 131, 19690667, 1, 135, 2, 19690716, 1, 139, 10, 0, 99, 2, 0, 14, 0]
        assert find_target_output[1] == 37
        assert find_target_output[2] == 49
