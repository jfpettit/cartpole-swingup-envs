# cartpole-swingup-envs

This repository contains one CartPole SwingUp [OpenAI gym](https://gym.openai.com/) environment from the [WANN paper](https://weightagnostic.github.io/) and one adaptation of that environment.

The original environment code is [here](https://github.com/google/brain-tokyo-workshop/blob/master/WANNRelease/WANNTool/custom_envs/cartpole_swingup.py).

The adaptation made is to produce a discrete version of the original environment.

You can install these environments with:

```
git clone https://github.com/jfpettit/cartpole-swingup-envs.git
pip install -e cartpole-swingup-envs
```

Then you can use the two included environments via:

``` python
import gym
import cartpole_swingup_envs

continuous_env = gym.make('CartPoleSwingUpContinuous-v0')

discrete_env = gym.make('CartPoleSwingUpDiscrete-v0')
```

And then use them as regular Gym environments.