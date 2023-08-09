# 進捗
steveで，conda(rllib)にて実行中
conda rllib作成
conda rllib に rllib, pytorch isntall
サーバー直接ray動かせない→dockerでやる→vscodeで編集できない．．となるので，ray clusterでやる．
どっかの小さいサーバーをheadにして，steveとかの大きいサーバーでcluster起動しておく．

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

[Ray Clusters](https://docs.ray.io/en/latest/cluster/getting-started.html)
[How to create ray cluster](https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html#on-prem)
