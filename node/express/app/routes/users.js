var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('users', { title: 'Users' });
});

// practice this stuff: https://www.airpair.com/javascript/complete-expressjs-nodejs-mongodb-crud-skeleton
//
//

router.post('/login', function(req, res, next) {
  console.log(req.body.user);
  console.log(req.body.pass);
});

module.exports = router;
