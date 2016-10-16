class Index(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<html>
<head>
<script>
var ws = new WebSocket('ws://localhost:8000/soc');
ws.onmessage = function(event) {
    document.getElementById('message').innerHTML = event.data;
};
</script>
</head>
<body>
<p id='message'></p>
        ''')