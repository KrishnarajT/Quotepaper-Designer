from pathlib import Path

def search_in_srt(path_to_srt, text):
    '''
    Searches for the text in the subtitle file, and returns the line number where it was found
    '''
    with open(path_to_srt, 'r', errors='ignore') as f:
        all_subs = f.readlines()
    for _, i in enumerate(all_subs):
        if text.lower() in i.lower():
            print(_, i)
            found = _
            break
        else:
            found = 0
    return found


def find_timestamp(all_subs, line_no):
    '''
    Takes the line number where the text search was hit, and returns the timestamp of that text
    '''
    tmp_list = all_subs[line_no-4:line_no]
    for _, j in enumerate(tmp_list):
        if '-->' in j:
            break
    print(tmp_list[_])
    timestamp = tmp_list[_].split(',')[0].split(':')
    timestamp.append(int(tmp_list[_].split(',')[1][:3]))
    # timestamp = tmp_list[_].split('>')[1].strip(' ').split(',')[0].split(':')
    for _, line_no in enumerate(timestamp):
        timestamp[_] = int(timestamp[_])
    timestamp[2] = timestamp[2] + 3
    return timestamp

