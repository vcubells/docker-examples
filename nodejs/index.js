var express = require('express');
var os = require("os");

var app = express();
var hostname = os.hostname();

app.get('/', function (req, res) {
  res.send('<html><body><h1>Bienvenidos al <b>Webinar: Contenedores Docker</b></h1><h2>Soy el contenedor ' + hostname + '</h2></body></html>');
});

const PORT = 80;
const HOST = '0.0.0.0';


app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
