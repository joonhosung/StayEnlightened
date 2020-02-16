const Studyspace = require('../models/studyspace-model')
const mongoUtil = require( '../mongoUtil' );
const ObjectId = require('mongodb').ObjectID;

defaultstuff = function(req,res){
  return res.json({'message' : 'Ping Successfull'});
}

getStudyspaceById = async (req, res) => {
    const db = await mongoUtil.getDb();
    await db.collection('Myhal_Centre').findOne({ "_id": ObjectId(req.params.id) }, (err, studyspace) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!studyspace) {
            return res
                .status(404)
                .json({ success: false, error: `Study space not found` })
        }
        return res.status(200).json({ success: true, data: studyspace })
    }).catch(err => console.log(err))
}

getStudyspaceByName = async (req, res) => {
    const db = await mongoUtil.getDb();
    await db.collection('Myhal_Centre').findOne({ "name": req.params.name }, (err, studyspace) => {
        if (err) {
            return res.status(400).json({ success: false, error: err })
        }

        if (!studyspace) {
            return res
                .status(404)
                .json({ success: false, error: `Study space not found` })
        }
        return res.status(200).json({ success: true, data: studyspace })
    }).catch(err => console.log(err))
}

getStudyspaces = async (req, res) => {
    const db = mongoUtil.getDb();
    studyspacesList = await db.collection('Myhal_Centre').find({})
    studyspaceJSON = await JSON.stringify(await studyspacesList.toArray())
    return res.json(await studyspacesList.toArray());
}

module.exports = {
    getStudyspaces,
    getStudyspaceById,
    getStudyspaceByName,
    defaultstuff,
}
