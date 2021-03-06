# CEC: Character Encoding Converter

Convert character encoding to different encoding.

## Installation

Install [Docker](https://www.docker.com/) in advance.

Pull the latest docker image.

```
$ docker pull koash/cec
```

Alternatively, to build the docker image, do the following.

```
$ docker build github.com/koash/cec
```

## Usage

### Default to UTF-8 

Specify the file or directory to convert (Default to **utf-8**)

```
$ ./python.sh cec.py [FILE PATH or DIRECTORY] --input-delimiter , --output-delimiter ,
```

Character encoding information of the read file.

```
[File] data/14KANAGA.CSV	[Detects] {'confidence': 0.2862116573623867, 'encoding': 'SHIFT_JIS'}
[File] data/test.txt		[Detects] {'confidence': 1.0, 'encoding': 'ascii'}
```

Converted files are output to `result` directory.

### Specify the output file encoding

e.g., UTF-16

```
$ ./python.sh cec.py --output-encoding utf_16 [FILE PATH or DIRECTORY] --input-delimiter , --output-delimiter ,
```

### Options

```
  -h, --help            show this help message and exit
  
  --input-encoding=INPUT_ENCODING
                        specify the input file encoding
  
  --output-encoding=OUTPUT_ENCODING
                        specify the output file encoding. Default is 'utf_8'
  
  --input-delimiter=INPUT_DELIMITER
                        specify the output file delimiter. Default is 'TAB(\t)'
  
  --output-delimiter=OUTPUT_DELIMITER
                        specify the output file delimiter. Default is 'TAB(\t)'
  
  --header=HEADER       specify row number(s) to use as the column names, and the start of the data in input file.
                        Default 'header=-1' has no header and reads the first line as data.
                        header=0 denotes the first line of data rather than the first line of the file.
                        e.g, -1: no header, 0: first line, 1: second line
```

## Sample data

- [Pre-download zip code data of Kanagawa Prefecture (**Shift_JIS**)](http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/14kanaga.zip)
    - [Zip codes data of Japan](http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html)

## References

- [Chardet: The Universal Character Encoding Detector](https://github.com/chardet/chardet)
- [Standard Encodings - Python](https://docs.python.org/2.7/library/codecs.html#standard-encodings)
