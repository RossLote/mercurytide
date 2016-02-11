from django.utils.html import strip_tags


def human_readable_filesize(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def get_links(soup, url):
    links = []

    for l in soup.find_all('a'):
        text = l.contents[0] if l.contents else 'N/A'
        try:
            link = l['href']
        except:
            'N/A'

        links.append(
            (
                link,
                strip_tags(text)
            )
        )
    return links

def get_missing_keywords(soup):
    keywords_meta = soup.findAll(attrs={"name":"keywords"})
    if keywords_meta:
        keywords = keywords_meta[0]['content'].encode('utf-8').split(', ')
        missing_words = [k for k in keywords if k not in word_list]
    else:
        missing_words = ''

    return missing_words
