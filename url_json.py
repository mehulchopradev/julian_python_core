from json import loads, dump

path = '/Users/mehul.chopra/Documents/personal/training/data-analysis-data/url-shortner/usagov_bitly_data2012-03-16-1331923249.txt'
output_path = '/Users/mehul.chopra/Desktop/url_shortner_filter'

li = []

with open(path) as fp:
  for line in fp:
    d = loads(line)
    do = {}
    if 'c' in d:
      do['country'] = d['c']
    if 'cy' in d:
      do['county'] = d['cy']
    if 'tz' in d:
      do['timezone'] = d['tz']
    li.append(do)

with open(output_path, mode='w') as fo:
  dump(li, fo)