import sys
import codecs

from htmltreediff import diff

def main(argv=None):
    if not argv:
        argv = sys.argv  # pragma: no cover
    with codecs.open(argv[1], 'r', 'utf-16') as file_a:
        html_a = file_a.read()
    with codecs.open(argv[2], 'r', 'utf-16') as file_b:
        html_b = file_b.read()
    with codecs.open('output.html', 'w', 'utf-16') as file_o:
        file_o.write(diff(html_a, html_b, cutoff=0.0, pretty=True))

if __name__ == '__main__':
    main()  # pragma: no cover
