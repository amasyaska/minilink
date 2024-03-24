Django Backend for test task minilink from IT-Revolution'24 by CrazyDuck192 and amasyaka

**Getting Started:**
1. install python 3.11
2. Install requirements: pip install -r requirements.txt
3. clone repo: git clone -b crazybranch --single-branch https://github.com/amasyaska/minilink.git
4. Launch server from "minilink" folder: python manage.py runserver

**Documentation:**
>views.py
* class HomePage - class based view with endpoint /relay/ with method "get".
Method returns 10 most clickable links as JSON
* class CreateLink - class based view with endpoint /relay/create/ with method "post".
Method recieves long url and shortens it. Creates new row in db if link is new
and returns shortened url. Otherwhise get shortened url from db and returns it.
* class RedirectTo - class based view with endpoint /relay/<short_link>/ with method "get".
Method recieves <short_link> from url, finds its long representation and redirects to this link.

>models.py
* class URL - model to save original url, its short representation and amount of followings.
* CustomModelManager - model manager with redefined "create" method that creates short
representation of original url before saving in db.
* PopularLinksManager - model manager with redefined "get_queryset" method that returns 10
most clickable urls.

>link_relay.py
* convert_decimal_to_tetrasexagesimal - function to create short representation of url.

