from csv import reader, DictReader, DictWriter, Dialect, QUOTE_MINIMAL

class MyDialect(Dialect):
  delimiter='|'
  quoting=QUOTE_MINIMAL
  quotechar='"'
  lineterminator='\n'

path = '/Users/mehul.chopra/Documents/personal/training/data-analysis-data/facebook_logs/facebook_login_logout_logs'
output_path = '/Users/mehul.chopra/Desktop/fb_outs'
with open(path) as fp:
  with open(output_path, mode='w') as fo:
    '''fb_reader = reader(fp)
    for row in fb_reader:
      print(row[0])
      print(row[3])'''

    reader = DictReader(fp, fieldnames=['username', 'date', 'time', 'action'])

    '''mydialect = Dialect()
    mydialect.delimiter = '|'
    mydialect.quoting = QUOTE_MINIMAL'''

    writer = DictWriter(fo, fieldnames=['username', 'date'], dialect=MyDialect)
    writer.writeheader()

    for row in reader:
      # print(row['username'])
      # print(row['action'])
      if row['action'] == 'out':
        writer.writerow({'username': row['username'], 'date': row['date']})
