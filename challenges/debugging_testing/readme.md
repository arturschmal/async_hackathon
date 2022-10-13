# Debugging and unit testing async code

# Monitoring for debugging
With aiomonitor we can listen to our running async code and get an interactive console to inspect our event loop and tasks.

## Debugging
A debugger needs event loop support to allow it to introspect or evaluate async results.

## Testing
With the pytest-async extension unit tests can wait for the eventloop to complete before testing outcomes.

## references

1. https://codebeez.nl/blogs/europython-2022-summaries-of-selected-talks/