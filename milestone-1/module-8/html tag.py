# def heading_two(text):
#     """
#     return heading two text of html
#     :param text: any kind of text
#     :return: html
#     """
#     html = f'<h2>{text}</h2>'
#     return html
#
# print(heading_two.__doc__)

def html_tag(text, html_tag):
    '''
    return html tag of anu text
    :param text: any kind of string
    :param html_tag: what kind of html tag you want to generate
    :return: html tag of anu text
    '''
    html = f"<{html_tag}>t{text}</{html_tag}>"
    return html
print(html_tag('this is paragraph', 'h4'))