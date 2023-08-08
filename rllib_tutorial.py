from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.algorithms.algorithm import Algorithm
import os 
import traceback
import subprocess

checkpoint_path = os.path.join(os.getcwd(),"checkpoint")


if os.path.isdir(checkpoint_path):
    algo = Algorithm.from_checkpoint(checkpoint_path)
else:
    config = (
    PPOConfig().environment("Taxi-v3").rollouts(num_rollout_workers=2).framework("torch").training(model={"fcnet_hiddens":[64,64]}).evaluation(evaluation_num_workers=1))
    algo = config.build()
    
# config = (
#     PPOConfig().environment("Taxi-v3").rollouts(num_rollout_workers=2).framework("torch").training(model={"fcnet_hiddens":[64,64]}).evaluation(evaluation_num_workers=1)
# )

# then, actually build (instantiate) the settings 


# then, train!
for i in range(1000):
    # output += str(algo.train())+"\n"
    algo.train()
    if i%100==0:
        algo.save(checkpoint_dir=checkpoint_path)
        print(f"saving checkpoint to {checkpoint_path}")

subprocess.run("osascript -e 'display notification \"training done\"'")