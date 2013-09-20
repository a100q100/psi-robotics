import time

__all__ = ['Timer']

class Timer(object):
    '''Timer'''

    def __init__(self):
        self.t_start = time.time()

    def get_elapsed(self):
        return time.time() - self.t_start

    def tic(self):
        self.t_start = time.time()

    def toc(self):
        toc = self.get_elapsed()
        return toc

    def __repr__(self):
        return 'Timer elapsed: %.4f'%self.get_elapsed()