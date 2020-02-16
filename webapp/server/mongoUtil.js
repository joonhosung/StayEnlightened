const MongoClient = require( 'mongodb' ).MongoClient;
const uri = "mongodb+srv://web:webster@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority";

var _db;

module.exports = {

  connectToServer: function( callback ) {
    MongoClient.connect( uri,  { useNewUrlParser: true }, function( err, client ) {
      _db  = client.db('Workspaces');
      return callback( err );
    } );
  },

  getDb: function() {
    return _db;
  }
};
