# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479758423.346278
_enable_loop = True
_template_filename = 'themes/zen/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        helper = _mako_get_namespace(context, 'helper')
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="post">\n    ')
        __M_writer(str(arusahni.html_title()))
        __M_writer('\n        <div class="meta">\n            <div class="authordate">\n                <time class="timeago" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n            ')
        __M_writer(str(arusahni.html_translations(post)))
        __M_writer('\n            ')
        __M_writer(str(arusahni.html_sourcelink()))
        __M_writer('\n            </div>\n            ')
        __M_writer(str(arusahni.html_tags(post)))
        __M_writer('\n        </div>\n        <div class="body">\n            ')
        __M_writer(str(post.text()))
        __M_writer('\n        </div>\n        ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('        ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n    </div>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/zen/templates/post.tmpl", "line_map": {"128": 25, "129": 27, "130": 27, "131": 30, "132": 30, "133": 32, "134": 32, "135": 33, "136": 34, "137": 34, "138": 34, "139": 36, "140": 36, "141": 36, "142": 38, "143": 38, "149": 143, "23": 3, "26": 4, "29": 2, "35": 0, "53": 2, "54": 3, "55": 4, "56": 5, "61": 16, "66": 39, "72": 7, "83": 7, "84": 8, "85": 8, "86": 9, "87": 10, "88": 10, "89": 10, "90": 12, "91": 12, "92": 12, "93": 13, "94": 13, "95": 14, "96": 14, "97": 15, "98": 15, "104": 18, "118": 18, "119": 20, "120": 20, "121": 23, "122": 23, "123": 23, "124": 23, "125": 24, "126": 24, "127": 25}, "uri": "post.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""