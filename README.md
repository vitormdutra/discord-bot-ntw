# Discord Music Bot Template

[![Docker Pulls](https://img.shields.io/docker/pulls/vitormdutra/discord-bot-ntw)](https://hub.docker.com/r/vitormdutra/discord-bot-ntw)
[![Docker Stars](https://img.shields.io/docker/stars/vitormdutra/discord-bot-ntw)](https://hub.docker.com/r/vitormdutra/discord-bot-ntw)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A template to create your own music bot for Discord. This bot can be easily self-hosted using Docker.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Plays music from various sources
- Intuitive commands to control playback
- Easy setup with Docker

## Prerequisites

- Docker installed
- A Discord account
- A Discord bot token

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/vitormdutra/discord-bot-ntw.git
    cd discord-bot-ntw
    ```

2. Build the Docker image:
    ```sh
    docker build -t your-username/discord-music-bot .
    ```

3. Run the Docker container with the necessary environment variable:
    ```sh
    docker run -d --name discord-music-bot -e DISCORD_TOKEN=your-discord-token your-username/discord-music-bot
    ```

## Usage

After installation, your bot will be ready to use. You can add the bot to your Discord server and start using the available commands.

### Main Commands

- `!join`: Joins the voice channel the user is in.
- `!play <url>`: Plays a song from the provided URL.
- `!pause`: Pauses the current playback.
- `!resume`: Resumes the paused playback.
- `!stop`: Stops the playback and disconnects the bot.
- `!queue`: Shows the music queue.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.