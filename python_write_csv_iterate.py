write_path = "[your file path]"

with open(write_path, 'w') as csvfile:
    fieldnames = ['Merchant_Name', 'Merchant_Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for t in list(all_merchant):  # each t is a distionary, even keys are in different order for each t, it's fine
        writer.writerow(t)
