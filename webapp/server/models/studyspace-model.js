const mongoose = require('mongoose')
const Schema = mongoose.Schema

const Studyspace = new Schema(
    {
        building: { type: String, required: true },
        area: { type: String, required: true },
        max: { type: Number, required: true },
    },
    { timestamps: true },
)

module.exports = mongoose.model('studyspace', Studyspace)
