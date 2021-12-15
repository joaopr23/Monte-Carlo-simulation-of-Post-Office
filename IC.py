def mean_confidence_interval(data, alpha):
  n = len(data)
  m = float(sum(data))/n # sample mean
  var = sum([(x - m)**2 for x in data]) / float(n-1) # sample variance
  # calls the inverse CDF of the Student's t distribution
  import scipy.stats, math
  tfact = scipy.stats.t._ppf(1-alpha/2., n-1)
  h = tfact * math.sqrt(var/n)
  return m-h, m+h
if __name__ == "__main__":
  confidence = .99 # 95%
  alpha = 1 - confidence
  data = [0]
  print(mean_confidence_interval(data, alpha))
