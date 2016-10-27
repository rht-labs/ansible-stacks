# Create OpenShift Resources Role

An ansible role that consumes the model defined in the [Open Innovation Labs Automation API](https://github.com/rht-labs/api-design). The API declares a desired state in one or more OpenShift clusters and this role is responsible for creating that state. Both projects are in early stages, so unless otherwise noted, this work is being developed against the master branch of the Automation API. Future versions will look to stabilize against a tagged release of the API.


## Testing

### CDK
Most of the tests are written against the [Red Hat Container Development Kit](http://developers.redhat.com/products/cdk/overview/) in order to increase portability. You'll need to make sure that ansible can ssh in to the vagrant image that serves the CDK. The simplest way to do this is to add the private key that vagrant generates to your local ssh agent. The below command is an example of how to do this is you are using libvirt as vagrant provider:

```
  >> ssh-add <your_vagrant_dir>/.vagrant/machines/default/libvirt/private_key
```

At this point, the configuration in the [test inventory file](tests/inventory) and the tests prefixed with `cdk` should be to run the tests. If not, please open an issue and let us know.

### Filter Plugin Tests
Tests prefixed with `filter_test` are primarily designed as unit tests for behavior provided by custom filter plugins for this role, and specifically how the filter plugin helps drive a subset of tasks. In order to run these tests locally, you must link the custom filter plugin as if they are standalone plugins. See [the docs](http://docs.ansible.com/ansible/dev_guide/developing_plugins.html#distributing-plugins) for how to do that. When using the plugins as part of the role, they will be distributed and linked via the role without extra configurations. These tests by design test the filter using only a subset of the tasks in the role, thus the need for extra config.

These tests also target the CDK, and should be run when logged in as `admin`.

### OpenShift Environment
For test that aren't a good fit for a CDK run, i.e.: need external / 3rd party resources, a real OpenShift environment can be used. As many of the roles part of the `ansible-stacks` implementations touches on cluster administration related areas, it's required that the user used is part of the `cluster-admins` role. For example, to run as the user **lisa** with password **mypassword!**, the following steps would be required:

```
  1. (as root) >> oadm policy add-cluster-role-to-user cluster-admin lisa
  2. (as lisa) >> ansible-playbook -e 'openshift_username=lisa openshift_password=mypassword! [cleanup=yes]' <playbook>
```

**Notes** 
  1. The first command to grant cluster-admin to the user is only needed to be done once per cluster for a user.
  1. If the tests should do clean-up after execution, make sure to set the `cleanup` environment variable - i.e.: >> ansible-playbook -e 'cleanup=yes' <playbook>
