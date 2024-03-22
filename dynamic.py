from os import listdir
from time import strftime

def get_all_html( exclude ):
    htmls = []
    for f in listdir('src/'):
        if '.html' in f and not f in exclude:
            htmls.append(f)
    return htmls



def parse( filename, variables ):
    with open('src/' + filename) as f:
        data = f.read()
    start = 0
    in_block = False
    new_data = ''
    parse_mode = 'none'
    

    for i, s in enumerate(data.split(' ')):
        if s == '{{':
            in_block = True
            start = i
        elif s == '}}':
            in_block = False
        elif in_block and i > start:
            if i == start+1:
                parse_mode = s
            
            if parse_mode == 'var' and i == start+2:
                try:
                    new_data += variables[s]
                except:
                    print(f'Undefined variable: "{s}"!')
            elif parse_mode == 'insert' and i == start+2:
                new_data += parse(s, variables)


        else:
            new_data += s + ' '
        


    return new_data

def export(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def format_title( html: str ) -> str:
    title: str = html[:-5]
    if title == 'index':
        return 'Home'
    title = title.replace('-', ' ')
    title = title.title()
    return title

def generate_nav(htmls):
    data = '<!-- Generated Navigation -->\n'
    base_code = '<a href="{html}" class="nav">{formatted}</a>'
    for html in htmls:
        data += base_code.format(html=html, formatted=format_title(html))
    return data


def main():
    htmls = get_all_html( ['start.html', 'end.html'] )
    nav_htmls = [ 'index.html', 'tutorial-hub.html' ]

    variables = {
        'title':'Thbop -> {title}',
        'date':strftime('%c'),
        'nav':generate_nav(nav_htmls)
    }
    for html in htmls:
        adjusted_variables = variables.copy()
        adjusted_variables['title'] = variables['title'].format(title=format_title(html))
        data = parse(html, adjusted_variables)
        export(html, data)
    

if __name__ == '__main__':
    main()