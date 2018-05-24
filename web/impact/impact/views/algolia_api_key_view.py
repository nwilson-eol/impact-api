# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from algoliasearch import algoliasearch
from django.conf import settings
import time


class AlgoliaApiKeyView(APIView):
    view_name = 'algolia_api_key_view'

    permission_classes = (
        permissions.IsAuthenticated,
    )

    actions = ["GET"]

    def get(self, request, format=None):
        client = algoliasearch.Client(
            settings.ALGOLIA_APPLICATION_ID,
            settings.ALGOLIA_API_KEY)
        params = {
            'hitsPerPage': 20,
            'filters': '',
            'validUntil': int(time.time()) + 3600,
            'userToken': request.user.id
        }
        search_key = settings.ALGOLIA_SEARCH_ONLY_API_KEY
        if request.user.is_staff:
            search_key = settings.ALGOLIA_STAFF_SEARCH_ONLY_API_KEY

        public_key = client.generateSecuredApiKey(
            search_key,
            params)

        return Response({'token': public_key})