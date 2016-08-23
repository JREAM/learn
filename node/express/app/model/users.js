var mongoose = require('mongoose');
var usersSchema = new mongoose.Schema({
  name: String,
  pass: String,
  is_active: Boolean
});
mongoose.model('Users', usersSchema);