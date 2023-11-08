from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi"]
    ]
    algorithms = ["ann_large"]
    c = Evaluator(prefix="test_large_savi_only", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()