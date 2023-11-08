from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths()
    ]
    algorithms = ["ann_savi_bound"]
    c = Evaluator(prefix="test_bound", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()