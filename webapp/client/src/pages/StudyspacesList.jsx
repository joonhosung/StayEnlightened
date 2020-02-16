import React, { Component } from 'react'
import ReactTable from 'react-table-6'
import api from '../api'

import styled from 'styled-components'

import 'react-table-6/react-table.css'

const Wrapper = styled.div`
    padding: 0 40px 40px 40px;
`

class StudyspacesList extends Component {
    constructor(props) {
        super(props)
        this.state = {
            studyspaces: [],
            columns: [],
            isLoading: false,
            building: this.props.building,
        }
    }

    componentDidMount = async () => {
        this.setState({ isLoading: true })

        await api.getStudyspacesByBuilding(this.props.building).then(studyspaces => {
            this.setState({
                studyspaces: studyspaces.data,
                isLoading: false,
            })
        })
    }

    render() {
        const { studyspaces, isLoading } = this.state
        console.log('TCL: StudyspacesList -> render -> studyspaces', studyspaces)

        const columns = [
            {
                Header: 'Building',
                accessor: 'building',
                filterable: true,
            },
            {
                Header: 'Floor',
                accessor: 'name',
                filterable: true,
            },
            {
                Header: 'Max Occupancy',
                accessor: 'max',
                filterable: true,
            },
            {
                Header: 'Current Occupancy',
                accessor: 'current',
                filterable: true,
            },
        ]

        let showTable = true
        if (!studyspaces.length) {
            showTable = false
        }

        for (const studyspace of studyspaces){
          studyspace["building"] = this.props.building
        }

        return (
            <Wrapper>
                {showTable && (
                    <ReactTable
                        data={studyspaces}
                        columns={columns}
                        loading={isLoading}
                        defaultPageSize={10}
                        showPageSizeOptions={true}
                        minRows={0}
                    />
                )}
            </Wrapper>
        )
    }
}

export default StudyspacesList
