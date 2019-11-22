import sys
import secrets
from htmltreediff import diff

def main(argv=None):
    if not argv:
        argv = sys.argv # pragma: no cover
    with open(argv[1]) as file_a:
        html_a = file_a.read()
    with open(argv[2]) as file_b:
        html_b = file_b.read()
    output_filename = f"output_{secrets.token_urlsafe(6)}.html"
    f = open(output_filename, "w")
    f.write(diff(html_a, html_b, cutoff=0.0, pretty=True))
    f.close()
    print(output_filename)

if __name__ == '__main__':
    main() # pragma: no cover
