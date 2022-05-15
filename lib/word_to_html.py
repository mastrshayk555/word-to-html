import mammoth


class Converter:
    def __init__(self, author: str, title: str, description: str, category: str, date: str,
                 input_file: str, output_file: str):
        self.author = author
        self.title = title
        self.description = description
        self.category = category
        self.date = date
        self.input_file = input_file
        self.input_file_path = f'./input/{self.input_file}.docx'
        self.output_file = output_file
        self.output_file_path = f'./output/{self.output_file}'

    def write_html(self):
        with open(self.input_file_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            full_html = (
                    f'<!DOCTYPE html><html><head>\n\t<title>{self.title}</title>\
                        <meta name="docTitle" content="{self.title}">\
                        <meta name="description" content="{self.description}">\
                        <meta name="docNumber" content="">\
                        <meta name="date" content="{self.date}">\
                        <meta name="Category" content="{self.category}">\
                        <meta name="Author" content="{self.author}">\
                        </head><body>'
                    + html
                    + "</body></html>"
            )
            with open(self.output_file_path, "w", encoding="utf-8") as f:
                f.write(full_html)

    def clean_html(self):
        apostrophe = '’'
        quote1 = '“'
        quote2 = '”'
        hyphen1 = '–'
        hyphen2 = '—'
        nbsp = ' '
        dot3 = '…'

        with open(self.output_file_path, encoding="utf8") as html_file:
            txt = html_file.read()
            txt = txt.replace(apostrophe, "'")
            txt = txt.replace(quote1, '"')
            txt = txt.replace(quote2, '"')
            txt = txt.replace(hyphen1, '-')
            txt = txt.replace(hyphen2, '-')
            txt = txt.replace(dot3, '...')
            txt = txt.replace(nbsp, '')

        with open(self.output_file_path, "w", encoding="utf-8") as outf:
            outf.write(txt)
