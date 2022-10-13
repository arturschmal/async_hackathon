# Lamport Clocks

Time in distributed systems.

## abstract

Ordering of events in distributed systems is not trivial. To get a concept of time in these systems we need physical clocks and reasoning about partial ordering before we can construct a global ordering of events.

Lamport introduces a formalism for this reasoning and defines the requirements. Here we will create async networks of clocks and proxies and do experiments about the ordering of events in networks of async services.

## references

1. https://medium.com/baseds/logical-time-and-lamport-clocks-part-1-d0317e407112
2. https://lamport.azurewebsites.net/pubs/time-clocks.pdf
3. https://greenlet.readthedocs.io/en/latest/contextvars.html
