# Create OpenShift Resources Role

An ansible role that consumes the model defined in the [Open Innovation Labs Automation API](https://github.com/rht-labs/api-design). The API declares a desired state in one or more OpenShift clusters and this role is responsible for creating that state. Both projects are in early stages, so unless otherwise noted, this work is being developed against the master branch of the Automation API. Future versions will look to stabilize against a tagged release of the API.

## Variables

Most variables should be ingested by setting `openshift_clusters` to a document conforming to the [automation-api spec](https://github.com/rht-labs/api-design). The below items should be set another way.

Required to be set via CLI or host variables:
* `openshift_user`: user to login into openshift
* `openshift_password`: password for above user

Possible overrides via CLI or host variables:
* `openshift_url`, which can override `openshift_cluster.openshift_host_env` in the API document (if it exists): OpenShift REST API endpoint used to login

## Testing

There are two directories of tests in the code base:

* `plays` : ansible playbooks that exercise this role by running it using an API document. At this time, the tests do not have assertions, so a test is considered passed if the execution of the play completes.
* `units` : these are pytests that exercise custom modules in the role.

### Running and Writing Playbook Tests

**The ansible play tests have the following expectations:**

* `oc` is installed on the host where the tests are running
* `openshift_user`, `openshift_password` and `openshift_url` are set via the CLI or inventory file, with a user in the `cluster-admins` role for the cluster
* each test provides a mechanism to delete resources created in the test by setting `cleanup=true`

**To the run the tests and leave resources created intact:**
```
$ ansible-playbook -i <inventory_file> <test_playbook>
```

**To the run the tests and delete created resources:**
```
$ ansible-playbook -i <inventory_file> <test_playbook> -e cleanup=true
```


See the below sections for setting up your inventory.

#### CDK

To make it easier to get up and running, we provide an `inventory_cdk` that allows you to run these tests against the [Red Hat Container Development Kit](http://developers.redhat.com/products/cdk/overview/). This requires you to make the ssh-key available to the host running the test.

If using libvirt:

```
$ ssh-add <your_vagrant_dir>/.vagrant/machines/default/libvirt/private_key
```

And if using virtualbox:

```
$ ssh-add <your_vagrant_dir>/.vagrant/machines/default/virtualbox/private_key
```

Once your vagrant ssh key is add, you should be able to run tests like so:

To run the tests, using this command:

```
$ cd roles/create-openshift-resources/tests/plays
$ ansible-playbook -i inventory_cdk <test_playbook>
```

#### OpenShift Cluster

You may prefer to use a real OpenShift Cluster over the CDK. There are two ways to do this:

1. create an `inventory` file (which is currently git ignored so don't accidentally commit it).
  1. a
  2. b
2.
 As many of the roles part of the `ansible-stacks` implementations touches on cluster administration related areas, it's required that the user used is part of the `cluster-admins` role. For example, to run as the user **lisa** with password **mypassword!**, the following steps would be required:

```
  1. (as root) >> oadm policy add-cluster-role-to-user cluster-admin lisa
  2. (as lisa) >> ansible-playbook -e 'openshift_username=lisa openshift_password=mypassword! [cleanup=yes]' <playbook>
```


#### Known Gaps in Playbook Testing

1. persistent volumes (hard to make these portable between clusters)
2. secured routes (requires certs to be setup)
3. default routes with custom hostnames (hard to make these portable between clusters)

### Running and Writing Units Tests

**The unit tests have the following expectations:**

* `oc` is installed on the host where the tests are running
* `oc login` has been performed with a user that can create projects and objects in those projects
* [pytest is installed](http://doc.pytest.org/en/latest/getting-started.html)
* each unit test cleans up after itself. due to async deletes in OpenShift, you may need to pause between test executions so the cluster can finish deleting resources before you try to recreate them in the test.

**To the run the tests:**
```
$ pytest roles/create-openshift-resources/tests/units
```
