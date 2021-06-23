def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


tags = ['h1', 'h2', 'p', 'ul', 'li']

for tag in tags:
    if tag != 'li':
        print_tag = html_tag(tag)
        print_tag(f'this is the {tag} tag')
    else:
        for i in range(4):
            print_tag = html_tag(tag)
            print_tag(f'this is the {tag} {i} tag')
