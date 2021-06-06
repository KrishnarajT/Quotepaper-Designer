import os
from pathlib import Path

# Length of each line of the quote in number of words
max_words = 12  # higher would mean long quote lines

# Maximum number of lines in each quote that is allowed
max_lines = 12  # higher  == more lines, allowing longer quotes to be pasted.

# Number of characters of each quote to check with the srt files.
charac_nums = 20  # higher == more accuracy


def modify_quotes(base_path, fortune_file_path):
    '''
    Makes the quotes shorter so that they can fit on the screen. Also removes ones that are too long for the screen.
    and saves them as Mod_Quotename in the Modified Quotes Folder
    '''
    with open(f'{fortune_file_path}', 'r') as f:
        quote_list = f.read().split('%')
        for i in range(len(quote_list)):
            quote_lines = quote_list[i].split('\n')
            for j in range(len(quote_lines)):
                quote_line_words = quote_lines[j].split(' ')
                for l in range(len(quote_line_words)):
                    quote_line_words[l] = quote_line_words[l] + ' '
                for k in range(max_words, len(quote_line_words), max_words):
                    quote_line_words[k] = quote_line_words[k] + '\n'

                tmp = ''
                tmp = tmp.join(quote_line_words)
                quote_lines[j] = tmp
            for m in range(len(quote_lines)):
                quote_lines[m] = quote_lines[m] + '\n'
            quote_list[i] = ''
            quote_list[i] = quote_list[i].join(quote_lines)
            quote_list[i] = quote_list[i].strip('\n')
        for i in quote_list[:]:
            if i.count('\n') > max_lines:
                quote_list.remove(i)
    with open(os.path.join(base_path, f'Mod_{fortune_file_path.name}'), 'w') as fout:
        bulkwrite = ''
        for i in range(len(quote_list)):
            quote_list[i] = quote_list[i] + '%'
        bulkwrite = bulkwrite.join(quote_list)
        fout.write(bulkwrite)


def remove_brackets(mod_quotesfile_path):
    """
    Returns a string of all the quotes without brackets and the parenthesis
    """
    rem_list = []
    with open(mod_quotesfile_path, 'r') as f:
        quotes = f.read()
        for _, i in enumerate(quotes):
            if i == '[':
                rem_list.append(_)
            if i == ']':
                rem_list.append(_)

    while len(rem_list) != 0:
        rem_list = []
        for _, i in enumerate(quotes):
            if i == '[':
                rem_list.append(_)
            if i == ']':
                rem_list.append(_)
        tmp = quotes[rem_list[-2]:rem_list[-1]+1]
        quotes = quotes.replace(tmp, '')
        rem_list.remove(rem_list[-1])
        rem_list.remove(rem_list[-1])

    # Parenthesis
    for _, i in enumerate(quotes):
        if i == '(':
            rem_list.append(_)
        if i == ')':
            rem_list.append(_)

    while len(rem_list) != 0:
        rem_list = []
        for _, i in enumerate(quotes):
            if i == '(':
                rem_list.append(_)
            if i == ')':
                rem_list.append(_)
        if len(rem_list) >= 2:
            tmp = quotes[rem_list[-2]:rem_list[-1]+1]
            quotes = quotes.replace(tmp, '')
            rem_list.remove(rem_list[-1])
            rem_list.remove(rem_list[-1])

    return quotes


def make_quote_list(quotes):
    '''
    Returns a quote_list that has all the quotes without the % sign and without the brackets
    So that makes it easy to directly search in the subtitles file.
    '''
    quote_list = quotes.split('%')
    for i, _ in enumerate(quote_list):
        quote_list[i] = quote_list[i].strip(
            ' ').strip('\n').strip(' ').strip('\n')
    for i in quote_list[:]:
        if len(i) == 0:
            quote_list.remove(i)
    return quote_list


def make_quote_search_list(quote_list):
    quote_search_text = []
    for i, _ in enumerate(quote_list):
        for j in range(len(quote_list[i].split('\n'))):
            if ':' in quote_list[i].split('\n')[j]:
                tmp = quote_list[i].split('\n')[j].split(
                    ':')[-1].lower().strip(' ').strip('\n')
                if len(tmp) > charac_nums:
                    quote_search_text.append(tmp[:charac_nums])
                    break
                elif 0 < len(tmp) < charac_nums:
                    quote_search_text.append(tmp)
                    break
            else:
                continue
    return quote_search_text


def mod_multiple_quotes(path):
    """
    the path should contain only a bunch of fortune files, 
    Converts them into wallpaper quote worthy format, collectively
    """
    basepath = Path(path)
    files_in_basepath = basepath.iterdir()
    for _, item in enumerate(files_in_basepath):
        qt.modify_quotes(item)
