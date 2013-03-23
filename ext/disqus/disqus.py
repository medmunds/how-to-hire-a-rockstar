"""
sphinxcontrib.disqus
~~~~~~~~~~~~~~~~~~~~

Add Disqus commenting to html pages.
http://www.disqus.com

"""

import os

from jinja2 import contextfunction

from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.errors import ExtensionError
from sphinx.jinja2glue import BuiltinTemplateLoader, SphinxFileSystemLoader

from .jinja_filters import register_filters

EXT_NAME = '.'.join(__name__.split('.')[:-1])
DISQUS_TEMPLATE_NAME = 'disqus.html'

ext_dir = os.path.abspath(os.path.dirname(__file__))
templates_dir = os.path.join(ext_dir, '_templates')
static_dir = os.path.join(ext_dir, '_static')


def add_static_path(app):
    """Add our extension _static dir to the app's static_path"""
    # Must go first, so that ours can be overwritten by user's
    if static_dir not in app.config.html_static_path:
        app.config.html_static_path.insert(0, static_dir)


def add_templates_path(app):
    """Add our extension _templates dir to the app's templates_path"""
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        return  # Disqus only makes sense in HTML

    # This is a little ugly, but there doesn't seem to be an opportunity to add
    # to app.config.templates_path before the builder is inited. So we have to
    # extend the builder's template loader by duplicating some of its internals:
    template_loader = app.builder.templates
    if not isinstance(template_loader, BuiltinTemplateLoader):
        raise ExtensionError("%s only works with Sphinx's BuiltinTemplateLoader"
                             % EXT_NAME)

    # Insert our templates_dir after the ones from conf.py (and before the themes):
    num_from_conf = template_loader.templatepathlen  # BuiltinTemplateLoader stashes the count
    template_loader.pathchain.insert(num_from_conf, templates_dir)
    template_loader.loaders.insert(num_from_conf, SphinxFileSystemLoader(templates_dir))
    template_loader.templatepathlen += 1


def add_jinja_functions(app):
    """Add our extension functionality to the template environment."""
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        # We don't know how to find Jinja2 environment for other builders
        # (and comments probably don't make sense in them, anyway).
        return

    register_filters(app.builder.templates.environment)
    app.builder.templates.environment.globals['disqus_comments'] = disqus_comments


# noinspection PyUnusedLocal
def add_disqus_page_context(app, pagename, templatename, context, doctree):
    """Add our config params to the template-rendering context"""
    context.update(
        disqus_shortname=app.config.disqus_shortname,
        disqus_urlroot=app.config.disqus_urlroot,
    )


@contextfunction
def disqus_comments(context, identifier=None, title=None, url=None, urlroot=None, shortname=None):
    """Insert a Disqus comments section in the HTML.

    Available as a Jinja2 global. In a template::

        {{ disqus_comments() }}

    """
    # We resolve all of these variables at the last possible moment (now),
    # so templates may override them right up to the time they call disqus_comments().
    shortname = shortname or context.resolve('disqus_shortname')
    if not shortname:
        return ""  # Disqus not (or no longer) enabled

    identifier = identifier or context.resolve('disqus_identifier')
    title = title or context.resolve('disqus_title')
    url = url or context.resolve('disqus_url')
    urlroot = urlroot or context.resolve('disqus_urlroot')

    comments_template = context.environment.get_template(DISQUS_TEMPLATE_NAME)
    return comments_template.render(
        context,
        disqus_shortname=shortname,
        disqus_identifier=identifier,
        disqus_title=title,
        disqus_url=url,
        disqus_urlroot=urlroot)


def setup(app):
    app.require_sphinx('1.0')
    app.add_config_value('disqus_shortname', None, 'html')
    app.add_config_value('disqus_urlroot', None, 'html')
    app.add_stylesheet("disqus.css")

    app.connect("builder-inited", add_static_path)
    app.connect("builder-inited", add_templates_path)
    app.connect("builder-inited", add_jinja_functions)
    app.connect("html-page-context", add_disqus_page_context)
