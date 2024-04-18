from Classes.Input import vinput, vranges, vrange
import Classes.Texts.Queries as q

def request_start_end():
    ranges = ['variable_start', 'variable_end']
    return vranges(q.stat_end_a_b_request,
        ranges, q.e_s_error, 'e_s_error')

def request_a_b():
    ranges = ['variable_a', 'variable_b']
    return vranges(q.a_b_request,
        ranges, q.range_error, 'range_error')

def request_n(start, end):
    request = lambda: vinput(q.n_request)['variable_n']
    return vrange(request, 'n', start, end)
