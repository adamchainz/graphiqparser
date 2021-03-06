import csvkit
import graphiqparser as gp

infilename = 'raw/hillary_fec_employers.csv'
outfilename = 'hillary_fec_labeled.csv'

with open(infilename, 'rU') as f:
    reader = csvkit.DictReader(f)

    all_rows = []
    for row in reader:
        raw_str = row['Employer']
        try:
            parsed = gp.tag(raw_str)
            row_dict = parsed[0]
        except:
            row_dict = {'error':'True'}

        row_dict['raw'] = raw_str
        all_rows.append(row_dict)

field_list = [  'raw', 
                'error', 
                'OtherCorporationName',
                ] + gp.LABELS

with open(outfilename, 'wb') as outfile:
    writer = csvkit.DictWriter(outfile, field_list)
    writer.writeheader()
    writer.writerows(all_rows)
