from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi2"]
    ]
    algorithms = ["mlr", "svr", "rf","ann_simple"]
    c = Evaluator(prefix="test_savi_savi2_all2", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()