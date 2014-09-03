gae-websockets-python-demo
==========================

WebSocket Demo using Google App Engine Managed VMs and a Python runtime with the Tornado framework


When deployed visit the /info path of your app to get the WebSocket connection URL.
For example http://sockets-dot-myappid.appspot.com/info

Then you can use any websocket client to connect to that URL. For example using the wscat command:

    wscat --connect <url from info page>


You must allow port 8080 on the default network on Compute Engine for your project.

