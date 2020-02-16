const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

//const db = require('./db')
const studyspaceRouter = require('./routes/studyspace-router')

const app = express()
const apiPort = 3000

const mongoUtil = require( './mongoUtil' );

mongoUtil.connectToServer( function( err, client ) {
  if (err) console.log(err);

  app.use(bodyParser.urlencoded({ extended: true }))
  app.use(cors())
  app.use(bodyParser.json())

  const db = mongoUtil.getDb();
  const cursor = db.collection('Myhal_Centre').find();

  console.log("Areas:");
  cursor.each(function(err, doc) {
      console.log(doc);
  });

  app.use('/api', studyspaceRouter)

  app.listen(apiPort, () => console.log(`Server running on port ${apiPort}`))
} );
