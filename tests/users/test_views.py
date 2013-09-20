# -*- coding: utf-8 -*-
"""
tests.users.test_views
~~~~~~~~~~~~~~~~~~~~~~~

This module implements view tests which can be seen as "smoke tests"
considering they go through the whole application stack for the users
API end-points.

"""
import json

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient as Client

from .factories import UserF, GroupF

User = get_user_model()


# Users

class UsersAPITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com',
                                             password='pass')
        self.user.is_staff = True
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='pass')

    def test_get_users(self):
        # one user available
        url = reverse('user-list')
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(content['results']), 1)

        # one more user available
        user = UserF()

        url = reverse('user-list')
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(content['results']), 2)

        # user with group
        group = GroupF()
        user.groups.add(group)
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(content['results']), 2)

    def test_post_user(self):
        url = reverse('user-list')
        data = {
            'email': 'test-user@gmail.com',
            'password': 'test',
        }
        res = self.client.post(url, json.dumps(data),
                               content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 201)
        self.assertIsNotNone(content['url'])
        self.assertEqual(content['email'], data['email'])

    def test_get_user(self):
        # get one user
        user = UserF()

        url = reverse('user-detail', kwargs={'pk': user.pk})
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content['email'], user.email)

    def test_put_user(self):
        user = UserF()
        data = {
            # in PUT, all mandatory fields must be provided
            'first_name': 'new-user-first-name',
            'email': 'new_email@example.com',
        }
        url = reverse('user-detail', kwargs={'pk': user.pk})
        res = self.client.put(url, json.dumps(data),
                              content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content['first_name'], data['first_name'])
        self.assertEqual(content['last_name'], user.last_name)

    def test_patch_user(self):
        user = UserF()
        data = {
            'first_name': 'new-user-first-name',
        }
        url = reverse('user-detail', kwargs={'pk': user.pk})
        res = self.client.patch(url, json.dumps(data),
                                content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content['first_name'], data['first_name'])

    def test_delete_user(self):
        user = UserF()

        url = reverse('user-detail', kwargs={'pk': user.pk})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, 204)

    def test_users_permissions(self):
        # only admin users can access to users and groups
        user = User.objects.create_user(email='test@locarise.com',
                                        password='password',)

        new_client = Client()
        new_client.login(email=user.email, password='password')

        # permission denied GET
        url = reverse('user-list')
        res = new_client.get(url)
        self.assertEqual(res.status_code, 403)

        # permission denied POST
        data = {
            'email': 'test@example.com',
        }
        res = new_client.post(url, data)
        self.assertEqual(res.status_code, 403)

        user = UserF()
        url = reverse('user-detail', kwargs={'pk': user.pk})

        # permission denied GET
        res = new_client.get(url)
        self.assertEqual(res.status_code, 403)

        # permission denied PUT
        data = {
            'first_name': 'new-user-first-name',
            'email': 'new_email@example.com',
        }
        res = new_client.put(url, data)
        self.assertEqual(res.status_code, 403)

        # permission denied DELETE
        res = new_client.delete(url)
        self.assertEqual(res.status_code, 403)

    def test_user_set_password(self):
        url = reverse('user-set-password', kwargs={'pk': self.user.pk})
        data = {
            'password': 'new-password',
        }
        res = self.client.post(url, data)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content, {'status': 'password set'})


# Groups

class GroupsAPITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com',
                                             password='pass')
        self.user.is_staff = True
        self.user.save()
        self.client = Client()
        self.client.login(email=self.user.email, password='pass')

    def test_get_groups(self):
        # one group available
        url = reverse('group-list')
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(content['results']), 0)

        # one group available
        group = GroupF()

        url = reverse('group-list')
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(content['results']), 1)
        self.assertEqual(content['results'][0]['name'], group.name)

    def test_post_groups(self):
        url = reverse('group-list')
        data = {
            'name': 'test-group',
        }
        res = self.client.post(url, json.dumps(data),
                               content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 201)
        self.assertIsNotNone(content['url'])
        self.assertEqual(content['name'], data['name'])

    def test_get_group(self):
        # get one group
        group = GroupF()

        url = reverse('group-detail', kwargs={'pk': group.pk})
        res = self.client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)

    def test_put_group(self):
        group = GroupF()
        data = {
            'name': 'new-group-name',
        }
        url = reverse('group-detail', kwargs={'pk': group.pk})
        res = self.client.put(url, json.dumps(data),
                              content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content['name'], data['name'])

    def test_patch_group(self):
        group = GroupF()
        data = {
            'name': 'new-group-name',
        }
        url = reverse('group-detail', kwargs={'pk': group.pk})
        res = self.client.patch(url, json.dumps(data),
                                content_type='application/json')
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(content['name'], data['name'])

    def test_delete_group(self):
        group = GroupF()

        url = reverse('group-detail', kwargs={'pk': group.pk})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, 204)

    def test_groups_permissions(self):
        # only admin groups can access to groups and groups
        user = User.objects.create_user(password='password',
                                        email='test@locarise.com')

        new_client = Client()
        new_client.login(email=user.email, password='password')

        # authorization denied GET
        url = reverse('group-list')
        res = new_client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 403)

        # permission denied POST
        data = {
            'name': 'test-group',
        }
        res = new_client.post(url, data)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 403)

        group = GroupF()
        url = reverse('group-detail', kwargs={'pk': group.pk})

        # permission denied GET
        res = new_client.get(url)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 403)

        # permission denied PUT
        data = {
            'name': 'new-group-name',
        }
        res = new_client.put(url, data)
        content = json.loads(res.content)
        self.assertEqual(res.status_code, 403)

        # permission denied DELETE
        res = new_client.delete(url)
        self.assertEqual(res.status_code, 403)
