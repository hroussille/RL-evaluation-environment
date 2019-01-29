import gym
import gym_multi_dimensional

id = gym_multi_dimensional.dynamic_register(n_dimensions=2, env_description={})
env = gym.make(id)

for i_episode in range(10):
    observation = env.reset()
    cum_reward=0
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        cum_reward += reward
        print(observation,reward,done,info)
        if done:
            print("Episode finished after {} timesteps, final reward : {}".format(t+1,cum_reward))
            break
    if t==199:
        print("Episode not finished after 199 timesteps,final reward : {}".format(cum_reward))

env.close()
