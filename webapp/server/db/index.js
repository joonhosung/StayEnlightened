const MongoClient = require( 'mongodb' ).MongoClient;
const url = "mongodb://localhost:27017";

var _db;

module.exports = {

  connectToServer: function( callback ) {
    MongoClient.connect( url,  { useNewUrlParser: true }, function( err, client ) {
      _db  = client.db('Workspaces');
      return callback( err );
    } );
  },

  getDb: function() {
    return _db;
  }
};

/*const { MongoClient } = require('mongodb');

let _db;

// connection string
const uri = "mongodb+srv://web:webster@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority";

const client = new MongoClient(uri);

try {
    // Connect to the MongoDB cluster
    client.connect();

    _db = client.db('Workspaces')

} catch (e) {
    console.error(e);
} finally {
    // Close the connection to the MongoDB cluster
    client.close();
}

module.exports = _db*/

/*const MongoClient = require('mongodb').MongoClient;

let _db;

// connection string
const uri = "mongodb+srv://web:webster@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority"
MongoClient.connect(uri, function(err, client) {
   if(err) {
        console.log('Error occurred while connecting to MongoDB Atlas...\n',err);
   }

   console.log('Connected...');

   _db = client.db("Workspaces");

   const collection = client.db("Workspaces").collection("Myhal_Centre");

   // perform actions on the collection object
   client.close();
});

module.exports = _db
*/

/*const MongoClient = require('mongodb').MongoClient;

// replace the uri string with your connection string.
const uri = "mongodb+srv://web:webster@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority"
MongoClient.connect(uri, function(err, client) {
   if(err) {
        console.log('Error occurred while connecting to MongoDB Atlas...\n',err);
   }
   console.log('Connected...');
   const collection = client.db("Workspaces").collection("Myhal_Centre");
   // perform actions on the collection object
   client.close();
});

const db = MongoClient.connection

module.exports = db
*/




/*const mongoose = require('mongoose')


mongoose
    .connect('mongodb://127.0.0.1:27017/cinema', { useNewUrlParser: true })
    .catch(e => {
        console.error('Connection error', e.message)
    })

const db = mongoose.connection

module.exports = db*/
