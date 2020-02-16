const { MongoClient } = require('mongodb');
const ObjectId = require('mongodb').ObjectID;

async function main() {
    /**
     * Connection URI. Update <username>, <password>, and <your-cluster-url> to reflect your cluster.
     * See https://docs.mongodb.com/ecosystem/drivers/node/ for more details
     */
    const uri = "mongodb+srv://web:webster@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority";

    /**
     * The Mongo Client you will use to interact with your database
     * See https://mongodb.github.io/node-mongodb-native/3.3/api/MongoClient.html for more details
     */
    const client = new MongoClient(uri);

    try {
        // Connect to the MongoDB cluster
        await client.connect();

        // Make the appropriate DB calls
        //await listDatabases(client);
        //await listAreas(client);
        //await findFloor(client)
        building_collections = await client.db('Workspaces').listCollections().toArray()
        buildings = []
        for await (const building of building_collections) {
          buildings.push(building["name"])
        }
        await console.log(buildings)
        //await console.log(building_collections)
        //await console.log(building_collections[1]["name"])

    } catch (e) {
        console.error(e);
    } finally {
        // Close the connection to the MongoDB cluster
        await client.close();
    }
}

main().catch(console.error);

/**
 * Print the names of all available databases
 * @param {MongoClient} client A MongoClient that is connected to a cluster
 */
async function listDatabases(client) {
    databasesList = await client.db().admin().listDatabases();
    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));

};

async function listAreas(client) {
    var cursor = client.db('Workspaces').collection('Myhal_Centre').find();

    console.log("Areas:");
    cursor.each(function(err, doc) {
        console.log(doc);
    });

};

async function findFloor(client) {
    var floor = client.db('Workspaces').findOne({ area: "5th" }, function(err, document) {
      console.log(document.name);
    })

    console.log("now:" + floor)

};
