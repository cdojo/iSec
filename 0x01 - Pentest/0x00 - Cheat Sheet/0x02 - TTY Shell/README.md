# 0x02 - TTY Shell

## Shell Spawning

* Python

```python
python -c 'import pty; pty.spawn("/bin/sh")'
```

```python
import os

os.system('/bin/bash')
```

* Bash

```bash
/bin/sh -i
```

* Perl

```perl
perl —e 'exec "/bin/sh";'
```

```perl
exec "/bin/sh";
```

* Ruby

```ruby
exec "/bin/sh"
```

* Lua

```lua
os.execute('/bin/sh')
```

* vi

```vi
:!bash
```

```vi
:set shell=/bin/bash:shell
```