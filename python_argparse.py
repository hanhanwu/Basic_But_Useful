import argparse

class TestArg():
    def get_arguments(self):
        '''
        Sample terminal command line: python3.5 test_arg.py -i '../input/Raw_Text/BOOKS/no1.txt' -o ../output/Preprocessed_Output/BOOKS/
        Ak for help: python3.5 test_arg.py -i '../input/Raw_Text/BOOKS/no1.txt' -o ../output/Preprocessed_Output/BOOKS/ --help
        :return: parameter values of your command line input
        '''
        parser = argparse.ArgumentParser(description='Get terminal command line input')
        parser.add_argument('--input', '-i', type=str, dest='input_path', action='store',
                            default='../input/Raw_Text/BOOKS/',
                            help="type you input file/folder path through command line")

        parser.add_argument('--outfile', '-o', type=str, dest='output_path', action='store',
                            default='../output/Preprocessed_Output/BOOKS/',
                            help="type you output folder path through command line")

        parser.add_argument('--log', '-l', type=str, dest='log_path', action='store',
                            default='../logs/log.txt',
                            help="type the path of your log file")

        args = parser.parse_args()
        return args



def main():
    t = TestArg()
    params = t.get_arguments()
    print(params.input_path)

if __name__ == "__main__":
    main()
