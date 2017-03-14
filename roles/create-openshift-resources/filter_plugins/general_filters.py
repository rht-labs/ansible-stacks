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


def create_param_string(key_value_pairs):
    pairs = []
    string = ""
    for key in key_value_pairs:
        pair = "\"{}={}\"".format(key, key_value_pairs[key])
        pairs.append(pair)
    for i, pair in enumerate(pairs):
        string += " -p {}".format(pair)
    return string


def create_env_string(key_value_pairs):
    pairs = []
    string = ""
    for key in key_value_pairs:
        pair = "\"{}={}\"".format(key, key_value_pairs[key])
        pairs.append(pair)
    for i, pair in enumerate(pairs):
        string += " -e {}".format(pair)
    return string


class FilterModule(object):
    ''' A set of general filters to support OpenShift CLI '''
    def filters(self):
        return {
            'key_value_pairs_string': create_key_value_pairs_string,
            'oc_param_string': create_param_string,
            'oc_env_string': create_env_string
        }
