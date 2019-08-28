from gym.envs.registration import register

register(
    id='CartPoleSwingUpContinuous-v0',
    entry_point='cartpole_swingup_envs.cartpole_swingup:CartPoleSwingUpEnv'
    )

register(
    id='CartPoleSwingUpDiscrete-v0',
    entry_point='cartpole_swingup_envs.discrete_cartpole_swingup:CartPoleSwingUpEnv'
    )