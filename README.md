Django Method Override
======================

Django middleware that overrides the HTTP method through either a `_method` form param (Ruby on Rails style) or the X-HTTP-Method-Override header.

Installation
------------

1. Install via pip:

        :::bash
        $ pip install django-method-override

2. Add the `MethodOverrideMiddleware` **after** Django's `CsrfViewMiddleware`:

        :::python
        MIDDLEWARE_CLASSES = (
            # ...
            'django.middleware.csrf.CsrfViewMiddleware',
            'method_override.middleware.MethodOverrideMiddleware',
            # ...
        )

3. Add `method_override` to your `INSTALLED_APPS`:

        :::python
        INSTALLED_APPS = (
            # ...
            'method_override',
        )

Usage
-----

Use the provided template tag in your form to add the desired form:

    :::html+django
    {% load method_override %}
    <form action="{% url 'post-detail' %}" method="POST">
      {% csrf_token %}
      {% method_override 'PUT' %}
    </form>

Now, you may use `put` in you Class-based views. Django Method Override will even copy over the form data to `request.PUT`:

    :::python
    class PostView(View):
        def put(self, request):
            form = Form(request.PUT)
            # ...

The X-HTTP-Method-Override header is also supported. So for the above view, this will work too:

    :::javascript
    $.ajax({
      'headers': {'X-HTTP-Method-Override': 'PUT'},
      'type': 'POST',
      'url': 'http://localhost:8000/posts/1/',
      // ...
    });

Configuration
-------------

Django Method Override can be customized from your Django `settings.py` file:

### `METHOD_OVERRIDE_ALLOWED_HTTP_METHODS`

A list of the allowed methods for overriding. Defaults to:

    :::python
    ['GET', 'HEAD', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'PATCH']

### `METHOD_OVERRIDE_PARAM_KEY`

The form param key used to override the method. Defaults to `'_method'`.

### `METHOD_OVERRIDE_HTTP_HEADER`

The HTTP header to check. Defaults to `'HTTP_X_HTTP_METHOD_OVERRIDE'`

### `METHOD_OVERRIDE_INPUT_TEMPLATE`

The string tempalte used to render the input for the form param. It will based to kwargs, `name` and `value`. Defaults to:

    :::python
    '<input type="hidden" name="{name}" value="{value}">'

Copyright
---------

Copyright (c) 2013 [LocalMed, Inc.](http://www.localmed.com/). See LICENSE for details.
