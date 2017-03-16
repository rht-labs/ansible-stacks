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

`plays` : ansible playbooks that exercise this role by running it using an API document. At this time, the tests do not have assertions, so a test is considered passed if the execution of the play completes.

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

**To the run the tests and leave resources created intact:**

```
$ cd roles/create-openshift-resources/tests/plays
$ ansible-playbook -i inventory_cdk <test_playbook>
```

**To the run the tests and delete created resources:**
```
$ cd roles/create-openshift-resources/tests/plays
$ ansible-playbook -i inventory_cdk -e cleanup=true <test_playbook>
```

#### OpenShift Cluster

You may prefer to use a real OpenShift Cluster over the CDK. To do this, we've provided `inventory_cluster`, which will use `ansible_connection = local`, and thus require the host to have `oc` installed. However; `inventory_cluster` does NOT provide `openshift_user`, `openshift_password` & `openshift_url` for obvious reasons.

**To the run the tests and leave resources created intact:**

```
$ cd roles/create-openshift-resources/tests/plays
$ ansible-playbook -i inventory_cluster -e "openshift_user=<user> openshift_password=<password> openshift_url=<url>" <test_playbook>
```

**To the run the tests and delete created resources:**
```
$ cd roles/create-openshift-resources/tests/plays
$ ansible-playbook -i inventory_cluster -e "openshift_user=<user> openshift_password=<password> openshift_url=<url> cleanup=true" <test_playbook>
```


#### Known Gaps in Playbook Testing

1. persistent volumes (hard to make these portable between clusters)
2. secured routes (requires certs to be setup)
3. default routes with custom hostnames (hard to make these portable between clusters)