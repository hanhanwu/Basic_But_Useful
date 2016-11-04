    
    # Write and append 
    # If the file exists, no header needed to be added
    # With DicWriter, you can read columns by name
    ## Well, since in some company, you even cannot install python pandas and Spark, have to use python csv , if you have to write python
    
    with open(all_sources_counts_path, 'ab') as csv_output:
        fieldnames = ['Category', 'Message_Count', 'Date', 'Part']
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)

        if os.stat(all_sources_counts_path).st_size == 0: writer.writeheader()
        writer.writerow({'Category':'Total', 'Message_Count':all_dct['Total'], 'Date':my_date, 'Part':part})
        for k in category_dct.keys():
            writer.writerow({'Category':k, 'Message_Count':all_dct[k], 'Date':my_date, 'Part':part})
