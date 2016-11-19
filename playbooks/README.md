# Playbooks

## load_infra.yml
This playbook is used to load up (i.e.: bootstrap) the infrastructure based on the Red Hat Open Innovation Labs [Automation API](https://github.com/rht-labs/api-design)

Example run:

```
>> ansible-playbook -e 'openshift_user=<username>' -e 'openshift_password=<password>' -e 'api_document_url=<api_document_url>' playbooks/load_infra.yml
```

**Notes**
 1. The user needs to have cluster-admin (or equivalent) rights for the roles to run successfully.

