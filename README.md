# PYTIL

## About

Python Utilities to be used as cli utilities or libraries

__WARNING__ The content of this repository is under no waranty. Read the LICENSE




## Scripts

### Config Loader

__about:__ Configuration loader for yaml files

__file:__ config_loader.py

__CLI:__ no


#### Functions

 * *load_config_file*
    * __about:__ Loads yaml config file and return data as map

    * __arguments:__  

        * path - named argument specifies the path for the config file[kwargs] (Optional, default config.yaml)

### Custom Logger

__about:__ Standard logging facility extensions for multiple file programs. Helps standarnize logs, identify executing files, track timestamp.

__file:__ custom_logger.py

__CLI:__ no

#### Functions

 * *setup*

    * __about:__ Instantiate shared log with name. Can be accessed by using *logging.getLogger('\<name\>')* 

   * __arguments:__  
     * log_level - Logging level (DEBUG|INFO|WARNING|ERROR), [kwargs](Optional, default *logging.INFO*)

* *print_objects*
    Prints an object and a label (using strings)

    * __usage:__
    Pass label as kwarg name and object as kwarg value.  
    Debug level must be set to DEBUG
        ```python
        custom_logger(label = myobject)
        ```
### MREF (Match Regex In File)

__about:__ *grep* like utility that stores set of matchig strings in a file(No repetition).

__file:__ mref.py

__CLI:__ yes

#### CLI Usage
Use no parameters for interactive mode

in interactive mode, when asked for regex, leave blank and press enter for first sugestion

if '-o' option not used a time based output name will be generated

```bash
$python mref.py -r "\\\$P\{[A-Za-z][0-9]?.?[A-Z\-Z]*[0-9]?\}" -i RMT.sql -o RMT_param.txt

```

#### Functions

* TODO (Functions are available but doc yet to come)


### Replacer

__about:__ Utility tooll for massive find and replace  
Loads a file with tuples of find and replace values, then loads target file to apply the replacing pattern, adn finaly stores the result in a new file

__file:__ replacer.py

__CLI:__ yes

#### CLI Usage
if '-o' option not used a time based output name will be generated

```bash
$python reparam.py -r test_param.txt -i RMT_fixedTA.sql -o test_out.sql
```

#### Functions

* TODO (Functions are available but doc yet to come)

### UTTOOL (Youtube download tool)
__about:__ Allows users or programs to download youtube videos

__File:__ uttool.py

__Original Repository:__  github.com/LC-Duarte/uttool

#### CLI Usage:

* Single video download

    Use the output and the source options like the example bellow

    ```bash

    $python uttool.py -o <path-to-ouput-folder> -s <url-to-video>

    ```

* Multiple video dowload  
    Create a new
    yaml config file containg *"out_path"* and *"video_list"* like the example bellow:

    __NOTE:__ If repetitive links are provided, the script will ignore the second occourence

    ```yaml

    #config_uttool.yaml

    out_path: /Users/Leonardo/Google Drive/investimento/curso_mira/video_aulas
    video_list:
        - https://www.youtube.com/watch?v=hKY0Z8J1cCU
        - https://www.youtube.com/watch?v=RZuEG-TtmGA
        - https://www.youtube.com/watch?v=DggquAatQNA
        - https://www.youtube.com/watch?v=HFXMxZLW4qA

    ```

    call the script providing the path to that config file

    ```bash

    $python uttool.py -c <config-file-path>

    ```

    Fore more information on usage of *uttol* check its [original repostory](http://github.com/LC-Duarte/uttool) or run the script with the help option (-h or --help)

#### Functions

* TODO (Functions are available but doc yet to come)

## Author
Leonardo Chaves Duarte 

leonardochavesduarte@gmail.com

github.com/LC-Duarte/

Curitiba - Parana - Brazil

