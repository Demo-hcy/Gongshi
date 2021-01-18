def cmp_dict(expr, data) -> bool:
    """
    判断data是否包含expr
    expr中的k,v都是data中对应k,v的子集
    :param expr: 表达式字典
    :param data: 数据字典
    :return: 满足条件返回True，反之返回False
    """
    result = False
    for k, v in data.items():
        # 为字典时递归调用
        if isinstance(v, dict):
            res = cmp_dict(v, expr.get(k))
            if res is False:
                break
        # 为list时，转为集合比较
        elif isinstance(v, list) and isinstance(expr.get(k), list):
            if set(v) < set(expr.get(k)):  # 是否为子集
                continue
            else:
                break
        else:
            if v == expr.get(k):
                continue
            else:
                break
    else:
        result = True
    return result

a={'a':1,'b':{'c':2}}
b={'c':2}

print(cmp_dict(b,a))