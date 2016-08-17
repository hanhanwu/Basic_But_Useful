write_path = "[your file path]"

with open(write_path, 'w') as csvfile:
    fieldnames = ['Merchant_Name', 'Merchant_Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for t in list(all_merchant):
        writer.writerow({'Merchant_Name': t[0], 'Merchant_Category': t[1]})
