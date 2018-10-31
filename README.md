Tenning RL
===========================

In this project, I will solve a multi-agent domain problem, where two agents should collaborate and/or compete to solve the task. I will work with the [Tennis](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#tennis) environment, where two agents control rackets to bounce a ball over a net.

<p align="center"><img src="https://user-images.githubusercontent.com/10624937/42135623-e770e354-7d12-11e8-998d-29fc74429ca2.gif" alt="Example" width="50%" style="middle"></p>

If an agent hits the ball over the net, it receives a reward of +0.1.  If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01.  Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation.  Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping. 

The task is episodic, and in order to solve the environment, the agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). The environment is considered solved, when the average (over 100 episodes) of those **scores** is at least +0.5. This project is part of the [Deep Reinforcement Learning Nanodegree](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwigwuKwr4LdAhUMI5AKHTuBCz0QFjAAegQIDBAB&url=https%3A%2F%2Fwww.udacity.com%2Fcourse%2Fdeep-reinforcement-learning-nanodegree--nd893&usg=AOvVaw3OfEe4LlR9h_4vW3TZpE_o) program, from Udacity. You can check my report [here](reports/Report.pdf).


### Install
This project requires **Python 3.5** or higher, the Tennis Environment (follow the instructions to download [here](INSTRUCTIONS.md)) and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Statsmodels]()
- [Torch](https://pytorch.org)
- [UnityAgents](https://github.com/Unity-Technologies/ml-agents)


### Run
In a terminal or command window, navigate to the top-level project directory `tennis-rl/` (that contains this README) and run the fol$

```shell
$ jupyter notebook
```

This will open the Jupyter Notebook software and notebook in your browser which you can use to explore and reproduce the experiments t$


### References
1. Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., et al. *Continuous control with deep reinforcement learning*. arXiv.org, 2015.
2. Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., et al. *Human-level control through deep reinforcement learning*. Nature, 2015.
3. ...


### License
The contents of this repository are covered under the [MIT License](LICENSE).
