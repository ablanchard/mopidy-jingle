# Mopidy-Jingle

A [Mopidy](http://www.mopidy.com/>) extension that plays jingles between tracks.

## Installation

Install by running `pip install Mopidy-Jingle`

## Configuration

There is only two properties to setup `media_dir` which points to the folder where the jingles are. And `every_x` which define how often a jingle should be played.

```
[jingle]
media_dir = /home/jingles
every_x = 1
```

## Jingles

Jingles should be in `.wav` and have a sample rate of 96000 hz.
You can use the script `script/gen_jingles.sh` to generate some jingles with a text-to-speech engine. The script uses `espeak` as tts engine and `sox` to modify the sample rate.

## Changelog

### v0.1.0 (2020-05-13)
 - Initial release.
