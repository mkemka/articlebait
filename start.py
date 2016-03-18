from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import lxml.html


list_of_pages = ['http://postach.us10.list-manage1.com/track/click?u=819841bd24897de296a130d94&id=1fbd285a11&e=01afa4fcef']

stemmer = Stemmer('English')
summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

if __name__ == "__main__":
  for url in list_of_pages:
      parser = HtmlParser.from_url(url, Tokenizer('English'))
      print(lxml.html.parse(url).find(".//title").text)
      print(url),
      for sentence in summarizer(parser.document, 2):
          print(sentence),
