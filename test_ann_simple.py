from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi2"]
    ]
    algorithms = ["ann_simple"]
    c = Evaluator(prefix="test_ann_savi2_only", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()