from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["red","vnir4"]
    ]
    algorithms = ["ann_simple"]
    c = Evaluator(prefix="test_red_vnir4", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()