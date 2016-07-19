#!/usr/bin/env python3
import regex

s=input().strip()
t=input().strip()

found = regex.finditer(t,s,overlapped=True)

results = [finds.starts() for finds in found]
results_list = [str(item+1) for sublist in results for item in sublist]

print(' '.join(results_list))
