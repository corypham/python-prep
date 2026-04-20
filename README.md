# python-prep


## Directory Structure:

```
python-prep/
├── README.md
│
├── 01_syntax/
│   ├── variables_types.py
│   ├── control_flow.py
│   ├── functions.py
│   ├── lists_dicts_sets.py
│   ├── comprehensions.py
│   ├── string_formatting.py
│   └── file_io.py
│
├── 02_modules/
│   ├── sys_and_os.py          # sys.argv, sys.path, os.path, os.environ
│   ├── pathlib_basics.py      # modern file path handling
│   ├── json_handling.py       # json.load, json.dump, parsing real payloads
│   ├── imports_deep_dive.py   # __name__, __main__, relative vs absolute
│   ├── write_your_own/
│   │   ├── mymodule.py        # module you write
│   │   └── main.py            # imports and uses mymodule
│   └── miniproject/
│       └── file_organizer.py  # script: reads a dir, sorts files by type
│
├── 03_classes/
│   ├── class_basics.py        # __init__, self, instance vars
│   ├── inheritance.py         # super(), method override
│   ├── dunder_methods.py      # __str__, __repr__, __len__, __eq__
│   ├── properties.py          # @property, getter/setter
│   ├── decorators.py          # write your own + read Django-style ones
│   ├── classmethods_static.py
│   └── miniproject/
│       └── task_manager.py    # CLI task tracker using classes only
│
├── 04_networking/
│   ├── socket_tcp_basics.py   # bind, listen, connect, send/recv
│   ├── socket_udp.py
│   ├── error_handling.py      # try/except, timeouts, connection errors
│   ├── requests_http.py       # GET/POST, headers, status codes
│   ├── read_real_code/
│   │   └── notes.md           # paste confusing work code here, annotate it
│   └── miniproject/
│       └── tcp_chat.py        # simple client/server chat from scratch
│
└── 05_miniprojects/
    └── README.md              # one bigger project per quarter
```

