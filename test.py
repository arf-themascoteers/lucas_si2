from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths()
    ]
    algorithms = ["ann_savi_only", "ann_savi_learned_only", "ann_savi_learned_only_bound"]
    c = Evaluator(prefix="test", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()