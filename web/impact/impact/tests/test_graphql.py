# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

import json
from django.urls import reverse
from impact.tests.factories import ExpertFactory
from impact.tests.api_test_case import APITestCase


class TestGraphQL(APITestCase):
    url = reverse('graphql')

    def test_query_with_expert(self):
        with self.login(email=self.basic_user().email):
            user = ExpertFactory()
            query = """
                query {{
                    expertProfile(id: {id}) {{
                        user {{
                            firstName
                            lastName
                            email
                        }}
                        phone
                        linkedInUrl
                        twitterHandle
                        personalWebsiteUrl
                        image
                        title
                        company
                        primaryIndustry {{
                            name
                        }}
                        additionalIndustries {{
                            name
                        }}
                        bio
                        homeProgramFamily {{
                            name
                        }}
                    }}
                }}
            """.format(id=user.expertprofile.id)
            response = self.client.post(self.url, data={'query': query})
            self.assertJSONEqual(
                str(response.content, encoding='utf8'),
                {
                    'data': {
                        'expertProfile': {
                            'user': {
                                'firstName': user.first_name,
                                'lastName': user.last_name,
                                'email': user.email
                            },
                            'phone': user.expertprofile.phone,
                            'linkedInUrl': user.expertprofile.linked_in_url,
                            'twitterHandle': user.expertprofile.twitter_handle,
                            'personalWebsiteUrl': user.expertprofile.personal_website_url,
                            'image': '',
                            'title': user.expertprofile.title,
                            'company': user.expertprofile.company,
                            'primaryIndustry': {
                                'name': user.expertprofile.primary_industry.name
                            },
                            'additionalIndustries': [],
                            'bio': user.expertprofile.bio,
                            'homeProgramFamily': {
                                'name': user.expertprofile.home_program_family.name
                            }
                        }
                    }
                }
            )


    def test_query_without_jwt(self):
        user = ExpertFactory()
        query = """
            query {{ expertProfile(id: {id}) {{ title }} }}
        """.format(id=user.expertprofile.id)
        response = self.client.post(self.url, data={'query': query})
        self.assertEquals(response.status_code, 403)
