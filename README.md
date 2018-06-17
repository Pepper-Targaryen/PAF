# PAF
## Detecting Internet Delay Changes with Artificial Neural Network

The target of this project is simple: how to automatically detect changes in time-series?

What for? It depends on the type of time-series we look at, e.g. stock price over last two months, global annual average temperature over the past 5000 years, etc.

Since we are “serious” network researchers, we are looking at latency across the Internet. If measured properly, Internet delay could be highly informative. It is not only a user side performance indicator, but as well reveals how the Internet is administrated. One of the applications we previously looked at is to tell from Internet latency time series when and where in the vast Internet congestion occurs. And one import prerequisite to this application is to detection significant changes in Internet latency time-series.

How to do that? Previously, we have already collected a bunch of Internet delay time-series, from which a “ground-truth” dataset of moments of change has been constructed. We then applied a Bayesian statistics method to the detection of changes, which worked well. Since Artificial Neural Networks (ANN) has become such a big deal over the past few years, we can’t resist the temptation of asking you to build a plug a ANN to our analysis pipeline. It is thus up to you to claim whether ANN is a worthwhile tool or a useless decoration to this application. (Relax, you are not going to start from zero. You shall stand on the “shoulder” of our previous works ranging from labelled dataset to visualization tools.)

Desirable skill set:

Curiosity; if you learn fast enough, it’s OK that you have none of the rest
Python, R, javascript, or no matter what tool you think that can get the job done;
Basic probability and statistics knowledge.
