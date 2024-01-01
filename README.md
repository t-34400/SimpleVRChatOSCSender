# SimpleVRChatOSCSender
Python GUI app for VRChat communication using OSC format.

## Prerequisites
Refer to the [official documentation](https://docs.vrchat.com/docs/osc-overview) for information on OSC communication in VRChat.

## Required Packages
- python_osc v1.8.3

## Usage

### Avatar Parameters Tab
![Alt text](/img/avatar_params_tab.png)
- `Avatar Parameter Sender` allows sending values to VRChat with any address as an argument.
    - The meaningful values to send depend on the currently used avatar (refer to the [official documentation](https://docs.vrchat.com/docs/osc-avatar-parameters) for details).
- `Received Avatar Parameters` displays a list of Avatar parameter addresses and values received from VRChat.
    - Enter a new value in the right input and press the `Send` button to send the new value to VRChat.

### Input Controller Tab
![Alt text](/img/input_controller_tab.png)
- `Axes` sends new values to VRChat every time the value is updated.
- `Buttons` sends '1' when the checkbox is checked and '0' when unchecked.
- Refer to the [official documentation](https://docs.vrchat.com/docs/osc-as-input-controller) for the meaning of values.

### Chatbox Tab
![Alt text](/img/chatbox_tab.png)
- Enter text in the `Text` field of `Chat`, press Enter, or click the `Send` button to send a chat to VRChat.
    - If `Immediate send` is checked, it sends immediately; if unchecked, it shows the keyboard for text input.
    - If `Notify sound` is checked, it plays a notification SFX.
- If `Typing indicator` is checked, it displays the typing indicator.

### Trackers Tab
![Alt text](/img/trackers_tab.png)
- You can send values by changing the position and rotation of each tracker.
- Refer to the [official documentation](https://docs.vrchat.com/docs/osc-trackers) for detailed specifications.

### OSC config Tab
![Alt text](/img/osc_config_tab.png)
- In the Sender section, specify the destination IP and port.
    - The next time you send, it will automatically send to the current input IP and port.
- In the Receiver section, specify the IP and port of the Avatar Parameters receiving server.
    - After updating the values, pressing the `Rebuild Receiver Server` button will create a new receiving server with the new IP and port.
- Refer to the [official documentation](https://docs.vrchat.com/docs/osc-overview#vrchat-ports) for how to configure ports on the VRChat side.

### License
[MIT License](LICENSE)

### Notes
- At the moment, this application has been created following the official documentation, and the actual behavior has not been verified.
