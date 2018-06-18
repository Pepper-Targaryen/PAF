# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:30:53 2018

@author: Targa
"""

#To generate the index of changements

#Method of Bayesian Change Algorithm
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import seaborn

import cProfile
import bayesian_changepoint_detection.offline_changepoint_detection as offcd
import bayesian_changepoint_detection.generate_data as gd
from functools import partial

import pandas
import timetools as tt
import changedetect as cpt

if __name__ == '__main__':
  show_plot = True
  dim = 1
  '''
  if dim == 1:
    partition, data = gd.generate_normal_time_series(7, 50, 200)
  else:
    partition, data = gd.generate_multinormal_time_series(7, dim, 50, 200)
  changes = np.cumsum(partition)

  if show_plot:
    fig, ax = plt.subplots(figsize=[16,12])
    for p in changes:
      ax.plot([p,p],[np.min(data),np.max(data)],'r')
    for d in range(dim):
      ax.plot(data[:,d])
    plt.show()

  
  #Q, P, Pcp = offcd.offline_changepoint_detection(data,partial(offcd.const_prior, l=(len(data)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  #Q_ifm, P_ifm, Pcp_ifm = offcd.offline_changepoint_detection(data,partial(offcd.const_prior, l=(len(data)+1)),offcd.ifm_obs_log_likelihood,truncate=-20)
  Q_full, P_full, Pcp_full = offcd.offline_changepoint_detection(data,partial(offcd.const_prior, l=(len(data)+1)),offcd.fullcov_obs_log_likelihood, truncate=-50)

  if show_plot:
    fig, ax = plt.subplots(figsize=[18, 16])
    ax = fig.add_subplot(2, 1, 1)
    for p in changes:
      ax.plot([p,p],[np.min(data),np.max(data)],'r')
    for d in range(dim):
      ax.plot(data[:,d])
    ax = fig.add_subplot(2, 1, 2, sharex=ax)
    ax.plot(np.exp(Pcp_full).sum(0))
    plt.show()
  
  trace = pandas.read_csv('11017.csv', sep=';', decimal=',')
  try:
  x = [tt.string_to_datetime(i) for i in trace['epoch']]
  except TypeError:
  x = [tt.epoch_to_datetime(i) for i in trace['epoch']]
  y = trace['rtt']
  y = y.as_matrix()
  y = y.astype(np.float)
  cp = [i for i, value in enumerate(trace['cp']) if value == 1]
  #Q, P, Pcp = offcd.offline_changepoint_detection(y,partial(offcd.const_prior, l=(len(y)+1)),offcd.gaussian_obs_log_likelihood, truncate=-20)
  Q_full, P_full, Pcp_full = offcd.offline_changepoint_detection(y,partial(offcd.const_prior, l=(len(y)+1)),offcd.fullcov_obs_log_likelihood, truncate=-50)
  if show_plot:
    fig, ax = plt.subplots(figsize=[18, 16])
    ax = fig.add_subplot(2, 1, 1)
    #for p in changes:
    ax.plot([0,0],[np.min(y),np.max(y)],'r')
    #for d in range(dim):
    ax.plot(y)
    ax = fig.add_subplot(2, 1, 2, sharex=ax)
    ax.plot(np.exp(Pcp_full).sum(0))
    plt.show()
  '''
  trace = pandas.read_csv('11017.csv', sep=';', decimal=',')
  try:
      x = [tt.string_to_datetime(i) for i in trace['epoch']]
  except TypeError:
      x = [tt.epoch_to_datetime(i) for i in trace['epoch']]
  y = trace['rtt']
  y = y.as_matrix()
  y = y.astype(np.float)
  cp = [i for i, value in enumerate(trace['cp']) if value == 1]
  
  detection = cpt.cpt_np(y)
  print(detection)

