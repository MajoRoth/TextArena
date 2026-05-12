""" A minimal script showing how to run textarena locally """

import textarena as ta 

agents = {
    0: ta.agents.HumanAgent(),
}

# initialize the environment
env = ta.make(env_id="Wordle-v0")
env = ta.wrappers.FilesystemWrapper(env=env, hidden_solution=True) #, render_mode="standard")
env.reset(num_players=len(agents))

# main game loop
done = False 
while not done:
  player_id, observation = env.get_observation()
  action = agents[player_id](observation)
  done, step_info = env.step(action=action)
  if step_info.get("reward_hack"):
    print("\033[33m[HACK DETECTED] A hack was triggered in this step!\033[0m")
rewards, game_info = env.close()
print(rewards)
print(game_info)
