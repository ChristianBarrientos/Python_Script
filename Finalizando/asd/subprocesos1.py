# write_to_stdin.py
import sys
input = sys.stdin.read()
sys.stdout.write('Received: %s'%input)