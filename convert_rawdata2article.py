import glob
import os

def get_rawdata_data(rawdata):
    main = rawdata.split('{{main}}:')[1].strip()
    rawdata = rawdata.split('{{main}}:')[0]

    urlname = rawdata.split('{{urlname}}:')[1].strip()
    rawdata = rawdata.split('{{urlname}}:')[0]

    title = rawdata.split('{{title}}:')[1].strip()

    return title, urlname, main

if __name__ == '__main__':

    rawdata_list = sorted(glob.glob('rawdata/*'))
    content_list = ''

    content_template = '<h3 id="{{id}}"><a href="https://mstn2050.github.io/blogs/contents/{{urlname}}">{{title}}</a></h3>'

    for rawdata_path in rawdata_list:
        with open(rawdata_path) as rawdata_file:
            rawdata = rawdata_file.read()

        title, urlname, main = get_rawdata_data(rawdata)

        with open('article_template') as article_template_file:
            article_template = article_template_file.read()

        article = article_template.replace('{{title}}', title)
        article = article.replace('{{main}}', main)

        output_path = os.path.join('docs', 'contents', urlname)
        with open(output_path, 'w') as outputfile:
            outputfile.write(article)

        content = content_template.replace('{{id}}', title)
        content = content.replace('{{title}}', title)
        content = content.replace('{{urlname}}', urlname)

        content_list += content + os.linesep

    with open('index_template') as index_templete_file:
        index_templete = index_templete_file.read()

    index_html = index_templete.replace('{{content}}', content_list.strip())

    with open('docs/index.html', 'w') as outputfile:
        outputfile.write(index_html)
