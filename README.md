# CEC: Character Encoding Converter

Convert file encoding to different encoding.

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

### Default to utf-8 

```
$ ./python.sh cec.py [FILE PATH or DIRECTORY]
```

```
[File] data/14KANAGA.CSV	[Detector] {'confidence': 0.2862116573623867, 'encoding': 'SHIFT_JIS'}
[File] data/a.txt	        [Detector] {'confidence': 1.0, 'encoding': 'ascii'}
```

### Specify the output file encoding

c.f. utf-16

```
$ ./python.sh cec.py --output-encoding utf_16 [FILE PATH or DIRECTORY]
```

## Sample data

- [Zip code data of Kanagawa Prefecture (**Shift_JIS**)](http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/14kanaga.zip)
    - [Zip code data in Japan](http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html)

## References

- [Standard Encodings - Python](https://docs.python.org/2.7/library/codecs.html#standard-encodings)