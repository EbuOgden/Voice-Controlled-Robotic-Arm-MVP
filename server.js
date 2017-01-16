'use strict';

var app = require('./app.js');

var exec = require('child_process').exec;

// Deployment tracking
require('cf-deployment-tracker-client').track();

var port = process.env.VCAP_APP_PORT || 3000;


app.listen(port, function(){
	setTimeout(function(){
	exec("sudo rm -rf Output.txt",function(err, stdout, stderr){})
	 exec('sudo idle -r servoZero.py', function(err, stdout, stderr){})
}, 500);
console.log('listening at:', port);
});
