import sys
import subprocess
import pytest

import promote_imagestream


class TestClass:

    def test_service_account_should_not_exist(self):
        # given nothing

        # when
        result = promote_imagestream.does_service_account_exist('test-sa', 'python-tests-build')
        # then
        assert result is False

    def test_service_account_should_exist_with_role(self):
        # given
        promote_imagestream.create_service_account('test-sa', 'python-tests-build')
        promote_imagestream.add_role_to_user('edit', 'test-sa', 'python-tests-build')

        # when
        result = promote_imagestream.does_service_account_exist('test-sa', 'python-tests-build')
        # then
        assert result is True
        # cleanup
        promote_imagestream.delete_service_account('test-sa', 'python-tests-build')

    def test_should_promote_image(self):
        # given
        promote_imagestream.create_nodejs_example_app('python-tests-build')

        # when
        promote_imagestream.wait_until_imagestream_tag_is_available('nodejs-mongodb-example', 'latest', 'python-tests-build')
        promote_imagestream.promote_image('python-tests-build', 'nodejs-mongodb-example', 'latest', 'python-tests-promote')

        # then
        assert promote_imagestream.does_imagestream_tag_exist('nodejs-mongodb-example', 'latest', 'python-tests-promote') is True

    @classmethod
    def setup_class(cls):
        promote_imagestream.create_openshift_project('python-tests-build')
        promote_imagestream.create_openshift_project('python-tests-promote')

    @classmethod
    def teardown_class(cls):
        promote_imagestream.delete_openshift_project('python-tests-build')
        promote_imagestream.delete_openshift_project('python-tests-promote')
