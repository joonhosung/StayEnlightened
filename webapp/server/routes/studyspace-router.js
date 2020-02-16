const express = require('express')

const StudyspaceCtrl = require('../controllers/studyspace-ctrl')

const router = express.Router()

router.get('/studyspace/:id', StudyspaceCtrl.getStudyspaceById)
router.get('/studyspaces', StudyspaceCtrl.getStudyspaces)
router.get('/area/:name', StudyspaceCtrl.getStudyspaceByName)
router.get('/', StudyspaceCtrl.defaultstuff);

module.exports = router
