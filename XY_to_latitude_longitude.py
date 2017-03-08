# all about crime data
import csv
import pyproj   # the library you use


def main():
    data_path = "[change to your folder]/input.csv"   # change input path
    output_path = "[change to your folder]/output.csv"    # change output path

    ll = pyproj.Proj(init="epsg:4326")       # get DATUM  (WGS84)
    utm10 = pyproj.Proj(init="epsg:32610")   # get the projection for Vancouver

    output_lst = []
    cols = ["ID", "X", "Y", "Latitude", "Longitude", "TYPE", "YEAR", "MONTH", "DAY", "HOUR", "MINUTE",
            "Concantenated", "HUNDRED_BLOCK", "NEIGHBOURHOOD"]

    with open(data_path) as crime_data:
        csv_reader = csv.DictReader(crime_data)

        private_data_count = 0
        missing_data_count = 0
        total_count = 0

        for r in csv_reader:
            total_count += 1
            if r['Y'] == '0' and r['Y'] == '0':
                private_data_count += 1
                continue
            if r['Latitude'] == "" or r['Longitude'] == "":
                missing_data_count += 1
                lat, lgn = pyproj.transform(utm10, ll, float(r['X']), float(r['Y']))    # convert X, Y to latitude and longitude
                r['Latitude'] = lat
                r['Longitude'] = lgn
                output_lst.append(r)

        with open(output_path, 'a') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=cols)
            writer.writeheader()
            for r in output_lst:
                writer.writerow(r)


if __name__ == "__main__":
    main()
