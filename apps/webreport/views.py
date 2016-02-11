from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.utils.html import strip_tags
from .forms import URLForm
import requests
import bs4
from collections import Counter
import re
import string
from .utils import get_links, get_missing_keywords, human_readable_filesize


def get_report(url):
    response = requests.get(url)
    html = response.content
    soup = bs4.BeautifulSoup(html)
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('style')]

    page_title = soup.title.string

    # Get the size of the
    pagesize = len(response.content)
    human_readable_pagesize = human_readable_filesize(pagesize)

    #find what's visible
    visible_html = ''.join([''.join(t.findAll(text=True)) for t in soup.findAll('body')])
    visible_text = "".join(l for l in strip_tags(visible_html) if l not in string.punctuation)

    # remove any blank words
    word_list = [i for i in visible_text.split(' ') if i]

    word_count = len(word_list)

    counter = Counter(word_list)

    top_five = counter.most_common(5)

    uniques = len([i for i in counter.values() if i == 1])

    meta_tags = re.findall(r'(<meta.*>)', html)

    missing_words = get_missing_keywords(soup, word_list)

    links = get_links(soup, url)

    return {
        'title': page_title,
        'tags': meta_tags,
        'pagesize' : human_readable_pagesize,
        'word_count' : word_count,
        'unique_words': uniques,
        'top_five': top_five,
        'missing_words' : ', '.join(missing_words),
        'links' : links,
        'page_url': url
    }


# Create your views here.
class ReportView(FormView):
    template_name = 'webreport/report.html'
    form_class = URLForm

    def form_valid(self, form):
        report = get_report(form.cleaned_data['url'])
        context = self.get_context_data(report=report)
        return self.render_to_response(context)
