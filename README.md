# Real-time Streaming Protocol (RTSP)


> RTSP is a protocol for controlling servers that stream media over the Internet. It helps set up and manage connections between devices for audio and video streaming. With RTSP, media players and servers can talk to each other easily, so users can play, pause, change volume, and do other actions while streaming. 


####  How Does RTSP Work?


RTSP works a lot like HTTP and is often called a "network remote control" for media servers. This protocol controls video and audio streams without needing to download the media files. When a video stream starts, the device using RTSP sends a request to the media server to set it up.

The first request also needs to tell the client about the available options using the Options command. After this, a user can watch or stop the stream. Besides the Options request, RTSP supports several control commands like play, pause, and setup. RTSP uses TCP to keep a stable connection without needing local downloads or caching.

But RTSP has some downsides. It doesn't support content encryption or retransmission of lost media packets, and it can't stream directly to a browser over HTTP. This is because RTSP connects to a dedicated server for streaming and relies on RTP to send real media. To work around this, you need to use FFMPEG to convert RTSP to an HLS stream. This limitation and its lack of scalability have led to a decrease in RTSP use.

#### RTSP Requests
RTSP can send these commands from the client to the server to negotiate and control media streams:

- Options: Determines what other types of requests the media server will accept.
- Describe: Identifies the URL and type of data.
- Announce: Describes the presentation when sent from the client to the server and updates the description when returned.
- Setup: Specifies how a media stream must be transported before a play request is sent.
- Play: Starts the media transmission by telling the server to start sending data.
- Pause: Temporarily stops the stream.
- Record: Starts recording the media stream.
- Teardown: Ends the session and stops all media streams.
- Redirect: Tells the client to connect to another server by giving a new URL for the client to use.