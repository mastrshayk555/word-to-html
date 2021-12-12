from lib.word_to_html import Converter


author = 'Sharon Boyd'
doc_file_title = 'Setting Achievable Goals For Your Employees'
title = 'Setting Achievable Goals For Your Employees'
description = 'Using the S-M-A-T-E-R Guide framework will help you to clearly provide specific objectives and help your team keep focus on their objectives.  '
category = ''
date = '12/01/2021'
output_filename = 'SharonBoydBusiness_2021Dec01.htm'


def convert_to_html():
    file = Converter(author=author, title=title, description=description, category=category, date=date, input_file=doc_file_title,
          output_file=output_filename)
    file.write_html()
    file.clean_html()


convert_to_html()