# bad-taxi 🚕

We've been asked to develop software for
the world's first fully automated taxi.

Unfortunately, we haven't been given very
much time to develop it, and we don't want
to put taxi drivers out of work. So we are
going to build a very *bad* taxi service.

The taxi assumes it is driving around a city
made from perfect squares. It works on a
co-ordinate system, with East/West travelling
across the X axis and North/South travelling
up/down the Y axis. The origin at (0, 0) is
some arbitrary point in the city.

Passengers give their destination in the form
of co-ordinates such as (11, -13) and the
driver converts this into a series of
movements along compass directions.
So to get to the green point
on the graph, the driver could enter the
following instructions:

```
EEES
```

