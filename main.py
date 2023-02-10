# """
# CMPS 2200  Recitation 2
# """

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	# """Compute the value of the recurrence $W(n) = aW(n/b) + n

	# Params:
	# n......input integer
	# a......branching factor of recursion tree
	# b......input split factor

	# Returns: the value of W(n).
	# """
	# TODO
  if n==1:
    return n
  else:
    return (a*(simple_work_calc(n//b, a, b)) + n)




def test_simple_work():
	# """ done. """
  assert simple_work_calc(10, 2, 2) == 36 #TODO
  assert simple_work_calc(20, 3, 2) == 230 #TODO
  assert simple_work_calc(30, 4, 2) == 650 #TODO

  assert simple_work_calc(8, 3, 2) == 65
  assert simple_work_calc(40, 5, 2) == 5390


def work_calc(n, a, b, f):
	# """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	# Params:
	# n......input integer
	# a......branching factor of recursion tree
	# b......input split factor
	# f......a function that takes an integer and returns 
 #           the work done at each node 

	# Returns: the value of W(n).
	# """
  if n==1:
    return n
  else:
    return a*(work_calc(n//b, a, b, f)) + f(n)

print(work_calc(10, 2, 2, lambda n: 1))
print(work_calc(100, 2, 2, lambda n: 1))
print(work_calc(1000, 2, 2, lambda n: 1))
    
# print(work_calc(10, 2, 2,lambda n: 1))

    
def span_calc(n, a, b, f):
	# """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	# Params:
	# n......input integer
	# a......branching factor of recursion tree
	# b......input split factor
	# f......a function that takes an integer and returns 
 #           the work done at each node 

	# Returns: the value of W(n).
	# """
  if n==1:
    return n
  else:
    return (span_calc(n//b, a, b, f)) + f(n)


def test_work():
# 	""" done. """
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300

  assert work_calc(8, 2, 2, lambda n: n*n*n) == 680
  assert work_calc(16, 4, 2, lambda n: n*n) == 1280


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	# """
	# Compare the values of different recurrences for 
	# given input sizes.

	# Return:
	# A list of tuples of the form
	# (n, work_fn1(n), work_fn2(n), ...)
	
	# """
  result = []
  
  for n in sizes: # compute W(n) using current a, b, f
    result.append((
      n,
      work_fn1(n),
			work_fn2(n)
		))
  return result

def print_work_results(results):
	# """ done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: 1) #f(n) = n^c where n < log_2(2)

  
	# create work_fn2
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n*n) #f(n) = n^c where n > log_2(2)

  res = compare_work(work_fn1, work_fn2)
  print_work_results(res)

test_compare_work()



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
  for n in sizes:
		# compute W(n) using current a, b, f
    result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
  return result

def print_span_results(results):
	# """ done """
	print(tabulate.tabulate(results,
							headers=['n', 'S_1', 'S_2'],
							floatfmt=".3f",
							tablefmt="github"))
  
def test_compare_span():
	# create span_fn1
  span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1) 
  
	# create work_fn2
  span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n*n)  

  res = compare_work(span_fn1, span_fn2)
  print_span_results(res)

test_compare_span()




