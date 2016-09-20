# Create OpenShift Resources Role

An ansible role that consumes the model defined in the [Open Innovation Labs Automation API](https://github.com/rht-labs/api-design). The API declares a desired state in one or more OpenShift clusters and this role is responsible for creating that state. Both projects are in early stages, so unless otherwise noted, this work is being developed against the master branch of the Automation API. Future versions will look to stabilize against a tagged release of the API.


## Testing

The current tests are written against the [Red Hat Container Development Kit](http://developers.redhat.com/products/cdk/overview/) in order to increase portability. You'll need to make sure that ansible can ssh in to the vagrant image that serves the CDK. The simplest way to do this is to add the private key that vagrant generates to your local ssh agent. The below command is an example of how to do this is you are using libvirt as vagrant provider:

    `ssh-add <your_vagrant_dir>/.vagrant/machines/default/libvirt/private_key`

At this point, the configuration in the [test inventory file](tests/inventory) and the tests prefixed with `cdk` should be to run the tests. If not, please open an issue and let us know.
