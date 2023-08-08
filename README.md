# Rllibまとめ
[Getting Started with RLlib](https://docs.ray.io/en/latest/rllib/rllib-training.html)
- trainして，saveする．
- tuneでハイパラチューニングできる．
- single_actionの計算の仕方．
- policy_state == NN weightsの取得方法．
- configuring
- debugging rllib experiments
- "monitor": trueでgymのエピソードmp4取れる
- tfならeager modeというのがある
- data ouput apiでepisode tracesを取得できる
- log levelをlog_levelで指定できる
- ray stackで，stack tracesをdumpできる

[Key Concepts](https://docs.ray.io/en/latest/rllib/key-concepts.html)
- workerを取り出して個々に操作できる    
- batchのsampleについて
- training_step() -> もっとアルゴリズムのカスタマイズをしたい場合に使うやつっぽい

[Environments](https://docs.ray.io/en/latest/rllib/rllib-env.html)
- 