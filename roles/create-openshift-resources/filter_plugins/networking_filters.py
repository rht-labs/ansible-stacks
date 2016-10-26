import json
import copy

def apply_ports_spec_config(deployment_config, application):
    deployment_config_ports_spec = create_port_spec_for_deployment_config( application )
    
    if len(deployment_config_ports_spec) > 0:
        updated_deployment_config = modify_deployment_config_with_new_ports_spec( deployment_config, deployment_config_ports_spec  )
        return updated_deployment_config
    else:
        return deployment_config    

def create_port_spec_for_deployment_config( application ):
    deployment_config_ports_spec = []
    for route in application['routes']:
        for port_config in route['service']['ports']:
            port_spec = {}
            port_spec['containerPort'] = port_config['target_port']
            port_spec['protocol'] = port_config['protocol']
            deployment_config_ports_spec.append( port_spec )
    return deployment_config_ports_spec

def modify_deployment_config_with_new_ports_spec( deployment_config, deployment_config_ports_spec ):
    updated_deployment_config = copy.deepcopy( deployment_config )
    # we currently only support one container pods https://github.com/rht-labs/api-design/issues/48
    updated_deployment_config['spec']['template']['spec']['containers'][0]['ports'] = deployment_config_ports_spec
    return updated_deployment_config

def create_secured_route_options( route, app_name ):
    options_string = ''
    if 'route_type' in route and route['route_type'] != '':
        options_string += '{} '.format( route['route_type'] )
    if 'name' in route and route['name'] != '':
        options_string += '{} '.format( route['name'] )
    
    # current API model does not have a service name, so we assume it's the same of the app.name
    options_string += '--service {} '.format( app_name )

    if 'hostname' in route and route['hostname'] != '':
        options_string += '--hostname {} '.format( route['hostname'] )
    if 'port' in route and route['port'] != '':
        options_string += '--port {} '.format( route['port'] )
    
    return options_string

def create_unsecured_route_options( route, app_name ):
    options_string = ''
    
    # current API model does not have a service name, so we assume it's the same of the app.name
    options_string += '{} '.format( app_name )
    
    if 'name' in route and route['name'] != '':
        options_string += '--name {} '.format( route['name'] )
    
    if 'hostname' in route and route['hostname'] != '':
        options_string += '--hostname {} '.format( route['hostname'] )
    if 'port' in route and route['port'] != '':
        options_string += '--port {} '.format( route['port'] )
    
    return options_string

class FilterModule(object):
    ''' A filter to build a custom ports spec and optionally apply it to a deployment config  '''
    def filters(self):
        return {
            'apply_ports_spec_config': apply_ports_spec_config,
            'create_secured_route_options': create_secured_route_options,
            'create_unsecured_route_options': create_unsecured_route_options
        }

