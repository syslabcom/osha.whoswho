OSHA WhosWho
============

Boilerplate
-----------

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
Being a doctest, we can tell a story here.

First, we must perform some setup.

    >>> from plone.testing.z2 import Browser
    >>> browser = Browser(layer['app'])
    >>> portal = layer['portal']
    >>> portal_url = portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in.

    >>> browser.open(portal_url + '/login_form')

We have the login portlet, so let's use that.

    >>> browser.getControl(name='__ac_name').value = 'admin'
    >>> browser.getControl(name='__ac_password').value = 'secret'
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.


And we ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

    >>> browser.open(portal_url)

Basic Testing
-------------

We start out by adding a WhosWho object.

    >>> browser.getLink(url='createObject?type_name=whoswho').click()
    >>> browser.getControl('Title').value = 'My WhosWho'
    >>> browser.getControl('Save').click()
    >>> "Changes saved" in browser.contents
    True

Now we look at the alphabetical index:

    >>> browser.open('/'.join(browser.url.split('/')[:-1] + ['whoswho_alphabetical']))
    >>> browser.getLink(id='M-term').click()
    >>> "My WhosWho" in browser.contents
    True
