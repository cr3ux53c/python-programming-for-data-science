def vector_size_check(*vector_variables):
    return len(set([len(i) for i in vector_variables])) == 1
