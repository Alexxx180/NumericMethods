def input_list(query, variables):
    result = []
    request = prompt(query)

    for variable in variables:
        if len(variable) == 1:
            result.append(variable[0]())
        else:
            name = variable[1]
            if name == '':
                result.append(None)
            else:
                convert = variable[0]
                result.append(convert(request[name]))
    return result
