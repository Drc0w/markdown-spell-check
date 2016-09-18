# markdown-spell-check

This project is designed in order to spell-check Markdown files.
This project has been written in `Python3` and is based on the python library `enchant`.

##Initialize environment

In order to get dependencies and run the spell-checker, use:
```
pip -r requirements.txt
```

##Usage

You can start running the spell-checker with the following command line:
```
python spellchecker.py -i input_file -o output_file
```

This will read `input_file`, check errors from the default language and write the output in `output_file`.
If no input file (respectively output file) is specified, it will read on `stdin` (respectively write on `stdout`).

You can see available languages with the following command:
```
python spellchecker.py --list
```

You can change spell-checker language by specifying it with the option `--lang LANG`.
You can also install new languages thanks to the packages `myspell-*` available on your system.

Run `python spellchecker.py --help` for more information.
