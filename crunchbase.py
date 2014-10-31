import os
import urllib2

try:
    import simplejson as json
except ImportError:
    import json

CRUNCHBASE_TOKEN = os.environ.get('CRUNCHBASE_TOkEN')
API_URL = 'http://api.crunchbase.com/v/2/'


class CrunchBaseError(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class CrunchBase(object):
    def __init__(self, token=None):
        self.token = token or CRUNCHBASE_TOKEN

    @staticmethod
    def __is_iterable(x):
        return isinstance(x, (list, tuple, set))

    @staticmethod
    def __get_request(url):
        """
        Returns the request.
        :param url: str or unicode
        :return:
        """
        try:
            request = urllib2.urlopen(url)
            result = request.read()
            return result
        except urllib2.HTTPError as e:
            raise CrunchBaseError(e)

    def __get_data(self, path, filters='', page=''):
        """
        Return the json loaded response.
        :param path: str or unicode
        :param filters: str or unicode
        :param page: str or unicode
        :return:
        """
        url = '{api_url}{path}?{filters}user_key={user_key}{page}'.format(
            api_url=API_URL,
            path=path,
            filters=filters,
            user_key=self.token,
            page='&page={}'.format(page) if isinstance(page, int) else ''
        )
        return json.loads(self.__get_request(url))

    def get_organization(self, permalink):
        """
        Returns the data about an organization.
        :param permalink: str or unicode
        :return:
        """
        path = 'organization/{}'.format(permalink)
        result = self.__get_data(path=path)
        return result

    def get_organizations(self, query=None, name=None, organization_type=None, locations=None,
                          categories=None, page=None):
        """
        Returns the list of organizations.
        :param query: str or unicode (name, previous names, location, and domain name)
        :param name: str or unicode (filter organization by name)
        :param organization_type: list (filter organization by one or more types).
        :param locations: list (filter Organizations by one or more Location UUIDs.)
        :param categories: list (filter Organizations by one or more Category UUIDs.)
        :param page: str or unicode or int (the page of results to retrieve )
        :return:
        """
        path = 'organizations'
        filters = []

        if name:
            filters.append('name={}'.format(name))
        if query:
            filters.append('query={}'.format(query))
        if organization_type:
            filters.append('organization_types={}'.format(organization_type))
        if locations and self.__is_iterable(locations):
            filters.append('location_uuids={}'.format(','.join(locations)))
        if categories and self.__is_iterable(categories):
            filters.append('category_uuids={}'.format(','.join(categories)))

        encoded_filters = '{}&'.format('&'.join(filters)) if filters else ''
        result = self.__get_data(path=path, filters=encoded_filters, page=page)
        return result

    def get_person(self, permalink):
        """
        Returns the data about a person.
        :param permalink: str or unicode
        :return:
        """
        path = 'person/{}'.format(permalink)
        result = self.__get_data(path=path)
        return result

    def get_people(self, page=None):
        """
        Returns the list of people.
        :param page: str or unicode or int (the page of results to retrieve )
        :return:
        """
        path = 'organizations'
        result = self.__get_data(path=path, page=page)
        return result

    def get_product(self, permalink):
        """
        Returns the data about a product.
        :param permalink: str or unicode
        :return:
        """
        path = 'product/{}'.format(permalink)
        result = self.__get_data(path=path)
        return result

    def get_products(self, page=None):
        """
        Returns the list of people.
        :param page: str or unicode or int (the page of results to retrieve )
        :return:
        """
        path = 'products'
        result = self.__get_data(path=path, page=page)
        return result

    def get_categories(self, page=None):
        """
        Returns list of categories.
        :return:
        """
        path = 'categories'
        result = self.__get_data(path=path, page=page)
        return result

    def get_locations(self, page=None):
        """
        Returns list of locations.
        :return:
        """
        path = 'locations'
        result = self.__get_data(path=path, page=page)
        return result

    def get_funding_round(self, uuid):
        """
        Returns a funding round.
        :param uuid: str or unicode
        :return:
        """
        path = 'funding-round/{}'.format(uuid)
        result = self.__get_data(path=path)
        return result

    def get_acquisition(self, uuid):
        """
        Returns an acquisition.
        :param uuid: str or unicode
        :return:
        """
        path = 'acquisition/{}'.format(uuid)
        result = self.__get_data(path=path)
        return result

    def get_ipo(self, uuid):
        """
        Returns an ipo.
        :param uuid: str or unicode
        :return:
        """
        path = 'ipo/{}'.format(uuid)
        result = self.__get_data(path=path)
        return result

    def get_fund_raise(self, uuid):
        """
        Returns an fund raise.
        :param uuid: str or unicode
        :return:
        """
        path = 'fund-raise/{}'.format(uuid)
        result = self.__get_data(path=path)
        return result
