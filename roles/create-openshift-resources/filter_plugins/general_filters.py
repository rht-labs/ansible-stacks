def create_key_value_pairs_string(key_value_pairs):
    pairs = []
    string = ""
    for key in key_value_pairs:
        pair = key + '=' + key_value_pairs[key]
        pairs.append(pair)
    for i, pair in enumerate(pairs):
        string += pair
        if i != (len(pairs) - 1):
            string += ','
    return string

class FilterModule(object):
    ''' A set of general filters to support OpenShift CLI'''
    def filters(self):
        return {
            'key_value_pairs_string': create_key_value_pairs_string
        }
