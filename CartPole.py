# -*- coding: utf-8 -*-
# @Time : 2024/1/8 11:37
# @Author : yysgz
# @File : CartPole.py
# @Project : RL_models

import gym

env = gym.make('CartPole-v1', render_mode='rgb_array')

state = env.reset()
for t in range(100):
    # env.render()  # 弹出窗口, a window pops up
    # print("state)

    action = env.action_space.sample()
    state, reward, done, info = env.step(action)[0]
    print("state: {}, reward: {}, done: {}".format(state, reward, done))

    if done==1:
        print('Finished')
        break

env.close()