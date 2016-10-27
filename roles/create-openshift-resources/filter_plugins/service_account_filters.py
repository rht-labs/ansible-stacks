def get_sa_token_name( sa_describe_output ):
    return return_token_after_keyword( sa_describe_output, 'tokens:')

def get_sa_token_secret( sa_token_secret_command_output ):
    return return_token_after_keyword( sa_token_secret_command_output, 'token:')

def return_token_after_keyword( string, keyword ):
    tokens = string.split()
    return_next_token = False
    for t in tokens:
        if return_next_token == True:
            return t
        if ( t.lower() == keyword.lower() ):
            return_next_token = True
    return None           

class FilterModule(object):
    ''' A set of filters to support OpenShift service account creation'''
    def filters(self):
        return {
            'get_sa_token_name': get_sa_token_name,
            'get_sa_token_secret': get_sa_token_secret
        }

