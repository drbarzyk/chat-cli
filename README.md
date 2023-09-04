# Chat Client Application

A Python-based chat client that allows users to send and receive messages. The chat interactions are managed using API requests to an external service. Additionally, the application provides a graphical representation of the number of readable messages sent per user.

## Features:

1. **User Identification**: Begin your chat session by setting sender and recipient names.
2. **Special Chat Commands**:
    - `:clear` - Clears all chats.
    - `:update` - Refreshes and updates the chat view.
    - `:quit` - Exits the chat and displays a bar chart of message counts.
3. **Message Handling**: Send messages to your recipient and view incoming messages in real-time.
4. **Graphical Visualization**: After quitting a chat session, view a bar chart that displays the number of messages sent by each participant.

## Dependencies:

- [requests](https://pypi.org/project/requests/): Needed to make HTTP requests to the external chat service.
- [matplotlib](https://matplotlib.org/stable/users/installing.html): Used for plotting the message counts in a bar chart.

## Installation:

1. Clone the repository:
   ```
   git clone [URL of the GitHub repo]
   ```
2. Navigate to the directory:
   ```
   cd [Directory name]
   ```
3. Install the required libraries:
   ```
   pip install requests matplotlib
   ```
4. Run the chat client:
   ```
   python chat_client.py
   ```

## Usage:

1. Start the chat client.
2. Enter the sender and recipient names.
3. Begin chatting! Use the special commands (`:clear`, `:update`, `:quit`) as needed.

## Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License:

[MIT](LICENSE.txt)
