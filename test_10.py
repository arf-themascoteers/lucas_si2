from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.transform_indices([202,400,597,796,994,1192,1390,1588,1785,1981,2179,2377,2577,2772,2970,3168,3366,3564,3762,3960]),
        spec_utils.transform_indices([442,515,888,1161,1135,1783,1398,1896,1896,2020,2117,2132,2127,2157,2970,3184,3409,3409,3800,3732])
    ]
    algorithms = ["mlr"]#,"mlr","rf","svr"]
    c = Evaluator(prefix="zxz2", folds=10, algorithms=algorithms, column_groups=column_groups)
    c.process()