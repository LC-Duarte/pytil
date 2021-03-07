"""
uttool 
Youtube download tool
Rev 0 - march 2021 - leonardochavesduarte@gmail.com
For more information use the --help option or read ./README.md
"""

#utool
#Standard dependencies
import time
import sys
import getopt

#Third party dependencies
from pytube import YouTube
from colorama import init #Banner Dependencies
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint #Banner Dependencies
from pyfiglet import figlet_format #Banner Dependencies

#Custom dependencies
import config_loader as c_load
import custom_logger as c_log


ARG_LIST = sys.argv[1:]
#Script options
OPT = "hdc:o:s:"
#Script options long
LONG_OPT = ["help", "debug", "config",  "output" "source"] 

config_path = '/Users/Leonardo/Code/uttool/config_uttool.yaml'

NO_VAL ='~N*'

#Path to store the dowloaded videos 
output_path = './'
#List of video URLS
video_list = ['']

#YAML configuration
general_field = 'general'
out_path_field = 'out_path'
video_list_field = 'video_list'

log = c_log.setup('main', log_level = c_log.DEBUG)


def my_help():
    log.setLevel(c_log.ERROR)
    print("""
        ## About 

        Script for downloading youtube videos

        ## Options

        * -c | --config\t\tSet configuration file path 
        * -d | --debug\t\tActivate debug mode
        * -o | --output\t\tSet output path
        * -s | --source\t\tSet video source URL
        """)
    print("Type 'M'for more usage instructions or any other key for ending help ")
    inp = input(":")
    if inp != 'm' and inp != 'M':
        sys.exit(1)
    print("""
        ## Usage

        ### Single video download
        
        Use the output and the source options like the example bellow

        ```bash

        python uttool -o <path-to-ouput-folder> -s <url-to-video>

        ```
        """)

    print(
        """ 
        ### Multiple video dowloads
    
        Edit '.../uttool/cofig_uttool' and call the scripts with no options or create a new
        yaml config file containg "out_path" and "video_list" like the example bellow: 
        NOTE: If repetitive links are provided, the script will ignore the second occourence 

        ```yaml

        #config_uttool.yaml

        out_path: /Users/Leonardo/Google Drive/investimento/curso_mira/video_aulas
        video_list:
        - https://www.youtube.com/watch?v=hKY0Z8J1cCU
        - https://www.youtube.com/watch?v=RZuEG-TtmGA
        - https://www.youtube.com/watch?v=DggquAatQNA
        - https://www.youtube.com/watch?v=HFXMxZLW4qA

        ```
        If you edited the default config file at .../uttool/cofig_uttool just call the script 
        with no extra options

        ```bash

        $ python uttool.py

        ```

        If you opted for a new config file call the script providing the path to that config file

        ```bash

        $ python uttool.py -c <config-file-path>

        ```

        """)


def header():
    cprint(figlet_format('uttool', font='larry3d'),
       'red') #'smkeyboard'

def load_config(file_path):
   config = c_load.load_config_file(path = file_path)
   global output_path 
   output_path  = config.get(out_path_field,  './')
   global video_list
   video_list = set(config.get(video_list_field, None))
   log.info('Configuration loaded')
   c_log.print_objects(out_path = output_path)
   c_log.printList(video_list, name='video list')


def download_utube_vid(url, out_path):
    start_time = time.time()
    yt = YouTube(url)
    title = yt.title
    if len(title) > 31 :
        title = title[0:15] + '...'+ title[-10:]
    log.info(f"Downloading {title} from {url}")
    my_video = yt.streams.first()
    my_video.download(out_path)
    log.info(f"'{title}' downloaded in {round(time.time() - start_time, 4)}")
    return 1

def dowload_videos(url_list, out_path):
    if(len(url_list) < 1):
        log.error(f'Empty URL List --- ({url_list})')
        return -1
    elif(len(url_list) == 1):
        log.info(f'Downloading {len(url_list)} video to {out_path}')
    else: 
        log.info(f'Downloading {len(url_list)} videos to {out_path}')
    c = 0
    for url in url_list:
        c += download_utube_vid(url, out_path)
    if (c == 1):
        log.info(f'{c} video downloaded')
    else:
        log.info(f'{c} videos downloaded')
    return c

   
def main():
    global video_list
    global output_path
    global config_path
    
    load_con = True
    start_time = time.time()
    header()
    try:
        # Parsing argument
        arguments, values = getopt.getopt(ARG_LIST, OPT, LONG_OPT)
        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--helo") :
                 my_help()
                 return
            elif currentArgument in ("-c", "--config"):
                config_path = currentValue
            elif currentArgument in ("-o", "--output"):
                output_path = currentValue
            elif currentArgument in ("-s", "--source"):
                load_con = False
                video_list = [currentValue]
            elif currentArgument in ("-d", "--debug"):
                log.setLevel(c_log.INFO)
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    log.info('Starting execution')
    if load_con:
        load_config(config_path)
    c = dowload_videos(video_list, output_path)
    log.info(f'Execution finished in {round(time.time() - start_time, 2)}s')


if __name__ == '__main__':
    main()
