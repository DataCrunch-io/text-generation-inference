# %%
import os
import pathlib
import subprocess
import pexpect

# %%
# text-generation-benchmark --tokenizer-name bigscience/mt0-xxl-mt --sequence-length 100 --decode-length 100
# text-generation-benchmark --tokenizer-name bigscience/bloomz-1b1 --sequence-length 100 --decode-length 100
# Not working due to complex TUI I/O requirements
"""
ret = subprocess.run(["text-generation-benchmark",
                                        "--batch-size", "1",
                                        "--sequence-length", "10",
                                        "--decode-length", "10",
                                        "--tokenizer-name", "bigscience/mt0-xxl-mt",
                                      ],
                                     universal_newlines=True,)
"""
# %%
# Second approach
child = pexpect.spawn("text-generation-benchmark --batch-size 1 --sequence-length 10 --decode-length 10 --tokenizer-name bigscience/mt0-xxl-mt")
# %%
child.expect("**Ctrl-C to stop**")
# %%
# Third approach
"""
ret = subprocess.run(["script", "-q", "-c", "text-generation-benchmark",
                                        "--batch-size", "1",
                                        "--sequence-length", "10",
                                        "--decode-length", "10",
                                        "--tokenizer-name", "bigscience/mt0-xxl-mt",
                                        "/dev/null"
                                      ],
                                     capture_output=True,
                                     text=True)

# %%
print(ret.stderr)
"""
# %%
# Fourth approach
import io
import selectors
import subprocess
import sys

def capture_subprocess_output():
    # Start subprocess
    # bufsize = 1 means output is line buffered
    # universal_newlines = True is required for line buffering
    process = subprocess.Popen(["text-generation-benchmark",
                                "--batch-size", "1",
                                "--sequence-length", "10",
                                "--decode-length", "10",
                                "--tokenizer-name", "bigscience/bloomz-1b1",
                                ],
                                bufsize=1,
                                universal_newlines=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)

    # Create callback function for process output
    buf = io.StringIO()
    def handle_output(stream, mask):
        # Because the process' output is line buffered, there's only ever one
        # line to read when this function is called
        line = stream.readline()
        buf.write(line)
        sys.stdout.write(line)

    # Register callback for an "available for read" event from subprocess' stdout stream
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ, handle_output)

    # Loop until subprocess is terminated
    while process.poll() is None:
        # Wait for events and handle them with their registered callbacks
        events = selector.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

    # Get process return code
    return_code = process.wait()
    selector.close()

    success = (return_code == 0)

    # Store buffered output
    output = buf.getvalue()
    buf.close()

    return (success, output)
# %%
success, output = capture_subprocess_output()

# %%
