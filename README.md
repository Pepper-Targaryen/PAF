# PAF (Projet d'apprentissage finale)

This is a project at the end of the first year in Telecom ParisTech. We have 4 people, 2 Chineses, 1 French and 1 Tunisian in the team. The tutor is Wenqin SHAO, a network teacher from Telecom ParisTech. The project aims at learning knowledge and in this project, we've learned about RTT (Round Trip Time) representing delay in network, application of neural network and two classic algorithms CUSUM and Bayesian.

The project is mainly based on Python but to apply the algorithm of Bayesian, we still need the environment of R.

The difficulty of the application of neural network is that there are too many '0' representing that there is no changement at the position. So a performant strategy might be assuming there is no changement at all, which gives a high accuracy. The core of the final model for the neural network is that we trained our model by artificial dataset (small pieces of 100 points and 0 ~ 8 changements). And we test with artificial dataset as well. This gives a high accuracy but still, if we turn to the real dataset, the model is less performant. What's more, we do have a pre-treatment before entering the input data. And the model uses a bidirectional LSTM of 32 parameters.

The problem is that I don't know how to really design a sophisticated neural network for now. The project gives us 2 weeks and we know nothing before. We start from the classic methods for the first week and do the whole system of evalution, comparing with the 'ground-truth'. The second week, we tried the neural work. And we have a day of demonstration. The tutor is great. He demonstrated how to use the Keras and Tensorflow to implement the neural network and he provided plenty of tools and datasets for the project.

## Detecting Internet Delay Changes with Artificial Neural Network

The target of this project is simple: how to automatically detect changes in time-series?

What for? It depends on the type of time-series we look at, e.g. stock price over last two months, global annual average temperature over the past 5000 years, etc.

Since we are “serious” network researchers, we are looking at latency across the Internet. If measured properly, Internet delay could be highly informative. It is not only a user side performance indicator, but as well reveals how the Internet is administrated. One of the applications we previously looked at is to tell from Internet latency time series when and where in the vast Internet congestion occurs. And one import prerequisite to this application is to detection significant changes in Internet latency time-series.

How to do that? Previously, we have already collected a bunch of Internet delay time-series, from which a “ground-truth” dataset of moments of change has been constructed. We then applied a Bayesian statistics method to the detection of changes, which worked well. Since Artificial Neural Networks (ANN) has become such a big deal over the past few years, we can’t resist the temptation of asking you to build a plug a ANN to our analysis pipeline. It is thus up to you to claim whether ANN is a worthwhile tool or a useless decoration to this application. (Relax, you are not going to start from zero. You shall stand on the “shoulder” of our previous works ranging from labelled dataset to visualization tools.)

Desirable skill set:

Curiosity; if you learn fast enough, it’s OK that you have none of the rest
Python, R, javascript, or no matter what tool you think that can get the job done;
Basic probability and statistics knowledge.
