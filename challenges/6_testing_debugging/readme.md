# Testing and debugging async code

## Testing
With the pytest-async extension unit tests can wait for the eventloop to complete before testing outcomes.

### Challenge
Write unit tests for the generators we wrote in challenge 4 using pytest and pytest-asyncio.

## Debugging
For debugging we need a REPL that is able to await. IPython has a patch that allows this and since PyCharm integrates IPython the debugging functionality of PyCharm should work on the unit tests you wrote above.
We need a second event loop to evaluate async results in the debugger.
Apply the following line inside the debugger
```
import nest_asyncio 
nest_asyncio.apply()
```

### Challenge option PyCharm
Run your unit tests in debug mode within PyCharm and enable the nested event loop and evaluate and inspect some async functions

### Challenge option VScode
VSCode uses debugpy, which has seen recent code merged supporting awaiting in the debugger. This does not need a nested event loop as far as I understand.
Run your unit tests in debug mode and evaluate async functions in the debug console.

## references

1. https://pypi.org/project/pytest-asyncio/
1. https://github.com/pytest-dev/pytest-asyncio
1. https://pypi.org/project/nest-asyncio/
1. https://docs.python.org/3/library/asyncio-dev.html#debug-mode
1. https://github.com/microsoft/debugpy
1. https://github.com/microsoft/debugpy/pull/1012