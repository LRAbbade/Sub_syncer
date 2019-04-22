# Sub Syncer

An application to sync '.srt' subs

## Using the CLI

To run from the command line, you will need:

```sh
    python syncer.py <file_path> <offset>
```

Where `<file_path>` is the path of the subtitle, either absolute or relative to the current working directory, and `<offset>` is the desired offset in the entire subtitle. This should be in one of the following formats:

```py
number
number,number_2
number.number_2
```

In any of those cases, `number` will be the offset in `seconds`, and `number_2` in `microseconds`. If only microseconds are desired, it has to be specified like: `0,<number>` or `0.<number>`.

## Requirements

+ Python 3.6+
