import sys
import tty
import termios
from select import select
import thread
import threading


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def press_any_key_to_continue():
    print "Press Any Key to Continue..."
    getch()


def raw_input_with_timeout(prompt="", timeout=30.0):
    print prompt,
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring


def getch_timeout(timeout=0.01):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        rlist, _, _ = select([sys.stdin], [], [], timeout)
        if rlist:
            s = sys.stdin.read(1)
            return s
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
