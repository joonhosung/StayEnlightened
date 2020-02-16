import axios from 'axios'

const api = axios.create({
    baseURL: 'https://server-dot-stayenlightenedv2.appspot.com/api',
})

export const getStudyspaces = () => api.get(`/studyspaces`)
export const getStudyspaceById = id => api.get(`/studyspace/${id}`)
export const getStudyspacesByBuilding = (building) => api.get(`/studyspaces/${building}`)
export const getBuildings = () => api.get(`/buildings`)

const apis = {
    getStudyspaces,
    getStudyspaceById,
    getStudyspacesByBuilding,
    getBuildings,
}

export default apis
