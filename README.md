# Cache timing attack vulnerability test suite

This repo is based on the code from the following paper:

`A Benchmark Suite for Evaluating Caches’ Vulnerability to Timing Attacks`

## Code
The unmodified code from the paper can be found under the tag [original_code](https://github.com/samobot/cpu-cache-timing-test-suite/releases/tag/orignal_code).  I does not compile under modern versions of gcc.  We found that gcc 7 works to compile the original.

The original code has been modified to allow it to compile on gcc 16.  The supporting scripts have also been modified where possible for improved convenience.