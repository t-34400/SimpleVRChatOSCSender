# SimpleVRChatOSCSender
OSCフォーマットでVRChatと通信を行うPython GUIアプリ．

## 事前知識
VRChantにおけるOSC通信については，[公式ドキュメント](https://docs.vrchat.com/docs/osc-overview)を参照すること．

## 必要パッケージ
- python_osc v1.8.3

## 使い方

### Avatar Parameters Tab
![Alt text](/img/avatar_params_tab.png)
- `Avatar Parameter Sender`では，任意のアドレスに与えた値を引数としてVRChatに送信できる．
    - 送信して意味のある値は使用中のアバターに依存する（詳細は[公式ドキュメント](https://docs.vrchat.com/docs/osc-avatar-parameters)を参照すること）．
- `Received Avatar Parameters`には，VRChatから受け取ったAvatar parameterアドレスと値が一覧表示されている．
    - 右側の入力に新しい値を入力して`Send`ボタンを押すことで，新しい値をVRChatに送信できる．

### Input Controller Tab
![Alt text](/img/input_controller_tab.png)
- `Axes`では，値が更新されるたびに，新しい値がVRChatに送信される．
- `Buttons`では，チェックボックスにチェックを入れると`1`, チェックを外すと`0`が送信される．
- 値の意味については，[公式ドキュメント](https://docs.vrchat.com/docs/osc-as-input-controller)を参照すること．

### Chatbox Tab
![Alt text](/img/chatbox_tab.png)
- `Chat`の`Text`に文字を入力し，Enterキーを押すか`Send`ボタンを押すとVRChatにチャットを送信できる．
    - `Immediate send`にチェックが入っている場合は即座に送信し，外れている場合はキーボードを表示した上でテキストを入力欄に入れる．
    - Notify soundにチェックが入っている場合は，通知SFXを表示する．
- `Typing indicator`にチェックが入っている場合は，typing indicatorを表示する．

### Trackers Tab
![Alt text](/img/trackers_tab.png)
- 各トラッカーの位置，回転を変更すると値を送信できる．
- 詳しい仕様については，[公式ドキュメント](https://docs.vrchat.com/docs/osc-trackers)を参照すること．

### OSC config Tab
![Alt text](/img/osc_config_tab.png)
- Senderでは，送信先のIPとポートを指定する．
    - 次回送信時に自動で現在の入力値のIPとポートに送信される．
- Receiverでは，Avatar Parametersの受信サーバーのIPとポートを指定する．
    - 値を更新したあとに，`Rebuild Receiver Server`ボタンを押すと，新しいIPとポートでの受信サーバーが立ち上がる．
- VRChat側のポートの設定方法については，[公式ドキュメント](https://docs.vrchat.com/docs/osc-overview#vrchat-ports)を参照すること.

### ライセンス
[MITライセンス](LICENSE)

### 注意事項
- 現時点では，公式ドキュメントに沿って作成しただけで，実際の挙動を確認したわけではない．