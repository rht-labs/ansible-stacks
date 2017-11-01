# This project is deprecated.

It has been replaced by https://github.com/redhat-cop/casl-ansible/tree/master/roles/openshift-applier and https://github.com/rht-labs/labs-ci-cd

# Open Innovation Labs: Ansible Stacks

This repository contains a variety of Ansible roles to build and configure different technology stacks for Open Innovation Labs engagements. Currently, the repository is broken into two types of roles:

1. **General Pupose** - These roles are built to consume the model defined in the [Open Innovation Labs Automation API](https://github.com/rht-labs/api-design), so they are very dynamic. As the repository matures, most of the roles will fall into this category. Right now, `create-openshift-resources` is the only role that falls into this category.
2. **Specific** - These are much smaller, purpose built roles that do not consume the Automation API and here largely for reuse. All the roles except `create-openshift-resources` fall in this category.

## Related Work
This repository does not cover hosting infrastructure provisioning or the installation of a container platform, as this is the domain of the below repos:
- https://github.com/rhtconsulting/rhc-ose
- https://github.com/openshift/openshift-ansible
- https://github.com/openshift/openshift-ansible-contrib

## Supported Ansible Versions
We are actively testing against ansible versions:
- 2.2.0.0
- 2.2.1.0

## Contributing
See the [contributors guide](https://github.com/rht-labs/api-design/blob/master/CONTRIBUTING.md).
