from evaluator import Evaluator
import spec_utils
import clear

if __name__ == "__main__":
    #clear.clear_all()
    column_groups = [
        spec_utils.get_wavelengths()
    ]
    c = Evaluator(prefix="mlr", folds=10, algorithms=["mlr"], column_groups=column_groups)
    c.process()