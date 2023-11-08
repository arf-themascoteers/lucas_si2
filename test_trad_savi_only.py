from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        ["savi"]
    ]
    algorithms = ["mlr", "svr", "rf"]
    c = Evaluator(prefix="test_trad_savi_only", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()