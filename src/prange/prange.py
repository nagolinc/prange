__all__ = ['tqdm', 'trange']

import sys
import time
from parseStory import expandDescription,getAdventureRules


def format_interval(t):
    mins, s = divmod(int(t), 60)
    h, m = divmod(mins, 60)
    if h:
        return '%d:%02d:%02d' % (h, m, s)
    else:
        return '%02d:%02d' % (m, s)


def format_meter(n, total, elapsed):
    # n - number of finished iterations
    # total - total number of iterations, or None
    # elapsed - number of seconds passed since start
    if n > total:
        total = None
    
    elapsed_str = format_interval(elapsed)
    rate = '%5.2f' % (n / elapsed) if elapsed else '?'
    
    if total:
        frac = float(n) / total
        
        N_BARS = 10
        bar_length = int(frac*N_BARS)
        bar = '#'*bar_length + '-'*(N_BARS-bar_length)
        
        percentage = '%3d%%' % (frac * 100)
        
        left_str = format_interval(elapsed / n * (total-n)) if n else '?'
        
        return '|%s| %d/%d %s [elapsed: %s left: %s, %s iters/sec]' % (
            bar, n, total, percentage, elapsed_str, left_str, rate)
    
    else:
        return '%d [elapsed: %s, %s iters/sec]' % (n, elapsed_str, rate)


class StatusPrinter(object):
    def __init__(self, file):
        self.file = file
        self.last_printed_len = 0
        self.last_n_lines=0
    
    def print_status(self, s):
    	self.file.write("\033[2K")
    	for i in range(self.last_n_lines-1):
			self.file.write("\033[F")
			self.file.write("\033[2K")
        self.file.write('\r'+s+' '*max(self.last_printed_len-len(s), 0))
        self.file.flush()
        self.last_printed_len = len(s)
        self.last_n_lines=len(s.split("\n"))


 
    
def prange(iterable, desc='', total=None, leave=False, file=sys.stderr,
         mininterval=0.5, miniters=1):
    """
    Like tqdm, but prints a funny status message
    """
    #tqdm code
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            total = None
    
    prefix = desc+': ' if desc else ''
    
    sp = StatusPrinter(file)
    sp.print_status(prefix + format_meter(0, total, 0))
    
    start_t = last_print_t = time.time()
    last_print_n = 0
    n = 0
    for obj in iterable:
        yield obj
        # Now the object was created and processed, so we can print the meter.
        n += 1
        if n - last_print_n >= miniters:
            # We check the counter first, to reduce the overhead of time.time()
            cur_t = time.time()
            if cur_t - last_print_t >= mininterval:
            	#generate a new adventure action
            	suffix=expandDescription({"name":"event"},adventureRules)
            	#output text
                sp.print_status(prefix + format_meter(n, total, cur_t-start_t)+"\n"+suffix)
                last_print_n = n
                last_print_t = cur_t
    
    if not leave:
        sp.print_status('')
        sys.stdout.write('\r')
    else:
        if last_print_n < n:
            cur_t = time.time()
            sp.print_status(prefix + format_meter(n, total, cur_t-start_t))
        file.write('\n')
