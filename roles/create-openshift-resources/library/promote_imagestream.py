#!/usr/bin/python

import subprocess
import time


######################################################################
# Image Streams
######################################################################

def promote_image(src_project_name, src_imagestream, src_imagestream_tag, dst_project_name, dst_imagestream=None, dst_imagestream_tag=None):
    if dst_imagestream is None:
        dst_imagestream = src_imagestream
    if dst_imagestream_tag is None:
        dst_imagestream_tag = src_imagestream_tag
    src_image_string = format_image_string(src_project_name, src_imagestream, src_imagestream_tag)
    dst_imagestream_tag = format_image_string(dst_project_name, dst_imagestream, dst_imagestream_tag)
    tag_image(src_image_string, dst_imagestream_tag)


def format_image_string(project_name, imagestream, imagestream_tag):
    return '{}/{}:{}'.format(project_name, imagestream, imagestream_tag)


def tag_image(src_image_string, dst_image_string):
    execute_shell_command('oc tag {} {}'.format(src_image_string, dst_image_string))


def wait_until_imagestream_tag_is_available(imagestream, imagestream_tag, project_name, max_wait_time_in_seconds=300, retry_interval_in_seconds=5):
    max_retries = max_wait_time_in_seconds / retry_interval_in_seconds
    current_retry_count = 1
    while current_retry_count < max_retries:
        if does_imagestream_tag_exist(imagestream, imagestream_tag, project_name) == True:
            return
        else:
            current_retry_count += 1
            time.sleep(retry_interval_in_seconds)


def does_imagestream_tag_exist(imagestream, imagestream_tag, project_name):
    try:
        execute_shell_command('oc get istag {}:{} -n {}'.format(imagestream, imagestream_tag, project_name))
        return True
    except subprocess.CalledProcessError as e:
        return False

######################################################################
# Service Account
######################################################################


def does_service_account_exist(service_account_name, project_name):
    # oc will return exit code 1 if sa does not exist, which will then throw
    # the below error
    try:
        execute_shell_command('oc get sa {} -n {}'.format(service_account_name, project_name))
        return True
    except subprocess.CalledProcessError as e:
        return False


def create_service_account(service_account_name, project_name):
    execute_shell_command('oc create sa {} -n {}'.format(service_account_name, project_name))


def delete_service_account(service_account_name, project_name):
    execute_shell_command('oc delete sa {} -n {}'.format(service_account_name, project_name))


######################################################################
# Role Binding
######################################################################

def add_role_to_user(role, user_name, project_name):
    execute_shell_command('oc policy add-role-to-user {} -z {} -n {}'.format(role, user_name, project_name))

######################################################################
# Project
######################################################################


def create_openshift_project(project_name):
    try:
        execute_shell_command('oc new-project {}'.format(project_name))
    except subprocess.CalledProcessError as e:
        print e


def delete_openshift_project(project_name):
    execute_shell_command('oc delete project {}'.format(project_name))

######################################################################
# New App
######################################################################


def create_nodejs_example_app(project_name):
    execute_shell_command('oc new-app --template nodejs-mongodb-example -n {}'.format(project_name))

######################################################################
# Shell Interface
######################################################################


def execute_shell_command(command):
    return subprocess.check_output(command, shell=True)
