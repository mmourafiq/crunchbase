crunchbase
==========

Python library for pulling data from the CrunchBase API.

## Usage

Make sure to set the environment variable `CRUNCHBASE_TOKEN`, or `CrunchBase(your_crunchbase_key)`  

If you already know the permalink or the uuid for a given entity, you can grab the entry
with the `get_entity` method.

```python

    from crunchbase import CrunchBase
    
    cb_api = CrunchBase('my_key')
    dustin = cb_api.get_person('dustin-moskovitz')
    facebook = cb_api.get_organization('facebook')
    facebook_like_box = cb_api.get_product('facebook-like-box')
    venture_round = cb_api.get_funding_round('b0e3eb999048d301089226cedab900a7')
    fund_raise = cb_api.get_fund_raise('b0e3eb999048d301089226cedab900a7')
    facebook_ipo = cb_api.get_ipo('a3bc391490d52ba8529d1cfc20550a87')
    whats_app_acquisition = cb_api.get_acquisition('90ad2f738079c7c0dffc66cb82487a11')
```

### List all Items

To get the list of every single item for a given entity type, you can do so 
with the +get_entities+ method.

```python
    cb_api.get_organizations()
    cb_api.get_people()
    cb_api.get_products()
    cb_api.get_categories()
    cb_api.get_locations()
```

This returns an array containing objects representing each entity.

### Search

Searching the Crunchbase is possible for `organizations`, with this parameters:
    
```python
    query: str or unicode (name, previous names, location, and domain name)
    name: str or unicode (filter organization by name)
    organization_type: list (filter organization by one or more types).
    locations: list (filter Organizations by one or more Location UUIDs.)
    categories: list (filter Organizations by one or more Category UUIDs.)
    page: str or unicode or int (the page of results to retrieve )

    cb_api.get_organizations(**filters)
```
    
## Contributing

Contributions are welcome.
