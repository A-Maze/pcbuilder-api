README

GIT
Make sure not to push to develop and especially not master. Always make your own branch based on develop and when whatever you're doing is
done make a pull request. Let someone else of the group review and merge your request. Do not merge your own pull requests.

URL TRAVERSAL
We're using Pyramid's URL traversal. This mean we're working with factories. If this concept is new to you please read http://docs.pylonsproject.org/docs/pyramid/en/1.0-branch/narr/traversal.html. You most likely just want to add handlers with the right context of a factory rather than hard coding the route.

STYLE GUIDE
Please keep the following in mind while developing the API https://www.python.org/dev/peps/pep-0008/ . Any code that's not pep 8 valid should not be
merged.



