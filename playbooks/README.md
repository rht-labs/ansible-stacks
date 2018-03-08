# Playbooks

## load_infra.yml
This playbook is used to load up (i.e.: bootstrap) the infrastructure based on the Red Hat Open Innovation Labs [Automation API](https://github.com/rht-labs/api-design)

Example run:

```
>> ansible-playbook -e 'openshift_user=<username>' -e 'openshift_password=<password>' -e 'api_document_url=<api_document_url>' playbooks/load_infra.yml
```

**Notes**
 1. The user needs to have cluster-admin (or equivalent) rights for the roles to run successfully.

## load_identities.yml
This playbook is used to load users and groups into an identity manager based on the Red Hat Open Innovation Labs [Automation API](https://github.com/rht-labs/api-design)

Example run:

```
>> ansible-playbook -e 'ipa_admin_user=<username>' -e 'ipa_admin_password=<password>' -e 'api_document_url=<api_document_url>' playbooks/load_identities.yml
```


**Notes**
 1. The user needs to have idm rights to add/remove/modify users and groups


